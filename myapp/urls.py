from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-data/', views.retrieve_data, name='retrieve_data'),
]

