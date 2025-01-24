from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonelSerializers
from .models import personel


class PersonelApiViewSets(viewsets.ModelViewSet):
    queryset = personel.objects.all()
    serializer_class = PersonelSerializers