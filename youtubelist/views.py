from django.shortcuts import render
from .models import Video

def home(request):
    videos = Video.objects.all()
    return render(request, 'listagem.html', {'videos': videos})