# Generated by Django 4.1.5 on 2023-10-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0006_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='position',
            new_name='actype',
        ),
    ]