from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URLConf
urlpatterns = [
    path("",views.homepage),
    path('nearByRestaurant/',views.near_buy_restaurants),
    path('manageRestaurant',views.manageRestaurant),
    path('deleteRestaurant',views.deleteRestaurant),
    path('addNewRestaurant',views.addNewRestaurant),
    path('editRestaurant',views.editRestaurant),
    path('updateRestaurant',views.updateRestaurant),
    path('addRestaurant',views.addRestaurant),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)