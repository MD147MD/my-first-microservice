# Generated by Django 3.0.5 on 2021-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField(max_length=800)),
            ],
        ),
    ]
