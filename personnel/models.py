from django.db import models
from django.contrib.auth.models import User

class Abst(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class personel(Abst):

    BACHELOR = 'bachelor'
    MASTER = 'master'
    PHD = 'phd'

    DEGREE_CHOICES = [
        (BACHELOR, 'Bachelor'),
        (MASTER, 'Master'),
        (PHD, 'Phd'),
    ]
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    fathername = models.CharField(max_length=50)
    milirary_status = models.BooleanField(default=False)
    martial_status = models.BooleanField(default=False)
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=50)
    employment_data = models.CharField(max_length=100)
