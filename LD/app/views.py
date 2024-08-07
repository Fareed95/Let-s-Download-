import yt_dlp

def download_video(link, format='mp4'):
    ydl_opts = {}

    if format == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'skip'  # Tell yt-dlp not to use ffmpeg
        }
    elif format == 'mp4':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'merge_output_format': 'mp4',
            'ffmpeg_location': 'skip'  # Tell yt-dlp not to use ffmpeg
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    link = input("Enter the YouTube link: ")
    format_choice = input("Enter the format (mp4/mp3): ").lower()
    download_video(link, format=format_choice)
