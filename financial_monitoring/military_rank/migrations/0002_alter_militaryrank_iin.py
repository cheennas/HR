# Generated by Django 4.2.4 on 2023-09-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_info', '0003_alter_generalinfo_group'),
        ('military_rank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militaryrank',
            name='iin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='military_rank', to='general_info.generalinfo'),
        ),
    ]