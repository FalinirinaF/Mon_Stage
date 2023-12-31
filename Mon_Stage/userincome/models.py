from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class UserIncome(models.Model):
    amount = models.FloatField()  # DECIMAL
    im = models.IntegerField(default=0)
    nom = models.TextField(default="")
    date = models.DateField(default=now)
    description = models.TextField()
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    source = models.CharField(max_length=266)

    def __str__(self):
        return self.source

    class Meta:
        ordering: ['-date']


class Source(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Source'

    def __str__(self):
        return self.name
