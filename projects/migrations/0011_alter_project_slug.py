# Generated by Django 4.0.3 on 2022-03-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
