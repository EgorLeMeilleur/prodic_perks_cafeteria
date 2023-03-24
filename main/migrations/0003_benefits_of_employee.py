# Generated by Django 4.1.7 on 2023-03-24 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='benefits_of_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_or_wished', models.IntegerField()),
                ('id_benefit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.benefit')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.employee')),
            ],
        ),
    ]
