# Generated by Django 4.2.4 on 2023-09-03 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('general_info', '0002_generalinfo_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_info', to='group.group'),
        ),
    ]
