# Generated by Django 3.0.4 on 2020-03-27 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfollio', '0009_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
