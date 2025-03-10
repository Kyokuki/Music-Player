from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from playerWeb.models import Music, RelUserMusic,User
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1
import os


@csrf_exempt
def upload_music(request):
    if request.method == 'POST':
        file = request.FILES['file']
        userid = request.POST.get('userid')
        file_path = os.path.join('playerWeb', 'media', 'audio', file.name)
        if not os.path.exists(os.path.join('playerWeb', 'media', 'audio')):
            os.makedirs(os.path.join('playerWeb', 'media', 'audio'))
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        audio = MP3(file_path, ID3=ID3)

        # 获取歌名和歌手信息
        title = audio.get("TIT2", None)
        artist = audio.get("TPE1", None)

        new_music = Music.objects.create(artist=artist.text[0],
                                         name=title.text[0],
                                         url="http://localhost:8000/media/audio/"+file.name)
        RelUserMusic.objects.create(userid=userid,
                                    musicid=new_music.id)
        return HttpResponse(status=200)
    return HttpResponse(status=405)  # Method Not Allowed


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        file = request.FILES['file']
        userid = request.POST.get('userid')
        file_path = os.path.join('playerWeb','media','image', file.name)
        if not os.path.exists(os.path.join('playerWeb','media','image')):
            os.makedirs(os.path.join('playerWeb','media','image'))
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        User.objects.filter(id=userid).update(photo="http://localhost:8000/media/image/"+file.name)
        return HttpResponse({"http://localhost:8000/media/image/"+file.name},status=200)
    return HttpResponse(status=405)  # Method Not Allowed
