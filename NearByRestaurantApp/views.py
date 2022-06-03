from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from manage import main
from .models import Restaurant , Review ,Menu

# Create your views here.


def homepage(request):
    return render(request,'index.html')

def near_buy_restaurants(request):
    try:
        if(request.GET['search_keyword']):
            search_keyword = request.GET['search_keyword']
            restaurants = Restaurant.objects.filter(title__contains=search_keyword)
        else:
            restaurants = Restaurant.objects.all()
        
        return render(request,'nearByRestaurant.html',{'restaurants':restaurants})
    except:
        print('Something Went Wrong')

def error_404_view(request,exception):
    return render(request,'404.html')
