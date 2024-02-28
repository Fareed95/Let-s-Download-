from django.shortcuts import render, redirect
from django.http import HttpResponse,FileResponse, JsonResponse
import yt_dlp
from pytube import YouTube
import os 


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def function1(request):
    text = request.POST.get('text', '')
    audio = request.POST.get('audio', 'off')
    video = request.POST.get('video', '')

    if (audio!="None"):

        # Specify the directory where you want to save the audio
        output_directory = "/My downloaded audios"

        # Set the options for yt_dlp to download only the audio in MP3 format
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_directory}/%(title)s.%(ext)s'
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
            ydl.download([text]) 

        return HttpResponse("audio is doownloaded succesfully")


    if video:
        return HttpResponse("Video download functionality will be added soon")


