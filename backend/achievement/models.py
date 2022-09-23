from django.db import models

from achievement.services.current_year import current_year
from achievement.services.year_choices import year_choices


class Faculty(models.Model):
    """"""
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        db_table = "faculty"

    def __str__(self):
        return self.name


class Speciality(models.Model):
    """"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        db_table = "speciality"

    def __str__(self):
        return self.code


class YearOfAdmission(models.Model):
    """"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    year = models.IntegerField(choices=year_choices(), default=current_year())

    class Meta:
        ordering = ('year',)
        db_table = "year_of_admission"

    def __str__(self):
        return str(self.year)


class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    year_of_admission = models.ForeignKey(YearOfAdmission, on_delete=models.CASCADE)

    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "student"
        ordering = ('id', )

    def __str__(self):
        return f"{self.id} {self.name}"


class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    url = models.URLField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)
    # image = models.ImageField()
    # grade = models.DecimalField()

    class Meta:
        db_table = "achievement"
        ordering = ('-date_added',)

    def __str__(self):
        return self.title
