from transformers import *

# Function for text to text translation
def text_to_text(processor, model, input_text, input_lang, output_lang):
    # now, process some English test as well
    text_inputs = processor(text =input_text, src_lang=input_lang, return_tensors="pt")

    output_tokens = model.generate(**text_inputs, tgt_lang=output_lang, generate_speech=False)
    translated_text_from_text = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

    return translated_text_from_text