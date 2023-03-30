from django.urls import path
from . import views

urlpatterns = [

    path('', views.HoemePage, name='home'),
    path('categores/', views.category, name='categorys'),
    path('<slug:slug>/', views.single_post, name='single'),

]
