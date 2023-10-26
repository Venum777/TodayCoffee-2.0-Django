"""MODELS AUTHS"""
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


def user_directory_path(instance, filename):
    return f'image/user/user_{instance.id}/{filename}'


class MyUserManager(BaseUserManager):

    def create_user(
            self, 
            email, 
            password=None, 
            **extra_fields
        ):
        if not email:
            raise ValidationError('Email required')
        
        email = self.normalize_email(email)
        custom_user = self.model(email=email, **extra_fields)
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
            self, 
            email, 
            password=None, 
            **extra_fields
        ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class MyUser(
    AbstractBaseUser, 
    PermissionsMixin,
):

    first_name = models.CharField(
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

    phone_number = models.CharField(
        verbose_name='номер телефона',
        max_length=10
    )

    profile_picture = models.ImageField(
        verbose_name='изображение',
        upload_to=user_directory_path,
        default='image/user/user.png'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    @property
    def file_type(self):
        LAST: int = -1
        return self.profile_picture.url.split('.')[LAST]
