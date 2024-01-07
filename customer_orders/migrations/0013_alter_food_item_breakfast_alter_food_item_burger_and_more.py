# Generated by Django 4.2.7 on 2024-01-04 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_item', '0001_initial'),
        ('customer_orders', '0012_remove_food_item_customer_customer_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_item',
            name='breakfast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.breakfast'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='burger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.burger'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='dessert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.dessert'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='dinner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.dinner'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.drink'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.pizza'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='snack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_item.snack'),
        ),
        migrations.DeleteModel(
            name='Breakfast',
        ),
        migrations.DeleteModel(
            name='Burger',
        ),
        migrations.DeleteModel(
            name='Dessert',
        ),
        migrations.DeleteModel(
            name='Dinner',
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Snack',
        ),
    ]