from transformers import AutoProcessor, SeamlessM4TModel
import torchaudio

def speech_to_text(processor, model, input_audio_file_path, output_lang):

    # Load the audio file
    audio_sample, sample_rate = torchaudio.load(input_audio_file_path)
    audio_sample_array = audio_sample[0].numpy()

    # Process the audio, specifying the sampling rate
    audio_inputs = processor(audios=audio_sample_array, sampling_rate=sample_rate, return_tensors="pt")

    # Generate output tokens
    output_tokens = model.generate(**audio_inputs, tgt_lang=output_lang, generate_speech=False)
    translated_text_from_audio = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

    return translated_text_from_audio
