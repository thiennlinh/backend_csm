# Generated by Django 2.2.16 on 2022-01-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0003_auto_20211212_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 0), ('female', 1), ('another', 2)], default='male', max_length=20),
        ),
    ]
