from django.conf.urls import url
from leveltwo_firstapp import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
