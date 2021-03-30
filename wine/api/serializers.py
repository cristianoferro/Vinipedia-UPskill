from rest_framework import serializers

from wine.models import Evaluation, Grape, Wine


class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


class GrapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grape
        fields = '__all__'


class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'
