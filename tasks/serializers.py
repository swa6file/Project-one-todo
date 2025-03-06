import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
     person = serializers.HiddenField(default=serializers.CurrentUserDefault())

     class Meta:
          model = Task
          fields = "__all__"





# def encode():
#     model = TaskModel(title="Приготовить завтрак",description="1.Яичница или омлет\n2.Банан\n3.Вода")
#     model_sr = TaskSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json.decode("utf-8"))
#
# def decode():
#     string = '{"title":"Работаем братья","description":"Нужно усерднее работать"}'
#     stream = io.BytesIO(string.encode('utf-8'))
#     data = JSONParser().parse(stream)
#     serializers = TaskSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)

#title = serializers.CharField(max_length=50)
# description = serializers.CharField()
# completed = serializers.BooleanField(default=False)
#
# def create(self,validated_data):
#      return Task.objects.create(**validated_data)
#
# def update(self, instance, validated_data):
#      instance.title = validated_data.get("title", instance.title)
#      instance.description = validated_data.get("description", instance.description)
#      instance.completed = validated_data.get("completed",instance.completed)
#      instance.save()
#      return instance
#
# def delete(self, instance):
#      instance.delete()
#      return instance