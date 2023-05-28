from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Students_Form
from .models import Students_Data
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
def home(request):
    students = Students_Data.objects.all()
    return render(request, 'students/home.html', {
        'students': students
    })

def students_form(request, id=0):
    student_id = id
    if request.method == 'POST':
        if id == 0:
            form = Students_Form(request.POST)
        else:
            student = Students_Data.objects.get(id=id)
            form = Students_Form(request.POST, instance=student)

        if form.is_valid():
            form.save()
             
        return redirect('/')

    else:
        if id == 0:
            form = Students_Form()
        else:
            student = Students_Data.objects.get(id=id)
            form = Students_Form(instance=student)
        
        return render(request, 'students/students_form.html', {
            'form': form,
        })
    