from .models import User, Project, Todo
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, StringRelatedField


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'email')


class SingleUserModelSerializer(ModelSerializer):
    # user_name = StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('user_name',)


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('project_name', 'repo', 'users')


class TodoModelSerializer(ModelSerializer):
    author = SingleUserModelSerializer()
    # author = StringRelatedField()

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ('author', 'text', 'project')
