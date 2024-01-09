from django.contrib import admin
from customer_orders.models import Customer,Food_Item,Food,Order


admin.site.register([Customer])

admin.site.register([Food_Item])
admin.site.register([Food])
admin.site.register([Order])

# Register your models here.
