# Generated by Django 4.2.4 on 2023-10-02 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family_composition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familycomposition',
            old_name='birth_date',
            new_name='birth_date_family',
        ),
    ]