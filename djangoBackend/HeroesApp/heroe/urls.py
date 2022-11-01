#Django import
from django.urls import path

#Views
from heroe.views import HeroAPIView,CreateAPIView,HeroDetailsAPIView

#Urls
urlpatterns = [
    
    path('heroe-list/',HeroAPIView.as_view(),name="heroe_list"),
    path('heroe-create/',CreateAPIView.as_view(),name="create"),
    path('heroe-details/<int:pk>/',HeroDetailsAPIView.as_view(),name="details"),
]