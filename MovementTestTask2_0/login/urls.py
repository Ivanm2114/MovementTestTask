from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/<str:surname>/', views.success_create, name='success'),
    path('', include(router.urls)),
]
