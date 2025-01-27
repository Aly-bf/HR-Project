from django.db import models
from personnel.models import personel


class Salary(models.Model):
    base_salary = models.IntegerField()
    gross = models.IntegerField()
    insurance = models.IntegerField()
    tax = models.IntegerField()
    personel = models.ForeignKey(personel, on_delete=models.CASCADE, related_name='salaries')

    @property
    def net_salary(self):
        return self.base_salary - self.insurance - self.tax - self.gross


    def __str__(self):
        return f"{self.personel.name} the net salary : {self.net_salary}"
    