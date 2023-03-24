from django.db import models


class Benefit(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    city = models.CharField(max_length=20)
    id = models.CharField(max_length=1).primary_key


class Employee(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    experience = models.IntegerField()
    balance = models.IntegerField()
    city = models.IntegerField()


class benefits_of_employee(models.Model):
    bought_or_wished = models.IntegerField()
    id_employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    id_benefit = models.ForeignKey(Benefit, on_delete=models.DO_NOTHING)