# Generated by Django 4.1.7 on 2023-03-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
    ]
