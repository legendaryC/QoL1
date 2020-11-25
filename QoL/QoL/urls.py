"""QoL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
# from main import views

# To custom my console website
# default: "Django Administration"
admin.site.site_header = 'QoL Console'
# default: "Site administration"
admin.site.index_title = 'QoL Console'
admin.site.site_title = 'QoL Console'
admin.site.site_url = "http://localhost:8080/"

# admin.autodiscover()
# admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('console/', admin.site.urls),
    path('login/', include('main.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),


]
