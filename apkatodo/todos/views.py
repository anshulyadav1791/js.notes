from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

def task_list(request):
    task = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'task': task})

def task_create(request):
    if request.mothod == 'POST':
        tittle = request.POST.get('title', '').strip()
        discription = request.POST.get('description','').strip()
        if tittle:
            Task.objects.create(tittle=tittle, description=discription)
            return redirect(reverse('todo:task_list'))
        error = "Title connot be empty."        
        return render(request,'todo/task_form.html',{'error': error})
    return render(request, 'todo/task_form.html')

task_update(requst, pk):
task = get_object_or_404(Task, pk=pk)
if request.model == 'POST':
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    