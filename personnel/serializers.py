from rest_framework import serializers
from .models import personel
from django.contrib.auth.models import User
from salary.serializers import SalarySerializers


class PersonelSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    salaries = SalarySerializers(many=True, read_only=True)
    

    class Meta:
        model = personel
        fields = ['id' ,'name', 'birthdate', 'fathername', 'milirary_status', 'martial_status', 'degree', 'employment_data', 'salaries', 'user']

    