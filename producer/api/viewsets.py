from rest_framework import viewsets

from producer.api.serializers import ProducerSerializer, ProducerPictureSerializer, PictureAuthorSerializer
from producer.models import PictureAuthor, Producer, ProducerPicture


class PictureAuthorViewSet(viewsets.ModelViewSet):
    queryset = PictureAuthor.objects.all()
    serializer_class = PictureAuthorSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerPictureViewSet(viewsets.ModelViewSet):
    queryset = ProducerPicture.objects.all()
    serializer_class = ProducerPictureSerializer

