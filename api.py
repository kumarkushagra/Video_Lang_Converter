from fastapi import FastAPI, UploadFile, File, Form
from transformers import AutoProcessor, SeamlessM4TModel
import torchaudio
import uvicorn
import os

from SxT import speech_to_text
from mp3_to_wav import convert_mp3_to_wav

# Initialize FastAPI app
app = FastAPI()

# Load the model and processor (adjust paths as needed)
processor = AutoProcessor.from_pretrained(r"D:\PROJECT\facebook\hf-seamless-m4t-large")
model = SeamlessM4TModel.from_pretrained(r"D:\PROJECT\facebook\hf-seamless-m4t-large")

# Create temp directory if it doesn't exist
if not os.path.exists('temp'):
    os.makedirs('temp')

@app.post("/translate-audio/")
async def translate_audio(file: UploadFile = File(...), target_language: str = Form(...)):
    print(f"Received file: {file.filename}, Target language: {target_language}")

    # Define the path to save the uploaded file
    file_path = f'temp/{file.filename}'
    
    # Save the uploaded file to the temp directory
    with open(file_path, 'wb') as temp_file:
        temp_file.write(await file.read())

    # Convert MP3 to WAV if the file is MP3
    if file.filename.endswith('.mp3'):
        wav_file_path = file_path.rsplit('.', 1)[0] + '.wav'
        convert_mp3_to_wav(file_path)  # Convert to WAV
        file_path = wav_file_path  # Update the file_path to the new WAV file

    # Call the speech-to-text function
    translated_text_from_audio = speech_to_text(processor, model, file_path, target_language)

    # Remove the file after processing to clean up the temp directory
    os.remove(file_path)

    return {"translated_text": translated_text_from_audio}

if __name__ == "__main__":
    uvicorn.run("api:app")
