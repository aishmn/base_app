# Generated by Django 3.0.4 on 2020-03-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfollio', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.URLField(default='www.google.com'),
        ),
    ]
