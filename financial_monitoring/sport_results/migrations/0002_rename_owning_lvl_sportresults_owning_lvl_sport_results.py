# Generated by Django 4.2.4 on 2023-09-26 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_results', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportresults',
            old_name='owning_lvl',
            new_name='owning_lvl_sport_results',
        ),
    ]
