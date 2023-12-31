# Generated by Django 4.2.4 on 2023-09-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_info', '0004_generalinfo_birth_oblast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.TextField(blank=True, null=True)),
                ('iin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='general_info.generalinfo')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]
