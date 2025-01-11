"""
URL configuration for citizens_budget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

from voting.views import *

router = routers.DefaultRouter()
router.register(r'admin/projects', ProjectViewSet)
router.register(r'admin/votes', VoteViewSet)
router.register(r'admin/logs', AuditLogViewSet)
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)), # http://127.0.0.1:8000/api/projects

    path('api/projects/', ProjectAPIList.as_view()),
    path('api/votes/', VoteAPIList.as_view()),
    path('api/logs/', AuditAPIList.as_view()),

    path('api/projects/<int:pk>/', ProjectAPIRetrieve.as_view()),
    path('api/votes/<int:pk>/', VoteAPIRetrieve.as_view()),
    path('api/logs/<int:pk>/', AuditAPIRetrieve.as_view()),

    path('api/projectdelete/<int:pk>/', ProjectAPIDestroy.as_view()),

    path('api/projectcreate/', ProjectAPICreate.as_view()),
    path('api/vote/', VoteAPICreate.as_view()),


]

# path('api/projects/<int:pk>/', ProjectAPIUpdate.as_view()),
# path('api/projectsdelete/<int:pk>/', ProjectAPIDestroy.as_view())