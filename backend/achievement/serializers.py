from rest_framework import serializers

from .models import Faculty, Speciality, YearOfAdmission, Student, Achievement


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url"
        )


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = (
            "id",
            "faculty",
            "name",
            "code",
            "slug",
            "get_absolute_url"
        )
