# Generated by Django 5.0.3 on 2024-11-02 05:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_remove_carforrent_user_remove_carforsale_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='carforrent',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars_for_rent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carforsale',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars_for_sale', to=settings.AUTH_USER_MODEL),
        ),
    ]
