from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SalarySerializers
from .models import Salary

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializers