import os
from moviepy.editor import VideoFileClip

# Function to extract audio from video and save it in "uploads"
def extract_audio(video_path):
    # Ensure the 'uploads' directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Extract the audio and save it
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio
    
    # Save the audio to the 'uploads' directory as an MP3 file
    audio_path = os.path.join('uploads', 'extracted_audio.mp3')
    audio.write_audiofile(audio_path)
    
    return audio_path

# Function to split the audio into chunks and save in "audio_chunks"
from moviepy.editor import AudioFileClip

# Function to split the audio into chunks and save in "audio_chunks"
def split_audio(audio_path):
    # Ensure the 'audio_chunks' directory exists
    audio_dir = 'audio_chunks'
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    # Load the audio file using AudioFileClip (not VideoFileClip)
    audio_clip = AudioFileClip(audio_path)
    
    # Split audio into chunks of 1 minute (60 seconds)
    chunk_duration = 60  # seconds
    audio_duration = audio_clip.duration
    num_chunks = int(audio_duration // chunk_duration) + 1
    
    # Create each chunk
    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, audio_duration)  # Last chunk can be shorter
        
        # Extract the chunk from the audio
        audio_chunk = audio_clip.subclip(start_time, end_time)
        
        # Save the chunk
        chunk_path = os.path.join(audio_dir, f'audio_chunk_{i+1}.mp3')
        audio_chunk.write_audiofile(chunk_path)

    return f"Audio split into {num_chunks} chunks and saved in 'audio_chunks/'"

# Ensure this function is called correctly in the main script
# extracted_audio_path should be passed to split_audio function


    # Example usage (Later, we can call these from the Gradio app):
if __name__ == "__main__":
    video_path = r"D:\PROJECT\Video_Lang_Converter\uploads\uploaded_video_0.mp4"
    extracted_audio_path = extract_audio(video_path)
    split_audio(extracted_audio_path)
