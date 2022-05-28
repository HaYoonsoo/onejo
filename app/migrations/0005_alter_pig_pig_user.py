# Generated by Django 4.0.4 on 2022-05-27 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_pig_pig_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pig',
            name='Pig_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pigs', to=settings.AUTH_USER_MODEL),
        ),
    ]
