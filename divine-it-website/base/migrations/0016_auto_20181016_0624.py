# Generated by Django 2.0.9 on 2018-10-16 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_standardpage_seo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standardpage',
            old_name='seo',
            new_name='seo_keyword',
        ),
    ]
