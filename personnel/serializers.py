from rest_framework import serializers
from .models import personel
from django.contrib.auth.models import User


class PersonelSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    

    class Meta:
        model = personel
        fields = '__all__'

    