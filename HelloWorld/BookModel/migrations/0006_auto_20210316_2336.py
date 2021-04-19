# Generated by Django 3.1.7 on 2021-03-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookModel', '0005_auto_20210309_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='BookModel.author'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]