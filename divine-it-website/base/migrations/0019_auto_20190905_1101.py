# Generated by Django 2.0.13 on 2019-09-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20190514_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationsettings',
            name='recaptcha_private_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='applicationsettings',
            name='recaptcha_public_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicationsettings',
            name='theme',
            field=models.CharField(choices=[('default', 'default'), ('theme-1', 'theme-1'), ('theme-2', 'theme-2'), ('theme-3', 'theme-3'), ('theme-4', 'theme-4'), ('theme-5', 'theme-5'), ('theme-6', 'theme-6'), ('theme-7', 'theme-7'), ('theme-8', 'theme-8'), ('theme-9', 'theme-9'), ('theme-10', 'theme-10')], default='default', help_text='Select which theme to use', max_length=255),
        ),
    ]
