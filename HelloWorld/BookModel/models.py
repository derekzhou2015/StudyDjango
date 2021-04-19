from django.db import models
from HelloWorld.Common import common
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')


class Publisher(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()

    def __str__(self):
        return '%s(%s)' % (self.name, self.detail.get_gender_display()[0:1])


class AuthorDetail(models.Model):
    gender = models.SmallIntegerField(
        choices=common.GENDER_LIST)
    tel = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    birthday = models.DateField()
    author = models.OneToOneField(
        "Author", related_name="detail", primary_key=True, unique=True, on_delete=models.CASCADE)
