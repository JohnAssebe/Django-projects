from django.shortcuts import render,redirect
from .models import Tasks
from .forms import TasksForm
# Create your views here.
def index(request):
    tasks=Tasks.objects.all()
    forms=TasksForm()
    if request.method=='POST':
        forms=TasksForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')

    context={'tasks':tasks,'forms':forms}
    return render(request,'tasks/list.html',context)
def update_task(request,pk):
    task=Tasks.objects.get(id=pk)
    form=TasksForm(instance=task)
    context={'form':form}
    if request.method=='POST':
        form=TasksForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'tasks/update_task.html',context)
def delete_task(request,pk):
    task=Tasks.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    context={'task':task}
    return render(request,'tasks/delete.html',context)