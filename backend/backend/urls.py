"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='1.0',
        description='description',
        contact=Contact(email='test@test.com'),
        license=License(name='MIT')
    ),
    public=True,
    # permission_classes=(AllowAny, )
)

urlpatterns = [
    path('api/', include('library.urls', namespace='1.0')),
    path('api/1.0/', include('library.urls', namespace='1.0')),
    path('api/2.0/', include('library.urls', namespace='2.0')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui()),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', TemplateView.as_view(template_name='index.html')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui())

]
