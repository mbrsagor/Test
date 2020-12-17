# Generated by Django 2.0.8 on 2018-08-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divineit', '0010_auto_20180805_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='feedback',
        ),
        migrations.AddField(
            model_name='contactperson',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
