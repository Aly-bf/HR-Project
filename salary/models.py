from django.db import models
from personnel.models import personel


class Salary(models.Model):
    base_salary = models.IntegerField()
    gross = models.IntegerField()
    insurance = models.IntegerField()
    tax = models.IntegerField()
    personel = models.OneToOneField(personel, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.personel.name} - Salary Details"
    