# Generated by Django 3.2.12 on 2024-03-01 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test7', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='original_data',
            new_name='notify_data',
        ),
    ]
