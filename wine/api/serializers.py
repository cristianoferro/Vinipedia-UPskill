from rest_framework import serializers

from wine.models import Evaluation, Grape, Wine, Tag


class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


class GrapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grape
        exclude = ('img_author',)

class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        exclude = ('img_author',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
