# Generated by Django 4.2.7 on 2024-01-12 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='customer_orders.customer'),
        ),
    ]
