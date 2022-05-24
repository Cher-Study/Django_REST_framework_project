from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserReadViewSet, ProjectModelViewSet, TodoModelViewSet


app_name = 'library'

router = DefaultRouter()

router.register('users', UserReadViewSet)
router.register('projects', ProjectModelViewSet)
router.register('ToDos', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
