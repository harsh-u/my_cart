# Generated by Django 3.1.5 on 2021-01-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210123_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]