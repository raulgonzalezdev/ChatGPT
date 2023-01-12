# Translate Whiseper with ChatGPT

## Ao rodar o projeto pela primeira vez
### No Windows
- *Para criar uma virtual env* ```py -m venv env```
- *Ativando a virtual env:* ```.\env\Scripts\activate``` 
### No Linux
- É necessário ter a biblioteca: ```pip install virtualenv```
- *Para criar uma virtual env* ```virtualenv env```
- *Ativando a virtual env:* ```source env/bin/activate``` 

----
--- 



- ```pip install -r requirements.txt```   para instalar as dependências necessárias


## en caso de error con libriar pyaudio

``` sudo apt install build-essential portaudio19-dev python3.10-dev ```
```  pip install pyaudio ```

## en caso de error de whipser  siga estos pasos

``` pip install git+https://github.com/openai/whisper.git  ```

Para actualizar el paquete a la última versión de este repositorio, ejecute:

``` pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git ```

También requiere que la herramienta de línea de comandos esté instalada en su sistema, que está disponible en la mayoría de los administradores de paquetes:ffmpeg

# on Ubuntu or Debian

``` sudo apt update && sudo apt install ffmpeg ```

# on Windows using Scoop (https://scoop.sh/)
``` scoop install ffmpeg ```

## Para rodar o banco de dados
- no arquivo .env mudar a senha do banco para a sua senha local


### Start no servidor
- ```python ChatGpt.py```


 ## abra una ventana de navegador y use la app
``` http://localhost:7860 ```

# Servidor pronto para ser acessado em localhost:7860/

----
### Se preciso for incluir uma nova biblioteca no projeto, lembrar de adicionar ela a lista de bibliotecas do projeto com o comando
- ```pip freeze > requirements.txt```