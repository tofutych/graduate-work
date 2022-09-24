from rest_framework import serializers

from .models import Faculty, Speciality, YearOfAdmission, Student, Achievement


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class YearOfAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearOfAdmission
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = (
            'faculty',
            'speciality',
            'year_of_admission',
            'surname',
            'name',
            'patronymic',
            'date_of_birth',
            'phone_number',
            'email',
            'get_absolute_url',
            'achievements')
