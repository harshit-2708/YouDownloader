from django.shortcuts import render
from pytube import YouTube

def homepage(request):
    message = 'Welcome to our Youtube Video Downloader!'
    return render(request, 'downloader.html', {'message': message})
def download(request, *args, **kwargs):
    link = request.GET.get("link")
    url = YouTube(str(link))
    video = url.streams.first()
    video.download()
    return render(request, 'downloader.html',{'message1':'video is downloading','message':'Welcome to our Youtube Video Downloader!'})
