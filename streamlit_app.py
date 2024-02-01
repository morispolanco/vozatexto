import streamlit as st
import requests

st.title("Transcripción de Voz a Texto")

# Archivo de audio a transcribir
audio_file = st.file_uploader("Cargar archivo de audio", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')

    # Botón para iniciar la transcripción
    if st.button("Transcribir"):
        # Configuración de la solicitud
        headers = {
            'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c',
        }

        files = {
            'audio': audio_file.getvalue()
        }

        # Realizar la solicitud POST a la API
        response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)

        # Verificar el estado de la respuesta
        if response.status_code == 200:
            transcripcion = response.json().get("text")
            st.write("Transcripción:")
            st.write(transcripcion)
        else:
            st.write("Error al procesar la transcripción. Inténtalo de nuevo.")
