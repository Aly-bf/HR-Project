from rest_framework import serializers
from .models import Salary
from personnel.models import personel

class SalarySerializers(serializers.ModelSerializer):
    net_salary = serializers.ReadOnlyField()

    personel = serializers.PrimaryKeyRelatedField(queryset=personel.objects.all(), write_only=True)
    class Meta:
        model = Salary
        fields = ['base_salary', 'gross', 'insurance', 'tax', 'personel', 'net_salary']

   