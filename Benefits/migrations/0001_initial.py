# Generated by Django 4.1.5 on 2023-04-05 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=1000, null=True, verbose_name='Цена')),
                ('city', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Город')),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Льгота',
                'verbose_name_plural': 'Льготы',
            },
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='Benefits.benefit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Желание',
                'verbose_name_plural': 'Желания',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='Benefits.benefit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]
