from django.urls import path
from wine.views import WineDetail, WineList, EvaluationList, search

app_name = 'wine'

urlpatterns = [
    path('', WineList.as_view(), name='wine_list'),
    path('types/<slug:tag_slug>', WineList.as_view(), name='wine_list_by_type'),
    path('detail/<int:pk>/', WineDetail.as_view(), name='wine_detail'),
    path('evaluations', EvaluationList.as_view(), name='evaluation_list'),
    path('search', search, name='search'),
]
