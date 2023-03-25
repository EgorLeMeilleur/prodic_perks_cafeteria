from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Worker(models.Model):
    username = models.CharField(max_length=255, unique=True, blank=True, null=True, default=None)
    surname = models.CharField(max_length=255, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    password = models.CharField(max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)
    position = models.CharField(max_length=255, blank=True, null=True, default=None)
    experience = models.CharField(max_length=255, blank=True, null=True, default=None)
    balance = models.DecimalField(max_digits=10000, decimal_places=2, blank=True, null=True, default=None)

    def __str__(self):
        return self.surname + " " + self.first_name


class Benefit(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True, default=None)
    city = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Сотрудник'
    verbose_name_plural = 'Сотрудники'
