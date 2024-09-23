from transformers import AutoProcessor, SeamlessM4TModel
from IPython.display import Audio

from TxS import text_to_speech
from TxT import text_to_text
from SxT import speech_to_text
from SxS import speech_to_speech



processor = AutoProcessor.from_pretrained(r"F:\facebook\hf-seamless-m4t-large")
model = SeamlessM4TModel.from_pretrained(r"F:\facebook\hf-seamless-m4t-large")

if __name__ == "__main__":
    # Example usage
    input_text = "Hello How are you . SeamlessM4TModel is transformers top level model to generate speech and text, but you can also use dedicated models that perform the task without additional components, thus reducing the memory footprint. For example, you can replace the audio-to-audio generation snippet with the model dedicated to the S2ST task, the rest is exactly the same code"
    input_audio_file_path="result.mp3"
    output_speech_path = "output.mp3"
    
    # Text to Text
    # output = text_to_text(processor, model, input_text, "eng", "hin")
    # print(output)
    
    # Text to Speech
    # text_to_speech(processor,model, input_text, "eng", "fra", output_speech_path)
    # print("Text to Speech output saved at:", output_speech_path)
    
    
    # Speech to Text
    # print(speech_to_text(processor, model, output_speech_path, "eng"))

    # Speech to Speech
    # speech_to_speech(processor, model, input_audio_file_path, "hin", output_speech_path)