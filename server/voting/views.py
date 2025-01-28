from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import User, Project, Vote, AuditLog
from .permissions import IsOwner
from .serializers import ProjectSerializer, VoteSerializer, AuditLogSerializer


from django.http import JsonResponse
from django.db import connection
def find_user_by_username(username):
    with connection.cursor() as cursor:
        # Уязвимый SQL-запрос
        query = f"SELECT * FROM auth_user WHERE username = '{username}';"
        cursor.execute(query)
        return cursor.fetchall()
#http://127.0.0.1:8000/vulnerable/?username=admin' OR '1'='1


def vulnerable_view(request):
    username = request.GET.get("username", "")
    if username:
        try:
            # Используем уязвимую функцию
            result = find_user_by_username(username)
            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Please provide a username as ?username=..."}, status=400)

"""
================AdminOnly================
"""
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAdminUser]

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]



"""
================Lists read only================
"""
class ProjectAPIList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VoteAPIList(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class AuditAPIList(generics.ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]




"""
================single model instance read only================
"""

class ProjectAPIRetrieve(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VoteAPIRetrieve(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class AuditAPIRetrieve(generics.RetrieveAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]




"""
================single model instance read only================
"""

class ProjectAPIRetrieve(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VoteAPIRetrieve(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class AuditAPIRetrieve(generics.RetrieveAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]




"""
================single model instance delete only================
"""
class ProjectAPIDestroy(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated, IsOwner]







"""
================single model instance create-only================
"""


class ProjectAPICreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class VoteAPICreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class ProjectAPIUpdate(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser,]

