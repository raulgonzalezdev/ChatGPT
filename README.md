#OpenAI Whisper and ChatGPT Gradio Web UI

Este proyecto combina las tecnologías Whisper y ChatGPT de OpenAI para crear una interfaz web de usuario de grado. Whisper es una biblioteca de lenguaje natural de OpenAI que permite a los desarrolladores generar texto a partir de una variedad de entradas, como audio, video, texto y más. ChatGPT es un modelo de lenguaje de OpenAI que es capaz de generar texto coherente y coherente en una variedad de tareas de lenguaje natural. Juntos, estas tecnologías permiten a los desarrolladores crear una interfaz de usuario de grado que puede transcribir audio y generar respuestas en tiempo real.

## Running the project for the first time

##Requisitos previos

- *Python 3.6 o superior*
- *Una cuenta en OpenAI y una llave de API válida*
- *ffmpeg instalado en su sistema*



##Instrucciones de instalación

##Creando un ambiente virtual

Para evitar conflictos con otras librerías y tener un control más preciso de las dependencias del proyecto, es recomendable utilizar un ambiente virtual.

##Windows

Crear una virtual env: py -m venv env
Activar la virtual env: .\env\Scripts\activate

##Linux

Instalar virtualenv: pip install virtualenv

Crear una virtual env: virtualenv env

Activar la virtual env: source env/bin/activate

Instalar las dependencias necesarias: pip install -r requirements.txt

Solución de problemas

Error con la librería pyaudio

sudo apt install build-essential portaudio19-dev python3.10-dev
pip install pyaudio

Error con Whisper
pip install git+https://github.com/openai/whisper.git

Actualizar Whisper

pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

Instalar ffmpeg
Ubuntu/Debian: sudo apt update && sudo apt install ffmpeg
Windows: scoop install ffmpeg

Ejecutar el servidor

python ChatGpt.py

Abrir una ventana de navegador en http://localhost:7860

Añadir una nueva biblioteca
pip freeze > requirements.txt

Nota: Recuerda cambiar la contraseña del banco de datos en el archivo .env antes de ejecutar el proyecto

Reseña

¡Acabamos de lanzar nuestro proyecto de #OpenAI! Una combinación de Whisper y ChatGPT en una interfaz web de usuario con Gradio. Genera texto a partir de audio y responde preguntas de manera natural.

Este proyecto combina las tecnologías Whisper de OpenAI y ChatGPT para crear una interfaz web de usuario utilizando Gradio. Whisper es una herramienta de generación de lenguaje que permite generar texto a partir de un audio de entrada. ChatGPT es un modelo de lenguaje de OpenAI que se utiliza para responder preguntas y generar texto de manera natural.


 ¡Chequea nuestro repositorio para más detalles!