# Generated by Django 4.2.4 on 2023-09-26 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owning_languages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owninglanguages',
            old_name='owning_lvl',
            new_name='owning_lvl_language',
        ),
    ]
