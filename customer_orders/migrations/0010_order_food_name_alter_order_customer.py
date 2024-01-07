# Generated by Django 4.2.7 on 2024-01-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_orders', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='food_name',
            field=models.ForeignKey(default=50, on_delete=django.db.models.deletion.CASCADE, to='customer_orders.dessert'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_orders.customer'),
        ),
    ]