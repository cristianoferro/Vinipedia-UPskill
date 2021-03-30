"""vinipedia_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from accounts.api.viewsets import ProfileViewSet, UserViewSet
from producer.api.viewsets import ProducerViewSet, ProducerPictureViewSet
from wine.api.viewsets import EvaluationViewSet, GrapeViewSet, WineViewSet

from wine.views import EvaluationList


router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet)
router.register(r'accounts-profile', ProfileViewSet)
router.register(r'evaluations', EvaluationViewSet)
router.register(r'grapes', GrapeViewSet)
router.register(r'producer', ProducerViewSet)
router.register(r'producer-picture', ProducerPictureViewSet)
router.register(r'wine', WineViewSet)


urlpatterns = [
    path('', EvaluationList.as_view(), name='homepage'), # TODO mudar depois
    path('admin/', admin.site.urls),
    path('wines/', include('wine.urls')),
    path('accounts/', include('accounts.urls')),
    path('producer/', include('producer.urls')),

    # API paths
    path('api/', include(router.urls)),
    # TODO (Authentication):  path('api-auth', include('rest_framework.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)