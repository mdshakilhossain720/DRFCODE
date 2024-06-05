from rest_framework import serializers
from.models import Students


class Studentseri(serializers.ModelSerializer):
     class Meta:
          model=Students
          fields=['id','name','rool','city']

# class StudentSerilzer(serializers.Serializer):
#      name=serializers.CharField(max_length=100)
#      rool=serializers.IntegerField()
#      city=serializers.CharField(max_length=100)

#      def create(self, validated_data):
#           return Students.objects.create(**validated_data)
     
#      def update(self, instance, validated_data):
#           instance.name=validated_data.get('name',instance.name)
#           instance.rool=validated_data.get('name',instance.rool)
#           instance.city=validated_data.get('name',instance.city)
#           instance.save()
#           return instance
     
#      def validate_rool(self,value):
#           if value>=200:
#                raise serializers.ValidationError('seat fail')
#           return value
          

# # object validation
      
#      def validate(self,data):
#           nm=data.get('name')
#           ct=data.get('city')
#           if nm.lower() == 'rohit' and ct.lower()!='ranchi':
#                raise serializers.ValidationError('city must be ranchi')
#           return data

     
    