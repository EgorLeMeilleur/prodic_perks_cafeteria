from django.db import models

# Create your models here.


class Benefit(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(verbose_name="Цена", max_digits=1000, decimal_places=2, blank=True, null=True, default=None)
    city = models.CharField(verbose_name="Город", max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'

    def __str__(self):
        return self.name