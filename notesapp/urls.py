from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import NoteViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
