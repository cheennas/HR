# Generated by Django 4.2.4 on 2023-08-21 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(blank=True, max_length=255, null=True)),
                ('order_date', models.DateField(null=True)),
                ('types_of_order_types', models.CharField(blank=True, max_length=255, null=True)),
                ('iin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_list', to='general_info.generalinfo')),
            ],
            options={
                'db_table': 'orders_list',
            },
        ),
    ]
