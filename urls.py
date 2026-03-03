from django.urls import path
from .views import search_items
from . import views

##http://localhost:800/admin/


urlpatterns = [
    path("menu/search/", search_items,),
]
