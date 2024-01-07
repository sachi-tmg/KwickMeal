from django.contrib import admin
from customer_orders.models import Customer,Food_Item,Customer_Order,Reservation


admin.site.register([Customer])

admin.site.register([Food_Item])
admin.site.register([Customer_Order])
admin.site.register([Reservation])

# Register your models here.
