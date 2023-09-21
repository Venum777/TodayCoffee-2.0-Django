"""MODELS AUTHS"""
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group, Permission


class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        first_name,
        last_name,
        email: str,
        password: str,
        password2: str
    ) -> 'MyUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'MyUser' = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            password2=password2
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user


class MyUser(AbstractBaseUser, PermissionsMixin):

    fisrt_name = models.CharField(
        verbose_name='имя',
        max_length=50,
    )

    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=50
    )

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
        max_length=200
    )

    password = models.CharField(
        verbose_name='пароль',
        max_length=200
    )

    password2 = models.CharField(
        verbose_name='повторить',
        max_length=200
    )

    groups = models.ManyToManyField(Group, related_name='myuser_set'),
    user_permissions = models.ManyToManyField(Permission, related_name='myuser_set'),
    
    objects = MyUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'