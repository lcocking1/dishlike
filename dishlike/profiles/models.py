from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    birthdate = models.DateField()

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=200)

class Menu(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=64)
    item_name = models.CharField(max_length=200)
    price = models.DecimalField()

class UserMenu(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    like_indicator = models.BooleanField()
    transaction_date = models.DateTimeField()
