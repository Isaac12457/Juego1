# Juego1
# Juego de la serpiente - Proyecto de programacion
# Descripcion 
Este juego de la serpiente está realizado en Python utilizando la librería pygame para gráficos. Aquí documento todo mi proceso paso a paso.
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
# Pygame
Hice el principio del código de mi juego de la serpiente importando pygame para definir la pantalla y los colores. Creé un bucle principal para mantener la ventana abierta y permitir que Pygame se actualice correctamente.
