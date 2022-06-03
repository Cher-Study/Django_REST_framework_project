import graphene
from graphene_django import DjangoObjectType
from pkg_resources import require

from .models import User, Project, Todo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    user_by_id = graphene.Field(UserType, pk=graphene.Int(required=True))
    user_by_name = graphene.List(
        UserType, user_name=graphene.String(required=False))

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    def resolve_user_by_id(self, info, pk):
        return User.objects.get(pk=pk)

    def resolve_user_by_project(self, info, project=None):
        if not project:
            return User.objects.all()
        return User.objects.filter(project=project)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_name, first_name, last_name, email):
        user = User(user_name=user_name, first_name=first_name,
                    last_name=last_name, email=email)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        user_name = graphene.String(required=False)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, pk, user_name=None, first_name=None, last_name=None, email=None):
        user = User.objects.get(pk=pk)
        if user_name:
            user.user_name = user_name
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if user_name or first_name or last_name or email:
            user.save()
        return cls(user)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
