# Generated by Django 3.1.3 on 2020-11-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]