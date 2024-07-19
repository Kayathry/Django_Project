from django.urls import path
from . import views

# School, Answers, Subjects, Summary, Student, AssesmentAreas, Awards, Class

urlpatterns = [
    path('school-data/', views.school_model_view, name='school_model_view'),
    path('answers-data/', views.answers_model_view, name='answers_model_view'),
    path('subjects-data/', views.subjects_model_view, name='subjects_model_view'),
    path('summary-data/', views.summary_model_view, name='summary_model_view'),
    path('student-data/', views.student_model_view, name='student_model_view'),
    path('assesment-data/', views.assesmentareas_model_view, name='assesmentareas_model_view'),
    path('awards-data/', views.awards_model_view, name='awards_model_view'),
    path('class-data/', views.class_model_view, name='class_model_view'),
]
