from transformers import AutoProcessor, SeamlessM4TModel
import scipy.io.wavfile
from IPython.display import Audio

def text_to_speech(processor, model, input_text, input_lang, output_lang, output_path):
    text_inputs = processor(text = input_text, src_lang=input_lang, return_tensors="pt")
    audio_array_from_text = model.generate(**text_inputs, tgt_lang=output_lang)[0].cpu().numpy().squeeze()
    
    # Define the sample rate from model config
    sample_rate = model.config.sampling_rate
    # Save the audio to a WAV file
    scipy.io.wavfile.write(output_path, rate=sample_rate, data=audio_array_from_text)
    # Play the audio
    Audio(audio_array_from_text, rate=sample_rate)
    return f"{output_path}/output1.mp3"