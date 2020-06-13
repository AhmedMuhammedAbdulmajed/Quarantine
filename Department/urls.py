from django.urls import path
from . import views
app_name='Department'
urlpatterns = [
    path('', views.Deparment_List,name='Deparment_List'),
    path('<int:id>', views.Deparment_detial,name='Deparment_detial'),
]