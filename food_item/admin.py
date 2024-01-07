from django.contrib import admin
from customer_orders.models import Drink,Snack,Dessert,Breakfast,Dinner,Burger,Pizza

admin.site.register([Drink])
admin.site.register([Snack])
admin.site.register([Dessert])
admin.site.register([Breakfast])
admin.site.register([Dinner])
admin.site.register([Burger])
admin.site.register([Pizza])


# Register your models here.
