from django.http import HttpResponse
from django.shortcuts import render, redirect

from support.forms import SupportUserForm
from support.models import Support


def tasks(request):
    complaint = Support.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        form = SupportUserForm(request.POST)
        if form.is_valid() == True:
            try:
                Support.objects.create(**form.cleaned_data,user_id=request.user.id)
                return redirect('support')
            except:
                form.add_error(None,"Ошибка добавления задачи")
    else:
        form = SupportUserForm()

    return render(request,'support/support.html',context={'complaint':complaint,'form':form})

