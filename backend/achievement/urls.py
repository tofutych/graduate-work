from django.urls import path, include

from achievement import views

urlpatterns = [
    path('faculties/', views.faculty_list),
    path('faculties/<slug:slug>/', views.faculty_detail),
    path('faculties/<slug:faculty_slug>/<slug:speciality_slug>/', views.speciality_detail),
    path('faculties/<slug:faculty_slug>/specialities/', views.speciality_list),
]
