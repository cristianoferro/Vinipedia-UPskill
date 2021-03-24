from django.urls import path
from wine import views

app_name = 'wine'

urlpatterns = [
    path('', views.WineList.as_view(), name='wine_list'),
]
