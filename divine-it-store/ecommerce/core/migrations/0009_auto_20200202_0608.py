# Generated by Django 2.0.13 on 2020-02-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_user_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sts_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sts_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
