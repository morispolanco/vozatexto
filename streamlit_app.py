import streamlit as st
import requests

def main():
    st.title("Voice Transcription with API")

    # File uploader
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        # Transcribe audio
        transcription = transcribe_audio(uploaded_file)
        st.write("Transcription:")
        st.write(transcription)

def transcribe_audio(uploaded_file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    headers = {
        "Authorization": "Bearer 0ee2bb2a-c71d-426a-b96f-3c536d19d900"
    }

    files = {
        "media": uploaded_file
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        job_id = response.json()["id"]
        transcription = get_transcription(job_id)
        return transcription
    else:
        st.error("Error transcribing audio. Please try again.")
        return None

def get_transcription(job_id):
    url = f"https://api.rev.ai/revspeech/v1beta/jobs/{job_id}/transcript"
    headers = {
        "Authorization": "Bearer 0ee2bb2a-c71d-426a-b96f-3c536d19d900"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        transcript_json = response.json()
        transcript_text = ""
        for i in range(len(transcript_json["monologues"])):
            for j in range(len(transcript_json["monologues"][i]["elements"])):
                transcript_text += transcript_json["monologues"][i]["elements"][j]["value"]
                if transcript_json["monologues"][i]["elements"][j]["type"] == "punct":
                    transcript_text += " "
        return transcript_text
    else:
        st.error("Error getting transcription. Please try again.")
        return None

if __name__ == "__main__":
    main()
