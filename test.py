import gradio as gr
import os
import shutil
from moviepy.editor import VideoFileClip

sequence_number = 0  # Global variable to keep track of the sequence number

# Function to process video, extract audio, split into chunks, and return video
def process_and_extract(video_path, lang_code):
    global sequence_number

    # Save video to a local directory
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Copy the uploaded video to the desired location
    target_video_path = os.path.join('uploads', f'uploaded_video_{sequence_number}.mp4')
    shutil.copy(video_path, target_video_path)
    
    # Extract audio from the video
    video_clip = VideoFileClip(target_video_path)
    audio = video_clip.audio

    # Directory to save audio chunks
    audio_dir = 'original_samples'
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    # Ensure the subdirectory exists (to avoid permission issues)
    temp_audio_dir = os.path.join(audio_dir, "temp")
    if not os.path.exists(temp_audio_dir):
        os.makedirs(temp_audio_dir)
    
    # Split audio into chunks of length 1 minute or less
    chunk_duration = 60  # 60 seconds or 1 minute
    audio_duration = audio.duration  # Total audio duration
    num_chunks = int(audio_duration // chunk_duration) + 1  # Number of chunks

    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, audio_duration)  # Ensure last chunk is shorter than 1 minute
        
        # Extract the chunk from the audio
        audio_chunk = audio.subclip(start_time, end_time)
        
        # Save the chunk with sequence number in "original_samples/temp"
        audio_chunk_path = os.path.join(temp_audio_dir, f'audio_chunk_{sequence_number}.mp3')
        audio_chunk.write_audiofile(audio_chunk_path)
        
        # Increment the sequence number for each chunk
        sequence_number += 1
    
        # # Now convert each video to another language
        # convert_audio_clips(lang_code)

    # Return the same video path for demonstration
    return target_video_path

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### Upload a Video, Select a Value, and Extract Audio in Chunks")
    
    # Inputs: Video and Dropdown
    video_input = gr.Video(label="Upload a video")
    dropdown_input = gr.Dropdown(["Hin"], label="Language")
    
    # Output: Video (returned to user after processing)
    video_output = gr.Video(label="Processed Video Output")

    # Button to process the inputs
    submit_button = gr.Button("Submit")
    
    # Set up the function to be triggered on button click
    submit_button.click(process_and_extract, inputs=[video_input, dropdown_input], outputs=video_output)

# Launch the Gradio app
demo.launch()
