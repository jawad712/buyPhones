from django.db import models

# Create your models here.


class Menu(models.Model):
    starter_menu = models.TextField()
    main_course= models.TextField()
    desert= models.TextField()
    date = models.DateField()
class Restaurant(models.Model):
    title = models.CharField(max_length=150)
    img=models.ImageField(upload_to="restaurant_images")
    desc= models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    address=models.TextField()
    phone = models.CharField(max_length=16)
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField()
    id = models.OneToOneField(Menu,on_delete=models.CASCADE,primary_key=True)



class Review(models.Model):
    user_name = models.CharField(max_length=150)
    comments= models.TextField(max_length=300)
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,primary_key=True)
