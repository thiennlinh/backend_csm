# Generated by Django 2.2.16 on 2021-12-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0002_auto_20211212_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='mobile'),
        ),
    ]
