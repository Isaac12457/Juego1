#Ventana de Juego
import pygame 
#Iniciamos pygame
pygame.init()       
#Definir pantalla y colores
ANCHO, ALTO= 600, 400
pantalla= pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SnakeGame")
AZUL= (0,0,50)
CIAN= (0,255,255)
#Configuracion de funte de texto
fuente= pygame.font.Font(None,80)
#Bucle principal con tecla de inicio
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  
                 print("¡Inicio del juego!") 
        
    pantalla.fill(AZUL)
    #Intrucciones
    fuente1= pygame.font.Font(None,30)
    instrucciones = fuente1.render("Presiona ENTER para jugar", True, CIAN)
    pantalla.blit(instrucciones, (ANCHO // 2 - 140, ALTO // 2 + 40))
    
    

     
#Efecto neon
    pygame.draw.line(pantalla, CIAN, (50, 50), (550, 50), 3)
    pygame.draw.line(pantalla, CIAN, (50, 350), (550, 350), 3)
    pygame.draw.line(pantalla, CIAN, (50, 50), (50, 350), 3)
    pygame.draw.line(pantalla, CIAN, (550, 50), (550, 350), 3)
#Texto de bienvenida
    texto = fuente.render("¡SNAKE GAME!", True, CIAN)
    pantalla.blit(texto, (ANCHO // 2 - 205, ALTO // 2 - 20))

    pygame.display.update()
pygame.quit()
    


