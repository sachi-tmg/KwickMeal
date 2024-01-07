from django.db import models
from food_item.models import Burger,Pizza,Breakfast,Snack,Drink,Dessert,Dinner
# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)  # Adjust the max length according to your needs
    email = models.EmailField(unique=True)  # Ensure uniqueness for email addresses
    password = models.CharField(max_length=50)  # Use a longer field to store hashed passwords

    def __str__(self):
        return self.customer_name
    
class Food_Item(models.Model):   
    burger = models.ForeignKey(Burger, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)

class Customer_Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_item = models.ForeignKey(Food_Item, on_delete=models.CASCADE)



    
class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField(max_length=50)
    date=models.DateField(max_length=50)
    time=models.TimeField(max_length=50)
    No_of_guest=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    



