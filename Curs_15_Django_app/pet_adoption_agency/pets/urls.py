from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.pets, name='all_pets'),
    path('<int:pet_id>/', views.pet_detail, name='pet_detail')
]
