from idlelib.debugobj_r import remote_object_tree_item

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from tasks.forms import AddPostTask
from tasks.models import Task


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

