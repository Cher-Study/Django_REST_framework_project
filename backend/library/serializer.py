from .models import User, Project, Todo
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, StringRelatedField


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'email')


class ProgectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('project_name', 'repo', 'users')


class TodoModelSerializer(ModelSerializer):
    author = UserModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
