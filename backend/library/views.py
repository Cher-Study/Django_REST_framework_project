from re import A
from rest_framework.viewsets import ModelViewSet
from .models import Author, User
from .serializer import AuthorModelSerializer, UserModelSerializer


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
