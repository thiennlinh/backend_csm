# Generated by Django 2.2.16 on 2022-01-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0004_auto_20220113_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('another', 'Another')], default='male', max_length=20),
        ),
    ]
