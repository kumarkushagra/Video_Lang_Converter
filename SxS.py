from transformers import AutoProcessor, SeamlessM4TModel
import torchaudio
import scipy.io.wavfile
from IPython.display import Audio

def speech_to_speech(processor, model, input_audio_file_path, output_lang, output_path):
    audio_sample, sample_rate = torchaudio.load(input_audio_file_path)
    audio_sample_array = audio_sample[0].numpy()
    # Now, process it
    audio_inputs = processor(audios=audio_sample_array, sampling_rate=sample_rate, return_tensors="pt")

    audio_array_from_audio = model.generate(**audio_inputs, tgt_lang=output_lang)[0].cpu().numpy().squeeze()
    sample_rate = model.config.sampling_rate

    # Save the audio to a audio file
    scipy.io.wavfile.write( output_path, rate=sample_rate, data=audio_array_from_audio)
    # Play the audio
    Audio(audio_array_from_audio, rate=sample_rate)
    return output_path
