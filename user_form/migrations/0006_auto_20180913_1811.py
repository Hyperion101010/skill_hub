# Generated by Django 2.0.7 on 2018-09-13 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0005_auto_20180913_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='skill',
            new_name='name',
        ),
    ]
