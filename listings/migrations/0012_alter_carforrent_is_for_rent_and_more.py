# Generated by Django 5.0.3 on 2024-11-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_carforrent_is_for_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carforrent',
            name='is_for_rent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='is_for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='carforsale',
            name='is_for_rent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='carforsale',
            name='is_for_sale',
            field=models.BooleanField(default=True),
        ),
    ]