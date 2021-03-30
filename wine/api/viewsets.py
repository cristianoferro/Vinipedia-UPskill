from rest_framework import viewsets
from wine.models import Evaluation, Grape, Wine
from .serializers import EvaluationSerializer, GrapeSerializer, WineSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class GrapeViewSet(viewsets.ModelViewSet):
    queryset = Grape.objects.all()
    serializer_class = GrapeSerializer


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
