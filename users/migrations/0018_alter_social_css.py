# Generated by Django 4.0.3 on 2022-03-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_social_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='css',
            field=models.CharField(blank=True, default='', editable=False, max_length=50, null=True),
        ),
    ]
