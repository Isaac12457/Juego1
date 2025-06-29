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
def draw():
    pantalla.blit(FOND, (0, 0))
    for segmento in serpiente:
        pygame.draw.circle(pantalla, NEGRO, segmento, radio)  # Dibuja toda la serpiente
    pygame.draw.rect(pantalla, ROJO, comida)  # Dibuja comida
    pygame.display.update()

# Función para mostrar "GAME OVER" y permitir reiniciar
def game_over():
    pantalla.fill(NEGRO)
    texto_grande = fuente.render("GAME OVER", True, ROJO)
    fuente_pequeña = pygame.font.Font(None, 30)
    texto_pequeño = fuente_pequeña.render("Presiona ESPACIO para reiniciar", True, (255, 255, 255))

    pantalla.blit(texto_grande, (ANCHO // 2 - 100, ALTO // 2 - 50))
    pantalla.blit(texto_pequeño, (ANCHO // 2 - 160, ALTO // 2 + 20))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
                    reiniciar_juego()

# Función para reiniciar el juego
def reiniciar_juego():
    global x, y, dx, dy, comida, serpiente
    x, y = 125, ALTO // 2
    dx, dy = SERPIENTE_VEL, 0
    serpiente = [(x, y)]  # Reiniciar la serpiente
    comida.x, comida.y = random.randint(0, ANCHO - comida_ANCHO), random.randint(0, ALTO - comida_ALTO)
    main()
    
    
def victoria():
    pantalla.fill(NEGRO)
    texto_grande = fuente.render("¡VICTORIA!", True, VERDE)
    texto_pequeño = fuente.render("Presiona ESPACIO para reiniciar", True, (255, 255, 255))

    pantalla.blit(texto_grande, (ANCHO // 2 - 100, ALTO // 2 - 50))
    pantalla.blit(texto_pequeño, (ANCHO // 2 - 160, ALTO // 2 + 20))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
                    reiniciar_juego()



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
                           main()
                        elif nombre == "reglas":
                          mostrar_reglas()
                        elif nombre == "estadisticas":
                          print("Estadísticas en construcción 🛠️")
                         
                        elif nombre == "salir":
                          pygame.quit()
                          sys.exit()


                presiono = False
                
                

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
    pantalla.blit(fuente_adver.render("Presiona ESC para volver al menu", True, ROJO), (100, 350))
    
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


    
# Bucle principal del juego
def main():
    global x, y, dx, dy

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
        serpiente.insert(0, cuerpo)  # Insertar nueva posición

        # Detectar si la cabeza toca la comida
        distancia = math.sqrt((serpiente[0][0] - comida.x)**2 + (serpiente[0][1] - comida.y)**2)

        # Si la distancia es menor al radio de la serpiente + margen pequeño, considera que ha comido
        if distancia < radio + 5:

            while True:  # Generar nueva posición sin superponerse con la serpiente
                x_comida = random.randint(0, ANCHO - comida_ANCHO)
                y_comida = random.randint(0, ALTO - comida_ALTO)
                nueva_comida = (x_comida, y_comida)
                if nueva_comida not in serpiente:
                    comida.x, comida.y = nueva_comida
                    break
        else:
            serpiente.pop()  # Si no come, eliminar el último segmento

        # Colisión con los bordes
        if cuerpo[0] <= 0 or cuerpo[0] >= ANCHO or cuerpo[1] <= 0 or cuerpo[1] >= ALTO:
            game_over()
            return
        if cuerpo in serpiente[1:]:
            game_over()
            return
        if len(serpiente) >= (ANCHO // radio) * (ALTO // radio):  # Si llena la pantalla
           victoria()
           return


           

        draw()
        reloj.tick(10)

if __name__ == "__main__":
    bienvenida()
    main()










