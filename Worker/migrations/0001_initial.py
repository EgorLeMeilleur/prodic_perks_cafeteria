# Generated by Django 4.1.7 on 2023-03-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('surname', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('position', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('experience', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10000, null=True)),
            ],
        ),
    ]
