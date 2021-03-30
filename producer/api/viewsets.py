from rest_framework import viewsets

from producer.api.serializers import ProducerSerializer, ProducerPictureSerializer
from producer.models import Producer, ProducerPicture


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerPictureViewSet(viewsets.ModelViewSet):
    queryset = ProducerPicture.objects.all()
    serializer_class = ProducerPictureSerializer
