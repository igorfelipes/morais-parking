# Generated by Django 2.2 on 2020-06-02 19:48

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Funcionario Estacionamento'), (2, 'Rh'), (3, 'Gerente')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O username só pode conter letras, números ou as caracteres @/./+/-/_', 'invalid')], verbose_name='Username'),
        ),
    ]
