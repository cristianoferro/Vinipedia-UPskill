from rest_framework import serializers

from producer.models import PictureAuthor, Producer, ProducerPicture

class PictureAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PictureAuthor
        fields = '__all__'

class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ProducerPictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProducerPicture
        fields = '__all__'