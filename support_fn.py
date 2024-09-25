import os
from transformers import AutoProcessor, SeamlessM4TModel
import torchaudio
import scipy.io.wavfile
from IPython.display import Audio

def translate_audio_files(lang_code):
    input_directory = 'path/to/input/directory'
    output_directory = 'path/to/output/directory'
    
    # Step 1: List and sort audio files
    audio_files = [f for f in os.listdir(input_directory) if f.startswith('audio_chunk_') and f.endswith('.mp3')]
    audio_files.sort(key=lambda x: int(x.split('_')[2].split('.')[0]))  # Extract sequence number
    
    # Step 2: Process each audio file
    for audio_file in audio_files:
        input_audio_file_path = os.path.join(input_directory, audio_file)
        output_path = os.path.join(output_directory, audio_file.replace('.mp3', '.wav'))  # Save as .wav
        
        # Step 3: Translate and save audio
        speech_to_speech(processor, model, input_audio_file_path, lang_code, output_path)

# Example usage in this script
# translate_audio_files('fr')  # Translate to French
