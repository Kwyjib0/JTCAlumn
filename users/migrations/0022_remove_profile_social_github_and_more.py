# Generated by Django 4.0.3 on 2022-04-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_social_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_github',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_linkedin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_twitter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_website',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_youtube',
        ),
        migrations.AddField(
            model_name='profile',
            name='organization_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(default='alum', max_length=200),
        ),
    ]
