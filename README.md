# Juego1
# Juego de la serpiente - Proyecto de programacion
# Descripcion 
Este juego de la serpiente está realizado en Python utilizando diferentes bibliotecas para diferentes casos. Aquí documento todo mi proceso paso a paso.
# Requisitos
Antes de ejecutar el juego, se debe asegurar de tener instalado:
-Python 3.11
-pygame 2.6.1
# Python - Última versión
En este caso, tuve que descargar la última versión de Python para poder instalar Pygame y tener también disponible pip.
Ingresé a la página oficial de Python, descargué la última versión y le di clic a “Agregar al PATH”. Así, mi sistema reconoció a Python y pude instalar Pygame, tanto para mi laptop como para Spyder.
# Para instalar Pygame
Abrir la terminal del computador y escribir lo siguiente:
pip install pygame
Esto descargará automáticamente Pygame en el sistema.
# Configuración del entorno
Tuve que configurar Spyder para poder usar la versión correcta de Python:
Ruta: C:\Users\isaac\AppData\Local\Programs\Python313\python.exe
También instalé Pygame dentro de Spyder utilizando la terminal con el siguiente comando:
pip install pygame
# Verificacion de Pygame
Para comprobar que Pygame funcionaba correctamente en Spyder, escribí lo siguiente en la consola:
import pygame
pygame.init()
print("Pygame funciona")
El resultado fue el esperado. Me devolvió:
pygame 2.6.1 (SDL 2.28.4, Python 3.11.12)
Hello from the pygame community...
Pygame funciona
# Git
Descargué Git para poder guardar, administrar y conectar con GitHub, lo que me permite sincronizar fácilmente todo lo que tengo en mi computadora con mi repositorio en línea.
Los pasos que realicé fueron: buscar “descargar Git” en mi navegador, proceder a instalar la última versión (2.49.0), y luego comprobar que ya podía abrir Git Bash desde el explorador de archivos.
# GitHub
Abrí GitHub en el navegador y creé una cuenta. Una vez creada, generé un nuevo repositorio con el nombre Juego1, incluyendo un archivo README para poder documentar todo lo que voy haciendo en mi programa.
# Conexion de Git con GitHub
Primero abrí la carpeta donde quería clonar el repositorio desde GitHub a mi computadora. Luego, abrí Git Bash y ejecuté: git clone "el enlace que me dio GitHub" Después de clonar, utilicé: cd Juego1 para empezar a trabajar dentro de la carpeta del proyecto.
# Subir archivos
Para agregar el archivo .py que añadí a la carpeta Juego1, abrí Git Bash en esa carpeta y ejecuté:
git status
Git reconoció que había un nuevo archivo. Entonces usé los siguientes comandos para subirlo a GitHub:
git add .
git commit -m "Subida de archivo"
git push
Así subí mi primer commit al repositorio. Luego hice un git pull porque había realizado un cambio directamente en GitHub y quería actualizarlo en mi computadora.
# Bibliotecas
Utilicé cuatro bibliotecas diferentes para poder hacer mi código, ya que cada una me servía con un propósito distinto. Por ejemplo, Pygame me ayudó con los eventos y gráficos del juego; la tuve que importar con import pygame, colocándola siempre en la parte superior del programa.
Después importé tres bibliotecas más, que a diferencia de Pygame, no requieren una descarga manual porque ya vienen incluidas con Python. Estas son:
- random: La utilicé para ubicar la comida aleatoriamente. Sin esta biblioteca, la comida permanecería estática en el lugar donde se colocó inicialmente. La importé con el comando import random.
- sys: Esta biblioteca la usé para interactuar directamente con el sistema operativo y el intérprete. Así, cuando el jugador presiona la "X", puede salir del programa sin dificultad. También me permitió mostrar la palabra "GAME OVER" cuando se pierde, detener el programa y mostrar esa pantalla. La importé con import sys.
- math: Me dio acceso a funciones matemáticas más avanzadas. Al principio, la serpiente comía la manzana incluso cuando no estaba completamente cerca, lo que hacía que apareciera en otro lugar sin razón. Usando import math, pude calcular la distancia entre la cabeza de la serpiente y la comida, haciendo más precisa la detección y logrando que solo coma al tocarla completamente, como se tenía planeado desde el inicio.
# Pantalla y colores
Aquí creé diferentes variables, como "ANCHO" y "ALTO", siendo estas lo principal para definir el tamaño de la ventana. El tamaño final fue de 450 píxeles por lado, lo cual, a mi parecer, le da una buena estética al juego, ya que no se ve ni demasiado grande ni muy pequeño.
También utilicé el comando "pantalla = pygame.display.set_mode((ANCHO, ALTO))", que es lo que establece el tamaño de la ventana usando las variables definidas previamente. Igualmente, la ventana necesitaba un nombre, y esto lo logré con el comando "pygame.display.set_caption("SnakeGame")", haciendo que mi ventana se llame "SnakeGame".
Los colores los asigné con el formato RGB, que permite personalizar los colores dependiendo de los números que se establezcan en el comando. Yo usé:
- Negro para el fondo del Game Over y también para el color de la serpiente.
- Verde para las letras de victoria si se llega a ganar el juego.
- Rojo para el color de la comida.
# Serpiente y variables
Ya que decidí que la serpiente iba a ser dibujada con círculos, para ofrecer una mejor visualización al momento de jugar, asigné una variable llamada radio, que representa el radio que tendrá cada círculo de la serpiente. El valor del radio fue de 15 píxeles.
Para definir la velocidad de la serpiente, asigné la variable SERPIENTE_VEL con un valor de 15, lo que indica la cantidad de píxeles que avanzará por cada movimiento. También definí las variables x e y para contener la posición inicial de la serpiente en la pantalla. Además, creé la variable serpiente como una lista que almacena las coordenadas de todos los segmentos del cuerpo, lo que me permitió tener control sobre su longitud y forma.
# Comida
Creé dos variables para la comida que definen su alto y ancho, y las llamé comida_ALTO y comida_ANCHO. Cada una tiene un valor de 15, ya que decidí que la comida debía ser más pequeña que la serpiente, para que se notara visualmente que era un objeto diferente.
También la hice cuadrada utilizando el comando comida = pygame.Rect(...). Dentro del paréntesis coloqué las coordenadas y el tamaño correspondiente, usando las variables que había definido. Además, utilicé la biblioteca random para que la comida aparezca en diferentes lugares aleatoriamente, gracias al comando random.randint(...), logrando así que cada vez que se genere una nueva comida, aparezca en una posición distinta dentro de la ventana.\
# Movimiento
Como en todo o que he hecho, tuve que crear variables para controlar el movimiento. En este caso fueron dx y dy, que indican la dirección actual de la serpiente. Yo quise que comenzara moviéndose hacia la derecha, así que a dx le asigné la velocidad de la serpiente, y a dy le puse un valor de 0, de forma que el movimiento inicial fuese únicamente horizontal, como era lo deseado.
# Recursos externos
Para mi juego decidí que no quería tener un fondo de un solo color, así que le agregué una imagen de fondo. Para esto, creé una variable llamada FOND, y le asigné el siguiente comando:
FOND = pygame.image.load("...").convert(), este comando me ayudó a lograr el objetivo de mostrar una imagen .jpg como fondo del juego. El archivo de la imagen debe estar dentro del mismo directorio que el código, y su nombre se coloca dentro de los paréntesis.
Utilicé ese mismo comando en la función bienvenida, donde coloqué otra imagen que sirve como pantalla inicial del juego. En ella se muestra un mensaje de bienvenida y también qué botón debe presionar el jugador para comenzar.
# Reloj configuracion
Tuve que añadir un reloj, ya que algo tenía que controlar los FPS a los que corre el juego. Con este comando lo solucioné: pygame.time.Clock(). Esto controla la velocidad del juego limitando los FPS, para que en cualquier computador donde se ejecute, funcione de la misma manera.
# Dibujar los objetos
Para todas las variables asignadas anteriormente, se necesitan comandos que permitan dibujarlas correctamente. Por eso, creé una función llamada draw, donde incluí todo lo que debe representarse en la ventana. Allí coloqué el fondo usando pantalla.blit(FOND, (0, 0)), lo cual pone la imagen desde la esquina superior izquierda de la pantalla (posición (0, 0)).
Luego, utilicé un bucle for para recorrer la lista de la serpiente y dibujar cada fragmento. También incluí cómo dibujar la serpiente (con círculos) y la comida (con cuadrados). Al final, usé pygame.display.update() para que se actualice la pantalla y se reflejen todos los cambios.
# Función “GAME OVER”
Realicé esta función para reunir todo lo relacionado con la pantalla de derrota, que aparece si la serpiente choca con los bordes o consigo misma. Incluí el texto "GAME OVER" y otro que dice "Presiona ESPACIO para reiniciar", junto con la fuente y posición adecuada para que estén centrados. También usé .fill(NEGRO) para darle un fondo, el cual se puede definir como variable o directamente en formato RGB.
# Función Victoria
Mi idea aquí fue que si la serpiente llenaba toda la ventana, se mostrara una pantalla con el mensaje "VICTORIA" y también la opción de reiniciar presionando la tecla espacio. Se implementó un bucle para que el jugador pudiera cerrar la ventana con la "X" o reiniciar el juego con espacio. Incluí los textos respectivos, sus fuentes, colores y tamaños.

# Función para reiniciar el juego
Primero, declaré como global las variables necesarias como x, y, dx, comida y serpiente para poder usarlas dentro de la función, ya que están definidas afuera. Esta función reinicia el estado del juego y llama a la función main(), volviendo todo a su posición inicial.
# Función de bienvenida
Aquí declaré la variable INI (de "inicio") para cargar la imagen de bienvenida con pygame.image.load("...").convert(). También usé pygame.transform.scale(INI, (ANCHO, ALTO)) para ajustar la imagen al tamaño completo de la ventana. Luego, dentro de un bucle, se muestra la imagen y se detecta si el jugador presiona una tecla para empezar o la "X" para salir.
# Bucle principal del juego (main())
Esta es la parte central del código, la que hace funcionar el juego. Primero declaré como global las variables x, y, dx y dy, para poder usarlas dentro de main() si fueron definidas fuera. Después creé un bucle que mantiene el juego corriendo mientras la ventana no se cierre. Usé if evento.key == pygame.K_... para detectar las teclas que el jugador presiona (arriba, abajo, izquierda, derecha) y cambiar el movimiento de la serpiente con base en SERPIENTE_VEL.
Dentro del mismo bucle, se actualiza la posición de la serpiente sumando (dx, dy) a (x, y). Utilizando la biblioteca math, calculo la distancia entre la cabeza de la serpiente y la comida para detectar colisiones. También implementé las condiciones para perder: chocar contra los bordes o con su propio cuerpo, lo que activa la pantalla de "GAME OVER".
Al final, usé este bloque:
python
if __name__ == "__main__":
    bienvenida()
    main_con_estado(intentos_maximos, 0, 0, 0)
Este bloque permite que el juego inicie correctamente mostrando la pantalla de bienvenida, y luego comience el bucle principal.
#ACTUALIZACION
#Menu principal interactivo
Cuenta con cuatro botones visuales que el jugador puede seleccionar con el mouse:
- Jugar: Inicia el juego tras ingresar nombre e intentos (1 a 3).
- Reglas: Explica cómo jugar y qué condiciones provocan pérdida.
- Estadísticas: Muestra todas las partidas anteriores y un resumen total.
- Salir: Cierra el programa de forma segura.
#Funciones y mejoras implementadas
- Gestión de intentos: El jugador no pierde de inmediato. Puede fallar hasta tres veces.
- Sistema de estadísticas: Se almacena cada partida con manzanas comidas, colisiones con pared y con cuerpo.
- Aumento de dificultad: La velocidad aumenta automáticamente cada pocas manzanas.
- Pantalla de victoria: Si se llena el tablero, se muestra una pantalla de "¡VICTORIA!" y se guarda la partida.
- Nombre personalizado: Cada jugador ingresa su nombre al comenzar.
- Regreso al menú: Desde cualquier pantalla, se puede volver al menú presionando ESC.
#Comida
Ahora al comer 2 manzanas se aumenta la velocidad de la serpiente
#Concluciones
Este proyecto fue un gran desafío que me permitió practicar todo lo aprendido durante el curso: estructuras de control, funciones, eventos, manejo de listas, y lógica de juego. Aprendí a dividir tareas por funciones, a detectar colisiones con precisión, y a crear una experiencia completa para el usuario con menús, pantallas finales y seguimiento de estadísticas. También fortalecí habilidades de trabajo con bibliotecas externas, solución de errores y documentación del proceso. Me siento orgulloso del resultado final: un juego funcional, visualmente atractivo, y completo a nivel técnico.












