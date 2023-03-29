# Generated by Django 4.1.5 on 2023-03-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('city', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Льгота',
                'verbose_name_plural': 'Льготы',
            },
        ),
    ]
