# Generated by Django 4.1.1 on 2022-11-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='preferred_dish',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
