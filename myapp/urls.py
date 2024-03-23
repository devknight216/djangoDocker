from django.urls import path, include
from rest_framework import routers
from .views import NodeViewSet, AnalyzerViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'analyzers', AnalyzerViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
