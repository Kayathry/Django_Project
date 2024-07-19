from django.shortcuts import render
from .models import School, Answers, Subjects, Summary, Student, AssesmentAreas, Awards, Class

# Create your views here.
def index(request):
    return render(request, 'index.html')

def school_model_view(request):
    data = School.objects.all()
    return render(request, 'school_view.html', {'data': data})


def answers_model_view(request):
    data = Answers.objects.all()
    return render(request, 'answers_view.html', {'data': data})


def subjects_model_view(request):
    data = Subjects.objects.all()
    return render(request, 'subjects_view.html', {'data': data})


def summary_model_view(request):
    data = Summary.objects.all()
    return render(request, 'summary_view.html', {'data': data})


def student_model_view(request):
    data = Student.objects.all()
    return render(request, 'student_view.html', {'data': data})


def assesmentareas_model_view(request):
    data = AssesmentAreas.objects.all()
    return render(request, 'assesmentareas_view.html', {'data': data})

def awards_model_view(request):
    data = Awards.objects.all()
    return render(request, 'awards_view.html', {'data': data})


def class_model_view(request):
    data = Class.objects.all()
    return render(request, 'class_view.html', {'data': data})
