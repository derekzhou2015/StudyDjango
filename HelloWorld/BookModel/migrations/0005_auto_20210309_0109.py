# Generated by Django 3.1.7 on 2021-03-08 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookModel', '0004_auto_20210309_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='AuthorDetail', to='BookModel.author'),
        ),
    ]
