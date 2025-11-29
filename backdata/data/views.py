from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def data_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = StudentForm()

    return render(request, 'data/data_form.html', {'form': form})


def data_list(request):
    students = Student.objects.all()
    return render(request, 'data/data_list.html', {'students': students})


def data_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'data/data_detail.html', {'student': student})

def data_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render("data_list.html")
        else:
            form = StudentForm(instance=Student)
        return render(request, 'data_form.html', {'form': form})
    
    def data_delete(request, pk):
        student = get_object_or_404(student, pk=pk)
        if request.method == 'POST':
            student.delete()
            return redirect("data_list")
        return render(request, 'student_confirm_delete.html', {'student': student})