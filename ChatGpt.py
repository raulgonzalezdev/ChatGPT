from os import device_encoding
import whisper
import time
import gradio as gr
from pyChatGPT import ChatGPT
import warnings

warnings.filterwarnings("ignore")

# Load the model

secret_tocken = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..EuNAQxankC8er-ZP.Td8t1VqRqxKEGrgrpLoDUl5aUyOXQmtl5HbANeoY72qSvIt8XHbJ2055lwOF4H493Aj4Q5qgiVKcPfihXIoa27DZCP3oNHznZcmb-RcnQxFkKR2IZJMxFX5EalYJoSvOySYimpkOKBw55Tlvo0rY0wdqaUSufyCc_06HbRqNyEfvj5WKjz1quZrfWf0LSLX80oXyj8cUdijGBtjzEPBmaP74jt_VCTrWEnskkO4-LWffBY5-vIWTgaZYcMYAK5E1PfZdIw6pFig2XI6aJP8qjhtiLqe_EkhHQTgDFGRKfe9OFvc2LFjXJ58kW8tpl2c7U0KDUHs4IhKa_W6zzCTK6FiuFqR-HrttKjG7_P9WLTozATV_iKjdSmUJjZwgFLAVItRhB9etRddbWpq65Yn80WDk34J97R-Tv0GXCMA1_MogYUNjt6H5NANvK3DJsGa1JMcSyDDhB3IkbtLd3p4CXpmnodACShP5feoI9YUZiDBjbyHDoRpxIKqY_ntOCdzrqjGWUpxnKBHqQXvqIMGnSz_uoo5eYsUlH2lFrxQ3vXu5KnR77Ly1JUA3an_qLi5yNzWFuL-tNDOkO0a3DgQHi82xu7_WYnm4qKsXMY-eU30qEEfUbS4dcIimY1IUJG0hTAY9VJtpgcd-tVUiH3XBTH1z8pt4Kn6Ww1s_DsydG3EH3BvHTbANglKZXqYHpsB84-wLNSTWyZlFvMQkdDm91Dp419vWKqhVm7QS5nXLpUYXkn7WUU3fxGuwdKkRqTmPwx-p2n6AYaA1ZjqcF0uTP7isIMfU-OcBJI9oFyL0ltvwQElB3rmjEQzEXcwLdAv6NRHATRKQHzOrlSDVYQ2i1Vu0-Ik4UrVhVrToqwRv0PukUTPVDGl8IQGsMgXn9Z3-Qd3ogtlJZyKVpolP01MDhJzA-C8ySgzytivCoxnQFWkx8cioHNaceLnV3ZiWR4b2NT9pAGhtkUmPY2g9dcXsPseigIWj4SwNsYsQbu-hfe-sDzKG9yE0R5ZfN58TIQOEEx4cAs3f23b5MOqKnxkz8MWehl3Orlw7Pw3X8LEXscjVfb2Li7vJ1hy_mA171c7aaIPWuMphEl1axIVLVNuNNfkOmS05Vjq6YA3NcPlXNa2_viFo0kSG_pWMcV87OWNGCd_KwX_VUqA8i74qqwYW7XgHcPlvCrJUYNLZ9MqVDTrgsg5oYvB6YRrplCpRPh_5Ossv_PIW_IyDYcHJei5WnrECO5vSBxiy0USj4W0sOo9JQO_vbawHAJCo-XJjfiUuJ5uTB4Mr4OkUM7napf4CUw3Jq-XjhAzWYTXLKWdRZxLZiMbp11JiugXuV3Ky5NQsBBgY5-f_R9nzJKNHVCV-y9tHNvllN-7jxYVz898beMTiBoVFrPsLwJUh2OnTvDv4fw1zXBNw6IMCEULXjvJdhGRLPkZ-Q5tjZiRzA2A3V8x9-e_pgUKFossE5-XkLNrFQGun2LS3_ROtHQq04GmS6ZYaycfauIDtusPyxlKHnH-aRFjhlDapq7QMt4q06tnGTSl8vmoDlMN0C006rwdctftB7ZhS-gdRO9ycMxBruw-ltNIVd6s1ewgTY168ETrRqNbECp5HJQCtv_27yyPylOWhsVbPbLqLsS6jofnazY-EurIKbU2F_t7-HxPDLNUSW4OqKjKV9l3ku1QuR1OmNmLLqxFt9GYL7-C0vSf3U7TX33DISOY7QKuqp4wW6RBV9zR16z8Vj0I8VgumOEqoSTfnekG1zwzXoIQ-zmJbkowb5hzxCpWFRAGNmDFygAtlJib5Rocas4S0DmxS0P7uB0TTyB893L48Y63d3wwDL9X1GWCdz8e5st5PYz899VHyfhiVdPnwiLS4w7ojpZE1XZqHE4q_TijaHJI1mS3n8MUG_daaTJXiYcHqNl3U_Ee1QmuqTVhNFvqzQBs0oI87BVZuz3EVdj66UHhhpFKWjG5RUGHOR-c_Ishh9_YbgRYoFG4g7xec5BeucsY8b4TbMq01aemlBH2Es7B1UzIs0jl-_yHOTtvjlDvPvW36VviHNA5NYkkGIgOx26VwX_52IZ1BgB7hZTiJNNPs-vd6QM9iKlpBnnhTdZGvnV-v8NcBTdz_sKAVkcc1swZlQfO620rFftlnzYs0Ioje4tkvWNfbTkZi7wZz91_O-jvpvQikTlW8qnkeizMcS0PMo5uT7KRsWQSPdiNhnkzp8CWMUawjqT9a19PNni8Dgm8vuQRxGHZRt1I3UJeJlnCFpqcAJxi4neP4Gx7AjSsN3xMP5D73VFFo7oWgA9NPPdZ5h1BV-LVrw7G0phJDqE4ij-0FEV2_ySrUfUrOBPfabJeIr66p9kkM6-M.7vartfUsWEgTHmFatAWsMA"

model = whisper.load_model("base")
model.device

#device_encoding(type='cuda', index=0)

def transcribe(audio):
    # load audio and pad/trim
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs= model.detect_language(mel)
    
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    result_text = result.text
    
    chatgpt_api= ChatGPT(secret_tocken)
    resp = chatgpt_api.send_message(result_text)
    out_result = resp['message']
    
    return [result_text, out_result]

output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.Textbox(label="ChatGPT Output")

gr.Interface(
    title='OpenAI Whisper and ChatGPT Gradio Web UI',
    fn=transcribe,
    inputs=[
    gr.inputs.Audio(source="microphone", type="filepath")
    ],
    outputs=[output_1, output_2],
live=True).launch()


