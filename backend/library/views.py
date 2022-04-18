from rest_framework.viewsets import ModelViewSet
from .models import User, Project, Todo
from .serializer import UserModelSerializer, ProgectModelSerializer, TodoModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProgectModelSerializer
    queryset = Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
