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


def addRestaurant(request):
    try:
        photo = request.FILES
        title = request.GET.get('title',False)
        img = "restaurant_images/"+request.GET.get('img',False)
        desc = request.GET.get('desc',False)
        lat = request.GET.get('lat',False)
        lng = request.GET.get('lng',False)
        address = request.GET.get('address',False)
        phone = request.GET.get('phone',False)
        opening_time = request.GET.get('opening_time',False)
        closing_time = request.GET.get('closing_time',False)
        date = request.GET.get('date',False)
        starter_menu = request.GET.get('starter_menu',False)
        main_course = request.GET.get('main_course',False)
        desert = request.GET.get('desert',False)
        menu = Menu.objects.create(starter_menu=starter_menu,main_course=main_course,desert=desert,date=date)
        Restaurant.objects.create(title=title,img=img,desc=desc,lat=lat,lng=lng,address=address,phone=phone,opening_time=opening_time,closing_time=closing_time,date=date,id_id=menu.id)
        restaurants = Restaurant.objects.all()
        return render(request,'manageProduct.html',{'restaurants':restaurants})
    except:
        print("something went wrong while adding restaurant")    
def addNewRestaurant(request):
    return render(request,'addNewRestaurant.html')

def editRestaurant(request):
    rest_id = request.GET['rest_id']
    return render(request,'editRestaurant.html',{"rest_id":rest_id})

def updateRestaurant(request):
    title = request.GET.get('title',False)
    rest_id = request.GET.get('rest_id',False)
    Restaurant.objects.filter(id_id=rest_id).update(title=title)
    restaurants = Restaurant.objects.all()
    return render(request,'manageProduct.html',{'restaurants':restaurants})

def manageRestaurant(request):
    try:
        restaurants = Restaurant.objects.all()
        return render(request,'manageProduct.html',{'restaurants':restaurants})
    except:
        print("something Went Wrong in Manage restaurant")    
def deleteRestaurant(request):
    try:
        Restaurant.objects.get(id_id=request.GET['rest_id']).delete()
        restaurants = Restaurant.objects.all()
        return render(request,'manageProduct.html',{'restaurants':restaurants})
    except:
       print("something Went Wrong while deleting restaurant")

