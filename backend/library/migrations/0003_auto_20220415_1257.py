# Generated by Django 3.2.12 on 2022-04-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
