from idlelib.debugobj_r import remote_object_tree_item
from typing import ReadOnly

from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
#DRF
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from tasks.forms import AddPostTask
from .models import Task
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TaskSerializer
#end drf

# Часть 1 Туду листа самого сайта не трогать
def index(request): #HTTP Request
    # main = render_to_string("index.html")
    # return HttpResponse(main)
    return render(request, 'tasks/index.html')

def tasks(request):
    posts = Task.objects.filter(person_id=request.user.id)

    if request.method == 'POST':
        form = AddPostTask(request.POST)
        if form.is_valid() == True:
            try:
                Task.objects.create(**form.cleaned_data,person_id=request.user.id)
                return redirect('taski')
            except:
                form.add_error(None,"Ошибка добавления задачи")
    else:
        form = AddPostTask()

    return render(request,'tasks/tasks.html',context={'posts':posts,'form':form})

def delete_task(request,name):
    task = Task.objects.get(title=name)
    task.delete()
    return redirect('taski')

def update(request,name):
    task = Task.objects.get(title=name)
    task.completed = 1
    task.save()
    return redirect('taski')

def cancel_update(request,name):
    task = Task.objects.get(title=name)
    task.completed = 0
    task.save()
    return redirect('taski')
#2 Часть DRF

class WomenAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = WomenAPIListPagination

class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]
    # authentication_classes = (TokenAuthentication,)

class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

# class TaskAPIList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class TaskAPIUpdate(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class TaskAPIDetailView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class TaskAPIView(APIView):
#     def get(self, request):
#         lst = Task.objects.all()
#         return Response({'tasks':TaskSerializer(lst, many=True).data})
#
#     def post(self,request ):
#         serializer = TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#
#         return Response({'post': serializer.data})
#
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error":"Method put not allowed"})
#
#         try:
#             instance = Task.objects.get(pk=pk)
#         except:
#             return Response({"error":"Object does not exists"})
#
#         serializer =  TaskSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})


    # def delete(self,request,*args,**kwargs):
    #     pk = kwargs.get("pk",None)
    #     if not pk:
    #         return Response({"error":"Method delete not allowed"})
    #
    #     try:
    #         instance = Task.object.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exist in the current environmnet"})
    #
    #     serializer = TaskSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.delete
    #
    #     return Response({"post":"delete post "+str(pk)})
# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#



# class TaskAPIViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Task.objects.all()[3:]
#         return Task.objects.filter(pk=pk)
#
#     @action(methods=['get'],detail=False)
#     def users(self,request):
#         users = User.objects.all()
#         return Response({'users': [u.username for u in users]})
#
