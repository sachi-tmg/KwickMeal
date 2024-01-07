from django.db import models

# Create your models here.
# Create your models here.



class Drink(models.Model):
    drinks_name=models.CharField(max_length=50)
    drinks_picture=models.ImageField()
    drinks_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.drinks_name
    
class Snack(models.Model):
    snacks_name=models.CharField(max_length=50)
    snacks_picture=models.ImageField()
    snacks_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.snacks_name

class Dessert(models.Model):
    dessert_name=models.CharField(max_length=50)
    dessert_picture=models.ImageField()
    dessert_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.dessert_name
    
class Breakfast(models.Model):
    breakfast_name=models.CharField(max_length=50)
    breakfast_picture=models.ImageField()
    breakfast_price = models.DecimalField(max_digits=5, decimal_places=2)
    breakfast_description=models.CharField(max_length=250)
    def __str__(self):
        return self.breakfast_name

class Dinner(models.Model):
    dinner_name=models.CharField(max_length=50)
    dinner_picture=models.ImageField()
    dinner_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.dinner_name
    
class Burger(models.Model):
    burger_name=models.CharField(max_length=50)
    burger_picture=models.ImageField()
    burger_price = models.DecimalField(max_digits=5, decimal_places=2)
    burger_description=models.CharField(max_length=250)
    
    def __str__(self):
        return self.burger_name

class Pizza(models.Model):
    pizza_name=models.CharField(max_length=50)
    pizza_picture=models.ImageField()
    pizza_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.pizza_name
