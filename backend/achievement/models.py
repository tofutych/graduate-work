from django.db import models

from achievement.services.current_year import current_year
from achievement.services.year_choices import year_choices


class Faculty(models.Model):
    """
    Класс, описывающий таблицу faculty в БД.

    Атрибуты:
        name: Название факультета
        slug: slug факультета
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        db_table = "faculty"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Speciality(models.Model):
    """
    Класс, описывающий таблицу speciality в БД.

    Атрибуты:
        faculty: Foreign key (Faculty)

        name: Название специальности
        code: Код специальности
        slug: slug специальности
    """
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    slug = models.SlugField()

    class Meta:
        ordering = ('faculty',)
        db_table = "speciality"

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return f"{self.faculty.get_absolute_url()}{self.slug}/"


class YearOfAdmission(models.Model):
    """
    Класс, описывающий таблицу year_of_admission в БД.

    Атрибуты:
        faculty: Foreign key (Faculty)
        speciality: Foreign key (Speciality)

        year: Дата поступления
        slug: slug даты поступления
    """
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    year = models.IntegerField(choices=year_choices(), default=current_year())
    slug = models.SlugField()

    class Meta:
        ordering = ('year',)
        db_table = "year_of_admission"

    def __str__(self):
        return str(self.year)

    def get_absolute_url(self):
        return f"{self.speciality.get_absolute_url()}{self.slug}/"


class Student(models.Model):
    """
    Класс, описывающий таблицу student в БД.

    Атрибуты:
        faculty: Foreign key (Faculty)
        speciality: Foreign key (Speciality)
        year_of_admission: Foreign key (YearOfAdmission)

        surname: Фамилия
        name: Имя
        patronymic: Отчество
        date_of_birth: Дата рождения
        phone_number: Номер телефона
        email: Адрес электронной почты
    """
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
        ordering = ('id',)

    def __str__(self):
        return f"{self.id} {self.name}"

    def get_absolute_url(self):
        return f"{self.year_of_admission.get_absolute_url()}{self.id}/"


class Achievement(models.Model):
    """
    Класс, описывающий таблицу achievement в БД.

    Атрибуты:
        student: Foreign key (Student)

        title: Заголовок достижения
        description: Описание достижения
        date: Дата произошедшего события
        url: Ссылка
        date_added: Дата добавления записи

    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements')

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

    def get_absolute_url(self):
        return f"{self.student.get_absolute_url()}/achievement/{self.id}/"
