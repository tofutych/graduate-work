from django.contrib import admin

from .models import Faculty, Speciality, YearOfAdmission, Student, Achievement


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = dict(slug=("name",))


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'name', 'code')
    prepopulated_fields = dict(slug=("code",))


@admin.register(YearOfAdmission)
class YearOfAdmissionAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'speciality', 'year')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'year_of_admission', 'name', 'patronymic', 'speciality')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'description', 'date', 'url', 'date_added')
