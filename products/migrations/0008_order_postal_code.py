# Generated by Django 3.1.3 on 2020-11-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201111_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
