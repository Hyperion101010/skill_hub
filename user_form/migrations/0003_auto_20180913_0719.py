# Generated by Django 2.0.7 on 2018-09-13 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0002_auto_20180912_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='category',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Doctor', 'Doctor'), ('Clerk', 'Clerk')], default='Engineering', max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]