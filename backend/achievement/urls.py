from django.urls import path, include

from achievement import views

urlpatterns = [
    path('faculties/', views.FacultyList.as_view()),
]
