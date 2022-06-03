from django.contrib import admin
from .models import Restaurant, Review
from .models import Menu

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Review)