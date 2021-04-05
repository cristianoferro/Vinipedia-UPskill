from rest_framework import viewsets, filters

from producer.api.serializers import ProducerSerializer, ProducerPictureSerializer, PictureAuthorSerializer
from producer.models import PictureAuthor, Producer, ProducerPicture


class PictureAuthorViewSet(viewsets.ModelViewSet):
    queryset = PictureAuthor.objects.all()
    serializer_class = PictureAuthorSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name']



class ProducerPictureViewSet(viewsets.ModelViewSet):
    queryset = ProducerPicture.objects.all()
    serializer_class = ProducerPictureSerializer

