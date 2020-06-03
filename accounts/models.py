import re

from djongo import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class User (AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'Funcionario Estacionamento'),
        (2, 'Rh'),
        (3, 'Gerente'),
    )

    username = models.CharField('Nome do Usuario', max_length=30, unique=True,
            validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O username só pode conter letras, números ou as caracteres @/./+/-/_', 'invalid')]
            )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=50)
    user_type = models.PositiveSmallIntegerField('Função',choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField('Está ativo?', default=True, blank=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    is_staff = models.BooleanField('É superUsuário', blank=True, default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'