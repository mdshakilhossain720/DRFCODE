from django.shortcuts import render
import io
from rest_framework .parsers import JSONParser
from .models import Students
from .serializers import StudentSerilzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def studetnapi(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser.parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Students.objects.get(id=id)
            serilazer=StudentSerilzer(stu)
            json_data=JSONRenderer().render(serilazer.data)
            return HttpResponse(json_data,content_type='application/json')
            
            stu=Students.objects.all()
            serilazer=StudentSerilzer(stu,many=True)
            json_data=JSONRenderer().render(serilazer.data)
            return HttpResponse(json_data,content_type='application/json')


        if request.method == 'POST':
           json_data=request.body
           stream=io.BytesIO(json_data)
           pythondata=JSONParser().parse(stream)
           serilazer=StudentSerilzer(data=pythondata)
           if serilazer.is_valid():
               serilazer.save()
               res={'msg':'data create'}
               json_data=JSONRenderer().render(res)
               return HttpResponse(json_data,content_type='application/json')
            
        json_data=JSONRenderer().render(serilazer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method == 'PUT':
        json_data=request.body
        strem=io.BytesIO(json_data)
        pythondata=JSONParser().parse(strem)
        id=pythondata.get('id')
        stu=Students.objects.get(id=id)
        serilazer=StudentSerilzer(stu,data=pythondata,partial=True)
        if serilazer.is_valid():
            serilazer.save()
            res={'msg':'Data update'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serilazer.errors)
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method == 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Students.objects.get(id=id)
        stu.delete()
        res={'msg':'Data deleted'}
        json_data=JSONParser().parse(res)
        return HttpResponse(json_data,content_type='application/json')
        

        

           
           






