from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about',views.about, name = 'about'),
    path('made',views.made, name = 'made'),
    path('ok_order',views.ok_order, name = 'ok_order'),
]
