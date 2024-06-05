from rest_framework import serializers
from.models import Stduent

class StudentSerializers(serializers.Serializer):
     name=serializers.CharField(max_length=100)
     roll=serializers.IntegerField()
     city=serializers.CharField(max_length=100)

def create(self,validate_data):
     return Stduent.objects.create(**validate_data)