# gradio_app.py
from transformers import AutoProcessor, SeamlessM4TModel
import gradio as gr
from IPython.display import Audio
from transformers.integrations import deepspeed

from TxS import text_to_speech
from TxT import text_to_text
from SxT import speech_to_text
from SxS import speech_to_speech
import os

# Define the output directory
OUTPUT_DIR = "temperory_storage"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_app(processor, model):
    with gr.Blocks() as app:
        gr.Markdown("# Seamless M4T implementation")
        
        with gr.Tabs():
            # Text-to-Text Tab
            with gr.Tab("Text-to-Text"):
                input_text = gr.Textbox(label="Input Text")
                input_lang = gr.Textbox(label="Input Language")
                output_lang = gr.Textbox(label="Output Language")
                text_output = gr.Textbox(label="Translated Text")
                translate_btn = gr.Button("Translate")
                
                def text_to_text_wrapper(input_text, input_lang, output_lang):
                    return text_to_text(processor, model, input_text, input_lang, output_lang)
                
                translate_btn.click(
                    text_to_text_wrapper,
                    inputs=[input_text, input_lang, output_lang],
                    outputs=text_output
                )
            
            # Text-to-Speech Tab
            with gr.Tab("Text-to-Speech"):
                input_text = gr.Textbox(label="Input Text")
                input_lang = gr.Textbox(label="Input Language")
                output_lang = gr.Textbox(label="Output Language")
                speech_output = gr.Audio(label="Speech Output", type="filepath")
                
                def text_to_speech_wrapper(input_text, input_lang, output_lang):
                    output_path = os.path.join(OUTPUT_DIR, "text_to_speech_output.wav")
                    text_to_speech(processor, model, input_text, input_lang, output_lang, output_path)
                    return output_path
                
                speak_btn = gr.Button("Convert to Speech")
                speak_btn.click(
                    text_to_speech_wrapper,
                    inputs=[input_text, input_lang, output_lang],
                    outputs=speech_output
                )
            
            # Speech-to-Text Tab
            with gr.Tab("Speech-to-Text"):
                audio_input = gr.Audio(label="Input Audio", type="filepath")
                output_lang = gr.Textbox(label="Output Language")
                text_output = gr.Textbox(label="Recognized Text")
                
                def speech_to_text_wrapper(audio_input, output_lang):
                    return speech_to_text(processor, model, audio_input, output_lang)
                
                recognize_btn = gr.Button("Recognize Speech")
                recognize_btn.click(
                    speech_to_text_wrapper,
                    inputs=[audio_input, output_lang],
                    outputs=text_output
                )
            
            # Speech-to-Speech Tab
            with gr.Tab("Speech-to-Speech"):
                audio_input = gr.Audio(label="Input Audio", type="filepath")
                output_lang = gr.Textbox(label="Output Language")
                speech_output = gr.Audio(label="Converted Speech", type="filepath")
                
                def speech_to_speech_wrapper(audio_input, output_lang):
                    output_path = os.path.join(OUTPUT_DIR, "speech_to_speech_output.wav")
                    speech_to_speech(processor, model, audio_input, output_lang, output_path)
                    return output_path
                
                convert_btn = gr.Button("Convert Speech")
                convert_btn.click(
                    speech_to_speech_wrapper,
                    inputs=[audio_input, output_lang],
                    outputs=speech_output
                )
                
    return app

# Run the Gradio app
if __name__ == "__main__":
    processor = AutoProcessor.from_pretrained(r"D:\PROJECT\facebook\hf-seamless-m4t-large")
    model = SeamlessM4TModel.from_pretrained(r"D:\PROJECT\facebook\hf-seamless-m4t-large")

    app = create_app(processor, model)
    app.launch(share=True)
