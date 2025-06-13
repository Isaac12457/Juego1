# Juego1
# Juego de la serpiente - Proyecto de programacion
# Descripcion 
Este juego de la serpiete esta realizado en python utilizando la librería de **pygame** para graficos. Aquí documento todo mi proceso paso a paso.
# Requisitos
Antes de ejecutar el juego, se de asegurar de tener instalado:
- Python 3.11
- pygame 2.6.1
# Python ultima version
En este caso tuve que descargar la ultima version de python para poder descargar pygame y que igualmente tener el pip.
Ingrese a la pagina oficial de Python y descargue la ultima version y le di click a agregar al path y ahi mi sistema reconocio a Python y pude descargar Pygame para mi laptop y para Spider.
# Para instalar pygame
Abrir la terminal del computador poner lo siguiente:
pip install pygame
Esto descargara automaticamente pygame al sistema.
# Configuración del entorno
Tuve que confiurar Spider para poder usar la version correcta de Python:
Ruta: C:\Users\isaac\AppData\Local\Programs\Python313\python.exe
Tambien istale el pygame dentro de Spider con la terminal y con lo siguinte: pip istall pygame
# Verificacion de Pygame
Tuve que ver que pygame este funcionando de la mejor manera en Spyder lo que hice fue poner lo siguiente en la consola de Spider: import pygame
                                           pygame.init()
                                           print("Pygame funciona")
El resultado fue el esperado me devolvio: pygame 2.6.1 (SDL 2.28.4, Python 3.11.12)
                                          Hello from the pygame community...
                                          Pygame funciona
# Git
Descargue git para poder guardar, administrar y conectar con github para poder hacer todos los cambios y que todo lo que este en mi computadora se pueda trasmitir sin problema a github.
Los pasos que realize fueron: buscar "descargar git" en mi navegador y proceder a descargar la ultima version que es la 2.49.0 y pocedi a ver si ya podia abrir el Bash desde archivos y se logro.
# GitHub
Abri GitHub dentro del navegador y cree una cuenta, una vez creada la cuenta cree un nuevo repositorio con el nombre de Juego1 con ReadMe asi podria anotar todo lo que estoy haciend en mi programa.
# Conexion de Git con GitHub
Primero abri donde queria que se clonara lo que tenia en GitHub a mi computadora, despues abri el bash de Git y puse git clone: "el link que me dio GitHub" asi ya se clono y pude despues de eso solo tuve que poner cd Juego1 para empezar a trabajar.
# Subir archivos
Para poder agregar el archivo .py que agrege a la carpeta Juego1, en mi terminal tuve que abrir el bash de Git y poner "git status" para ver lo que cambio y reconocio que habia algo nuevo que era el archivo ".py" asi que para agregarlo en GitHub puse los siguientes comandos: git add, git commit -m "subida de archivo" y al ultimo git push, asi se subio mi primer commit a GitHub. Tambien hice un git pull despues porque cambie algo en GitHub para que se cambie en mi computadora.
# Pygame
Hice el principio de codigo de mi juego de la serpiente importando pygame para que me pueda ayudar a poder definir la pantalla y los colores, hice un bucle para que se mantenga la ventana abierta y que permita que pygame se actualice de la mejor manera.
