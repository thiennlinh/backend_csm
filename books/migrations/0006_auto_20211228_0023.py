# Generated by Django 2.2.16 on 2021-12-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_chapter_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='star',
        ),
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]