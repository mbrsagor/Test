# Generated by Django 2.0.13 on 2020-02-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200218_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='seoitem',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
