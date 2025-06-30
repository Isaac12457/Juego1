import pygame
import random
import sys
import math

# Inicializar pygame
pygame.init()

# Definir pantalla y colores
ANCHO, ALTO = 450, 450
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SnakeGame")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
CELESTE=(0, 255, 255)

#Funciones para las estadisticas
nombre_jugador= ""
intentos_maximos = 0
total_col_pared = 0
total_col_cuerpo = 0
total_manzanas = 0
historial_partidas = []
# Configuración inicial de la serpiente
radio = 15
SERPIENTE_VEL = 15
x, y = 125, ALTO // 2
serpiente = [(x, y)]

# Configuración inicial de la comida
comida_ANCHO, comida_ALTO = 15, 15
comida = pygame.Rect(random.randint(0, ANCHO - comida_ANCHO), random.randint(0, ALTO - comida_ALTO), comida_ANCHO, comida_ALTO)

# Variables de movimiento
dx, dy = SERPIENTE_VEL, 0

# Cargar imagen de fondo
FOND = pygame.image.load("cesped.jpg").convert()

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Fuente para "GAME OVER"
fuente = pygame.font.Font(None, 50)

#Botones del menu
ANCHO_boton= 200
ALTO_boton= 50
x_boton= (ANCHO-ANCHO_boton) //2
y_jugar = 100
y_reglas = y_jugar + 70
y_estadisticas = y_jugar + 140
y_salir = y_jugar + 210
rect_jugar= pygame.Rect(x_boton, y_jugar, ANCHO_boton, ALTO_boton)
rect_reglas= pygame.Rect(x_boton, y_reglas, ANCHO_boton, ALTO_boton)
rect_estadisticas= pygame.Rect(x_boton, y_estadisticas, ANCHO_boton, ALTO_boton)
rect_salir= pygame.Rect(x_boton, y_salir, ANCHO_boton, ALTO_boton)

# Diccionario 
botones = {"jugar": rect_jugar,
           "reglas": rect_reglas,
           "estadisticas": rect_estadisticas,
           "salir": rect_salir}



# Función para dibujar objetos en pantalla
def draw(nombre, intentos_restantes, manzanas_comidas):
    pantalla.blit(FOND, (0, 0))
    for segmento in serpiente:
        pygame.draw.circle(pantalla, NEGRO, segmento, radio)
    pygame.draw.rect(pantalla, ROJO, comida)

    fuente_info = pygame.font.Font(None, 30)
    texto_info = f"{nombre} | Intentos: {intentos_restantes} | Manzanas: {manzanas_comidas}"
    render_info = fuente_info.render(texto_info, True, (255, 255, 255))
    pantalla.blit(render_info, (10, 10))

    pygame.display.update()

# Función para mostrar "GAME OVER" y permitir reiniciar
def game_over():
    pantalla.fill(NEGRO)
    fuente_grande = pygame.font.Font(None, 90)
    texto_grande = fuente_grande.render("GAME OVER", True, ROJO)
    fuente_pequeña = pygame.font.Font(None, 30)
    texto_pequeño = fuente_pequeña.render("Presiona ESPACIO para salir del juego", True, (255, 255, 255))
    texto_esc= fuente_pequeña.render("Preciona ESC para regresar al menu", True, (255,255,255))
    
    pantalla.blit(texto_grande, (ANCHO // 2 - 180, ALTO // 2 - 100))
    pantalla.blit(texto_pequeño, (ANCHO // 2 - 180, ALTO // 2 + 20))
    pantalla.blit(texto_esc, (ANCHO // 2 - 175, ALTO // 2 + 80))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_ESCAPE:
                    menu_principal()
                    esperando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                    esperando = False

# Función para reiniciar el juego
def reiniciar_juego(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo):
    global x, y, dx, dy, comida, serpiente
    x, y = 125, ALTO // 2
    dx, dy = SERPIENTE_VEL, 0
    serpiente = [(x, y)]
    comida.x = random.randint(0, ANCHO - comida_ANCHO)
    comida.y = random.randint(0, ALTO - comida_ALTO)
    main_con_estado(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo)
    
    
def victoria():
    pantalla.fill(NEGRO)
    texto_grande = fuente.render("¡VICTORIA!", True, VERDE)
    texto_pequeño = fuente.render("Presiona ESPACIO para salir del juego", True, (255, 255, 255))
    texto_esc= fuente.render("Preciona ESC para regresar al menu", True, (255,255,255))

    pantalla.blit(texto_grande, (ANCHO // 2 - 100, ALTO // 2 - 50))
    pantalla.blit(texto_pequeño, (ANCHO // 2 - 180, ALTO // 2 + 20))
    pantalla.blit(texto_esc, (ANCHO // 2 - 175, ALTO // 2 + 80))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_ESCAPE:
                    menu_principal()
                    esperando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                    esperando = False



# Función de bienvenida
def bienvenida():
    INI = pygame.image.load("Bienvenida.jpg").convert()
    INI = pygame.transform.scale(INI, (ANCHO, ALTO))

    BORDE = INI.get_rect()
    BORDE.center = (ANCHO // 2, ALTO // 2)

    presionar = True
    while presionar:
        pantalla.blit(INI, BORDE)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    menu_principal()
                    presionar = False
    return

def menu_principal():
    presiono = True
    while presiono :
        dibujar_botones()# Muestra los botones
        
        pygame.display.update() #Actualiza la pantalla
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for nombre, rect in botones.items():
                     if rect.collidepoint(pos):
                        if nombre == "jugar":
                           pedir_datos_iniciales()                        
                           main_con_estado(intentos_maximos, 0, 0, 0)
                        elif nombre == "reglas":
                          mostrar_reglas()
                        elif nombre == "estadisticas":
                          mostrar_estadisticas()
                         
                        elif nombre == "salir":
                          pygame.quit()
                          sys.exit()


                presiono = False
                
def pedir_datos_iniciales():
    global nombre_jugador, intentos_maximos

    fuente = pygame.font.Font(None, 40)
    nombre_input = ""
    intentos_input = ""
    editando_nombre = True
    datos = True
    mostrar_ayuda = True  # Para mostrar la ayuda mientras no haya cambiado de campo

    while datos:
        pantalla.fill((254, 245, 218))

        # Título
        titulo = fuente.render("Ingresa los siguientes datos", True, (0, 0, 0))
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 40))

        # Campo nombre
        nombre_texto = fuente.render("Nombre:", True, (0, 0, 0))
        pantalla.blit(nombre_texto, (60, 120))
        nombre_escrito = fuente.render(nombre_input, True, (0, 0, 128))
        pantalla.blit(nombre_escrito, (200, 120))

        # Campo intentos
        intentos_texto = fuente.render("Intentos (1-3):", True, (0, 0, 0))
        pantalla.blit(intentos_texto, (60, 180))
        intentos_escrito = fuente.render(intentos_input, True, (0, 0, 128))
        pantalla.blit(intentos_escrito, (280, 180))

        # Indicador del campo activo (cursor)
        if editando_nombre:
            pygame.draw.line(pantalla, (0, 0, 0), (200 + len(nombre_input)*12, 140), (200 + len(nombre_input)*12, 120), 2)
        else:
            pygame.draw.line(pantalla, (0, 0, 0), (280 + len(intentos_input)*12, 200), (280 + len(intentos_input)*12, 180), 2)

        # Mensaje de ayuda (solo la primera vez)
        if mostrar_ayuda:
            ayuda_tab = fuente.render("Presiona TAB para cambiar", True, (100, 100, 100))
            pantalla.blit(ayuda_tab, (10, 310))

        # Mensaje de continuar
        if nombre_input.strip() != "" and intentos_input in ["1", "2", "3"]:
            continuar_texto = fuente.render("Presiona ENTER para comenzar", True, (0, 150, 0))
            pantalla.blit(continuar_texto, (10, 260))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    editando_nombre = not editando_nombre
                    mostrar_ayuda = False  # Ocultar mensaje de ayuda después de usar TAB

                elif evento.key == pygame.K_RETURN:
                    if nombre_input.strip() != "" and intentos_input in ["1", "2", "3"]:
                        nombre_jugador = nombre_input.strip()
                        intentos_maximos = int(intentos_input)
                        datos = False  # Salir del bucle

                elif evento.key == pygame.K_BACKSPACE:
                    if editando_nombre and len(nombre_input) > 0:
                        nombre_input = nombre_input[:-1]
                    elif not editando_nombre and len(intentos_input) > 0:
                        intentos_input = intentos_input[:-1]

                else:
                    if editando_nombre:
                        if len(nombre_input) < 15:
                            nombre_input += evento.unicode
                    else:
                        if evento.unicode in "123" and len(intentos_input) == 0:
                            intentos_input += evento.unicode
               

def dibujar_botones():
    
    pantalla.fill((108,59,42))
    fuente_menu= pygame.font.Font(None,100)
    texto_menu = fuente_menu.render("MENU", True, ROJO)

    pantalla.blit(texto_menu, (ANCHO // 2 - 100, ALTO // 2 - 200))
    
    
    for nombre, rect in botones.items():
        pygame.draw.rect(pantalla,(255,255,255), rect)
        color_texto= NEGRO
        texto= fuente.render(nombre.capitalize(),True, color_texto)
        texto_rect= texto.get_rect(center=rect.center)
        pantalla.blit(texto, texto_rect)
        
def mostrar_reglas():
    
    pantalla.fill((211,211,211))
    fuente_reglas= pygame.font.Font(None, 100)
    texto_reglas= fuente_reglas.render("REGLAS", True, CELESTE)
    fuente_adver= pygame.font.Font(None, 20)
    
    pantalla.blit(texto_reglas, (ANCHO // 2 - 150, ALTO // 2 - 200))
    pantalla.blit(fuente_adver.render("-Usa las flechas de tu teclado para moverte", True, NEGRO), (25, 150))
    pantalla.blit(fuente_adver.render("-Debes comer la comida para crecer y aumentar tu velocidad", True, NEGRO), (25, 200))
    pantalla.blit(fuente_adver.render("-Si topas la pantalla perderas intentos y sera un GAME OVER", True, NEGRO), (25, 250))
    pantalla.blit(fuente_adver.render("-Evita tocar tu cuerpo o perderas intentos y sera GAME OVER", True, NEGRO), (25, 300))
    pantalla.blit(fuente_adver.render("-Elije el numero de intentos del 1-3", True, NEGRO), (25, 350))
    pantalla.blit(fuente_adver.render("Presiona ESC para volver al menu", True, ROJO), (100, 400))
    
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                menu_principal()
                esperando = False

def mostrar_estadisticas():
    pantalla.fill((204, 169, 221))
    
    fuente_texto = pygame.font.Font(None, 30)
    y_offset = 100

    sum_manzanas = 0
    sum_pared = 0
    sum_cuerpo = 0

    for i, partida in enumerate(historial_partidas, 1):
        texto = f"Partida {i}: {partida['manzanas']}, {partida['col_pared']}, {partida['col_cuerpo']}"
        render = fuente_texto.render(texto, True, (255, 255, 255))
        pantalla.blit(render, (20, y_offset))
        y_offset += 30
        sum_manzanas += partida['manzanas']
        sum_pared += partida['col_pared']
        sum_cuerpo += partida['col_cuerpo']

    y_offset += 20  # un pequeño espacio antes del resumen
    resumen_total = [
        f"TOTAL: {sum_manzanas + sum_pared + sum_cuerpo}",
        f"Manzanas: {sum_manzanas}",
        f"Colisiones: {sum_pared}",
        f"Cuerpo: {sum_cuerpo}"]

    for linea in resumen_total:
        texto = fuente_texto.render(linea, True, (0, 255, 0))
        pantalla.blit(texto, (20, y_offset))
        y_offset += 30




    volver = fuente_texto.render("Presiona ESC para volver", True, ROJO)
    pantalla.blit(volver, (ANCHO//2 - volver.get_width()//2, ALTO - 40))

    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                esperando = False
                menu_principal()
    

    
# Bucle principal del juego
def main():
    global x, y, dx, dy, total_col_pared, total_col_cuerpo, total_manzanas, historial_partidas

    manzanas_comidas = 0
    intentos_restantes = intentos_maximos
    colisiones_cuerpo = 0
    colisiones_pared = 0
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx, dy = -SERPIENTE_VEL, 0
                if evento.key == pygame.K_RIGHT:
                    dx, dy = SERPIENTE_VEL, 0
                if evento.key == pygame.K_UP:
                    dx, dy = 0, -SERPIENTE_VEL
                if evento.key == pygame.K_DOWN:
                    dx, dy = 0, SERPIENTE_VEL

        # Mover la serpiente
        x += dx
        y += dy
        cuerpo = (x, y)
        serpiente.insert(0, cuerpo)

        # Detectar si comió la manzana
        distancia = math.sqrt((serpiente[0][0] - comida.x) ** 2 + (serpiente[0][1] - comida.y) ** 2)
        if distancia < radio + 5:
            manzanas_comidas += 1
            while True:
                x_comida = random.randint(0, ANCHO - comida_ANCHO)
                y_comida = random.randint(0, ALTO - comida_ALTO)
                nueva_comida = (x_comida, y_comida)
                if nueva_comida not in serpiente:
                    comida.x, comida.y = nueva_comida
                    break
        else:
            serpiente.pop()

        # Colisión con pared
        if cuerpo[0] <= 0 or cuerpo[0] >= ANCHO or cuerpo[1] <= 0 or cuerpo[1] >= ALTO:
            colisiones_pared += 1
            intentos_restantes -= 1

            if intentos_restantes == 0:
                total_col_pared += colisiones_pared
                total_col_cuerpo += colisiones_cuerpo
                total_manzanas += manzanas_comidas
                historial_partidas.append({
                    "manzanas": manzanas_comidas,
                    "col_pared": colisiones_pared,
                    "col_cuerpo": colisiones_cuerpo
                })
                game_over()
                return
            else:
                reiniciar_juego(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo)
                return

        # Colisión con su cuerpo
        if cuerpo in serpiente[1:]:
            colisiones_cuerpo += 1
            intentos_restantes -= 1

            if intentos_restantes == 0:
                total_col_pared += colisiones_pared
                total_col_cuerpo += colisiones_cuerpo
                total_manzanas += manzanas_comidas
                historial_partidas.append({
                    "manzanas": manzanas_comidas,
                    "col_pared": colisiones_pared,
                    "col_cuerpo": colisiones_cuerpo
                })
                game_over()
                return
            else:
                reiniciar_juego(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo)
                return

        if len(serpiente) >= (ANCHO // radio) * (ALTO // radio):
            victoria()
            return

        draw(nombre_jugador, intentos_restantes, manzanas_comidas)
        reloj.tick(10)
        return

def main_con_estado(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo):
    global x, y, dx, dy, total_col_pared, total_col_cuerpo, total_manzanas, historial_partidas

    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx, dy = -SERPIENTE_VEL, 0
                if evento.key == pygame.K_RIGHT:
                    dx, dy = SERPIENTE_VEL, 0
                if evento.key == pygame.K_UP:
                    dx, dy = 0, -SERPIENTE_VEL
                if evento.key == pygame.K_DOWN:
                    dx, dy = 0, SERPIENTE_VEL

        x += dx
        y += dy
        cuerpo = (x, y)
        serpiente.insert(0, cuerpo)

        distancia = math.sqrt((serpiente[0][0] - comida.x)**2 + (serpiente[0][1] - comida.y)**2)
        if distancia < radio + 5:
            manzanas_comidas += 1
            while True:
                x_comida = random.randint(0, ANCHO - comida_ANCHO)
                y_comida = random.randint(0, ALTO - comida_ALTO)
                if (x_comida, y_comida) not in serpiente:
                    comida.x, comida.y = x_comida, y_comida
                    break
        else:
            serpiente.pop()

        if cuerpo[0] <= 0 or cuerpo[0] >= ANCHO or cuerpo[1] <= 0 or cuerpo[1] >= ALTO:
            colisiones_pared += 1
            intentos_restantes -= 1
            if intentos_restantes == 0:
                total_col_pared += colisiones_pared
                total_col_cuerpo += colisiones_cuerpo
                total_manzanas += manzanas_comidas
                historial_partidas.append({
                    "manzanas": manzanas_comidas,
                    "col_pared": colisiones_pared,
                    "col_cuerpo": colisiones_cuerpo
                })
                game_over()
                return
            else:
                reiniciar_juego(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo)
                return

        if cuerpo in serpiente[1:]:
            colisiones_cuerpo += 1
            intentos_restantes -= 1
            if intentos_restantes == 0:
                total_col_pared += colisiones_pared
                total_col_cuerpo += colisiones_cuerpo
                total_manzanas += manzanas_comidas
                historial_partidas.append({
                    "manzanas": manzanas_comidas,
                    "col_pared": colisiones_pared,
                    "col_cuerpo": colisiones_cuerpo
                })
                game_over()
                return
            else:
                reiniciar_juego(intentos_restantes, manzanas_comidas, colisiones_pared, colisiones_cuerpo)
                return

        if len(serpiente) >= (ANCHO // radio) * (ALTO // radio):
           total_col_pared += colisiones_pared
           total_col_cuerpo += colisiones_cuerpo
           total_manzanas += manzanas_comidas
           historial_partidas.append({
               "manzanas": manzanas_comidas,
               "col_pared": colisiones_pared,
               "col_cuerpo": colisiones_cuerpo})
           victoria()
           return

        draw(nombre_jugador, intentos_restantes, manzanas_comidas)
        velocidad = min(25, 10 + manzanas_comidas // 2)
        reloj.tick(velocidad)





if __name__ == "__main__":
    bienvenida()
    main_con_estado(intentos_maximos, 0, 0, 0)










