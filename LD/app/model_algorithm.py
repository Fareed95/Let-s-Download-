import yt_dlp
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def download_video(video_url, output_path):
    ydl_opts = {
        'format': 'bestvideo',
        'outtmpl': os.path.join(output_path, '%(title)s_video.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_audio(video_url, output_path):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(output_path, '%(title)s_audio.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def combine_audio_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video to the downloaded audio
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the result to the output file
    video_clip.write_videofile(output_path, codec='libx264')

def main(video_url, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    print("Downloading video...")
    download_video(video_url, output_dir)
    
    print("Downloading audio...")
    download_audio(video_url, output_dir)
    
    # Get the filename from the video download
    video_filename = [f for f in os.listdir(output_dir) if f.endswith('_video.mp4')][0]
    audio_filename = [f for f in os.listdir(output_dir) if f.endswith('_audio.mp3')][0]
    
    video_path = os.path.join(output_dir, video_filename)
    audio_path = os.path.join(output_dir, audio_filename)
    
    output_path = os.path.join(output_dir, 'combined_video.mp4')
    
    print("Combining audio and video...")
    combine_audio_video(video_path, audio_path, output_path)
    
    print(f"Video combined successfully. Saved to {output_path}")

if __name__ == "__main__":
    video_url = "https://youtu.be/FFbc-jXkADs?si=gTC8qjYBjZ6QjgIR"  # Replace with your video URL
    output_dir = "./downloads"  # Directory where files will be saved
    main(video_url, output_dir)