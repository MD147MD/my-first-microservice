# Generated by Django 3.0.5 on 2021-05-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]