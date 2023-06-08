from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Students_Form, Students_Edit_Form
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
    if request.method == 'POST':
        if id == 0:
            form = Students_Form(request.POST) #submit when add
        else:
            student = Students_Data.objects.get(id=id)
            form = Students_Edit_Form(request.POST, instance=student) # submit when edit

        if form.is_valid():
            form.save()
             
        return redirect('/')

    else:
        if id == 0:
            form = Students_Form() # add form
        else:
            student = Students_Data.objects.get(id=id) # Edit Form
            form = Students_Edit_Form(instance=student)
        
        return render(request, 'students/students_form.html', {
            'form': form,
        })

def student_delete(request, id):
    student = Students_Data.objects.get(id=id)
    student.delete()

    return redirect('/')
