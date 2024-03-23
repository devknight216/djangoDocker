from rest_framework import viewsets
from .models import Node, Analyzer, Task
from .serializers import NodeSerializer, AnalyzerSerializer, TaskSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class AnalyzerViewSet(viewsets.ModelViewSet):
    queryset = Analyzer.objects.all()
    serializer_class = AnalyzerSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
