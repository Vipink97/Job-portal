# Generated by Django 3.0.6 on 2020-06-16 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_portal', '0004_auto_20200610_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
