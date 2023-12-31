# Generated by Django 4.2.4 on 2023-08-21 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_info', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(blank=True, max_length=255, null=True)),
                ('course_organization', models.CharField(blank=True, max_length=255, null=True)),
                ('course_start_date', models.DateField(null=True)),
                ('course_end_date', models.DateField(null=True)),
                ('document_type', models.CharField(blank=True, max_length=255, null=True)),
                ('course_name', models.CharField(blank=True, max_length=255, null=True)),
                ('iin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='general_info.generalinfo')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
