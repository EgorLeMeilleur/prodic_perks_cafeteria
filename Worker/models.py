from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    username = models.OneToOneField(User, related_name="profile", verbose_name="Логин", unique=True, blank=True, null=True, default=None, on_delete=models.CASCADE)
    surname = models.CharField(verbose_name="Фамилия", max_length=255, blank=True, null=True, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True, default=None)
    position = models.CharField(verbose_name="Должность", max_length=255, blank=True, null=True, default=None)
    experience = models.CharField(verbose_name="Опыт работы", max_length=255, blank=True, null=True, default=None)
    balance = models.DecimalField(verbose_name="Баланс", max_digits=10000, decimal_places=2, blank=True, null=True, default=None)
    city = models.CharField(verbose_name="Город", max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Cотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

