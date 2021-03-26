from django.urls import path
from producer.views import ProducerList, ProducerDetail

app_name = 'producer'

urlpatterns = [
    path('', ProducerList.as_view(), name='producer_list'),
    path('detail/<int:pk>/', ProducerDetail.as_view(), name='producer_detail'),
]
