# Generated by Django 2.0.13 on 2020-02-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_product_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pricing_detail_link',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
