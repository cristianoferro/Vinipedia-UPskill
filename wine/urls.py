from django.urls import path
from wine.views import WineDetail, WineList, search

app_name = 'wine'

urlpatterns = [
    path('', WineList.as_view(), name='wine_list'),
    path('types/<slug:tag_slug>', WineList.as_view(), name='wine_list_by_type'),
    path('<int:pk>', WineDetail.as_view(), name='wine_detail'),
    path('search', search, name='search'),
]
