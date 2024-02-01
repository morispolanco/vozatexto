import streamlit as st
import requests
import json

def transcribe_audio(audio_file):
    headers = {
        'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c',
    }

    files = {
        'audio': audio_file,
    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)
    return response.json()

def generate_autobiography(text):
    response = requests.post(
      "https://api.respell.ai/v1/run",
      headers={
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      data=json.dumps({
        "spellId": "dN5cL9gF7TOXGpQHIxkeb",
        "inputs": {
          "input": text,
        }
      }),
    )
    return response.json()

# Streamlit UI
st.title("Transcripción de Voz y Generación de Autobiografía")

# Subir archivo de audio
audio_file = st.file_uploader("Sube tu archivo de audio", type=['mp3', 'wav', 'm4a'])

if audio_file:
    st.audio(audio_file, format='audio/mp3')

    if st.button("Transcribir"):
        transcribed_text = transcribe_audio(audio_file)
        st.write("Texto Transcrito:")
        st.write(transcribed_text)

        if st.button("Generar Autobiografía"):
            autobiography = generate_autobiography(transcribed_text)
            st.write("Autobiografía Generada:")
            st.write(autobiography)
