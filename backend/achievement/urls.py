from django.urls import path, include

from achievement import views

urlpatterns = [
    path('faculties/', views.faculty_list),
    path('<slug:slug>/', views.faculty_detail),
    path('<slug:faculty_slug>/specialities/', views.speciality_list),
    path('<slug:faculty_slug>/specialities/<slug:speciality_slug>/', views.speciality_detail),
    path('<slug:faculty_slug>/specialities/<slug:speciality_slug>/year_of_admission/', views.year_of_admission_list),
    path('<slug:faculty_slug>/specialities/<slug:speciality_slug>/year_of_admission/<slug:year_of_admission_slug>',
         views.year_of_admission_detail),
]
