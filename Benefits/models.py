from django.contrib.auth.models import User
from django.db import models

from Worker.models import Profile


# Create your models here.


class Benefit(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(verbose_name="Цена", max_digits=1000, decimal_places=2, blank=True, null=True, default=None)
    city = models.CharField(verbose_name="Город", max_length=255, blank=True, null=True, default=None)
    description = models.CharField(verbose_name="Описание", max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='purchases')
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} bought {self.benefit.name} on {self.date}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class Wish(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wishes')
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, related_name='wishes')

    def __str__(self):
        return f'{self.user.username} wishes {self.benefit.name}'

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'
