from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class Abst(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            last_object = self.__class__.objects.order_by('-id').first()
            if last_object:
                self.id = last_object.id + 1
            else:
                self.id = 100000
        super(Abst, self).save(*args, **kwargs)



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

    def __str__(self):
        return f'{self.name} / {self.employment_data}'