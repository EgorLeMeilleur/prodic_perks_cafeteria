from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Worker(models.Model):
    username = models.CharField(verbose_name="Логин", max_length=255, unique=True, blank=True, null=True, default=None)
    surname = models.CharField(verbose_name="Фамилия", max_length=255, blank=True, null=True, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True, default=None)
    password = models.CharField(verbose_name="Пароль", max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True, default=None)
    position = models.CharField(verbose_name="Должность", max_length=255, blank=True, null=True, default=None)
    experience = models.CharField(verbose_name="Опыт работы", max_length=255, blank=True, null=True, default=None)
    balance = models.DecimalField(verbose_name="Баланс", max_digits=10000, decimal_places=2, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Cотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.surname + " " + self.first_name


class Benefit(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(verbose_name="Цена", max_digits=1000, decimal_places=2, blank=True, null=True, default=None)
    city = models.CharField(verbose_name="Город", max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'

    def __str__(self):
        return self.name
