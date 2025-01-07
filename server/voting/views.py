from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import User, Project, Vote, AuditLog
from .permissions import IsOwner
from .serializers import ProjectSerializer, VoteSerializer, AuditLogSerializer

# Widok dla listy projektów i tworzenia projektów
# class ProjectListView(APIView):
#     def get(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         # if not request.user.is_admin:
#         #     return Response({"error": "Only admins can create projects"}, status=status.HTTP_403_FORBIDDEN)
#
#         data = request.data
#         data['created_by'] = request.user.id
#         serializer = ProjectSerializer(data=data)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'post': serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

