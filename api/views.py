from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def student_details(request,pk):
    # complext data type
    stu=StudentModel.objects.get(id=pk)
    # python native data type
    serializers=StudentSerializers(stu)
    # native to json 
    json_data=JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type='application/json')

def allstudent(request):
    stu=StudentModel.objects.all()
    seralizers=StudentSerializers(stu,many=True)
    json_data=JSONRenderer().render(seralizers.data)
    return HttpResponse(json_data,content_type='application/json')




