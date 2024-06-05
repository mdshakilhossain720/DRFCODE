from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studentcreate(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser.parse(stream)
        serilazers=StudentSerializers(data=pythondata)
        if serilazers.is_valid():
            serilazers.save()
            res={'msg':'Data create'}
            json_data=JSONRenderer.render(res)
            return HttpResponse(json_data,contetn_type='application/json')
        json_data=JSONRenderer().render(serilazers.errors)
        return HttpResponse(json_data,content_type='application/json')


