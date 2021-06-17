from django.shortcuts import render,redirect

from .models import *
from .forms import *

# Create your views here.
def mainfunc(request):
    form=WorkForm()
    if request.method=='POST':
        form=WorkForm(request.POST)
        if form.is_valid():
            form.save()
    total_work=Work.objects.all()
    context={'total_work':total_work,'form':form}
    return render(request,'todo/main.html',context)

def deleteWork(request ,pk):
    work=Work.objects.get(id=pk)
    if request.method=='POST':
        work.delete()
        return redirect('/')
    context={'work':work}
    return render (request, 'todo/delete_work.html',context)



def updateWork(request ,pk):
    work=Work.objects.get(id=pk)
    form=WorkForm(instance=work)
    if request.method=='POST':
        form= WorkForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form,'work':work}
    return render(request,'todo/update_task.html',context)