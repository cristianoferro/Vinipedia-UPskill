from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from wine.models import Evaluation, Grape, Wine, Tag
from .serializers import EvaluationSerializer, GrapeSerializer, WineSerializer, TagSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class GrapeViewSet(viewsets.ModelViewSet):
    queryset = Grape.objects.all()
    serializer_class = GrapeSerializer


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
