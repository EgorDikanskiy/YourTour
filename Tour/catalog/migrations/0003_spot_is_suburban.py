# Generated by Django 4.2.5 on 2024-03-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='is_suburban',
            field=models.BooleanField(default=True, null=True, verbose_name='загороднее'),
        ),
    ]
