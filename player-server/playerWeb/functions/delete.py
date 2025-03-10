from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from playerWeb.models import Music, RelUserMusic
import json
import os


@csrf_exempt
def delete_music(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userid = data.get('userid')
        musicid = data.get('musicid')
        filename = Music.objects.filter(id=musicid).first().url.split('/')[-1]
        RelUserMusic.objects.filter(userid=userid, musicid=musicid).delete()
        Music.objects.filter(id=musicid).delete()
        filepath = os.path.join('playerWeb', 'media', 'audio', filename)
        os.remove(filepath)
        return HttpResponse(status=200)
    return HttpResponse(status=405)  # Method Not Allowed
