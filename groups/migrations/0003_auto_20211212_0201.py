# Generated by Django 2.2.16 on 2021-12-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_groupuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
