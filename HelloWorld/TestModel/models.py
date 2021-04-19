from django.db import models
from HelloWorld.Common import common
# Create your models here.


class Account(models.Model):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    acc_details = models.OneToOneField(
        'AccountDetails', on_delete=models.CASCADE, unique=True)


class AccountDetails(models.Model):
    class Meta:
        verbose_name = 'Account Details'
        verbose_name_plural = 'Account Details'
    gender = models.SmallIntegerField(choices=common.GENDER_LIST)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
