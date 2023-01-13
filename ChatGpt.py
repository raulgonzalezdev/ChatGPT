import os
import openai
import whisper
import time
import gradio as gr
import warnings

# Supress any warnings
warnings.filterwarnings("ignore")

# Load the whisper model
model = whisper.load_model("base")

# Get the device that the model is running on
device = model.device

# Secret token for the ChatGPT API


OPENAI_API_KEY= "sk-"

openai.api_key = OPENAI_API_KEY
openai.organization ="org-"
openai.Model.list()


# define the model to use
model_engine = "text-davinci-003"


# Function to transcribe audio
def transcribe(audio):
    # Load audio and pad/trim
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    
    # Get the log mel spectrogram of the audio
    mel = whisper.log_mel_spectrogram(audio).to(device)
    
    # Detect the language of the audio
    _, probs= model.detect_language(mel)
    
    # Decode the audio using the whisper model
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    result_text = result.text
    
    # generate a response
    resp = openai.Completion.create(
        engine=model_engine,
        prompt=result_text,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    # Send the result text to the ChatGPT API and get the response
    print(resp)
    out_result = resp["choices"][0]["text"]
    
    return [result_text, out_result]

# Create the gradio UI
output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.Textbox(label="ChatGPT Output")

gr.Interface(
    title='OpenAI Whisper and ChatGPT Gradio Web UI',
    fn=transcribe,
    inputs=[gr.inputs.Audio(source="microphone", type="filepath")],
    outputs=[output_1, output_2],
    live=True
).launch()
