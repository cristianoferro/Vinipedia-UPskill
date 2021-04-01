from rest_framework import serializers

from producer.models import Producer, ProducerPicture


class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ProducerPictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProducerPicture
        fields = ('pathname', 'producer')