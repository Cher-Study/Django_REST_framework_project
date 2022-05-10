from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import User, Project, Todo
from .serializer import UserModelSerializer, ProjectModelSerializer, TodoModelSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserReadViewSet(
    # CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    # DestroyModelMixin,
    ListModelMixin,
    GenericViewSet
):
    permission_classes = [DjangoModelPermissions]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class ProjectModelViewSet(ModelViewSet):
    pagination_class = ProjectLimitOffsetPagination
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name', None)
        if project_name:
            return Project.objects.filter(project_name__contains=project_name)
        return Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    pagination_class = TodoLimitOffsetPagination
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        project = self.request.query_params.get('project', None)
        if project:
            return Todo.objects.filter(project=project)
        return Todo.objects.all()
