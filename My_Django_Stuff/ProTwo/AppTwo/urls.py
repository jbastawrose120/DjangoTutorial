from django.conf.urls import url
from django.urls import path
from AppTwo import views

urlpatterns = [
    #url(r'^$', views.help, name='help')
    #url(r'^help/', views.help, name='help'),
    path('help/', views.help, name='help'),
    #path('', views.index, name='index'),
]
