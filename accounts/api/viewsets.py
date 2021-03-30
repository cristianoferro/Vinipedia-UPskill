from django.contrib.auth.models import User
from rest_framework import viewsets

from accounts.api.serializers import ProfileSerializer, UserSerializer
from accounts.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
