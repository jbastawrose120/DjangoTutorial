from django.urls import path, include
#from django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    #url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail'),
    path('<int:pk>/', views.SchoolDetailView.as_view(),name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
]
