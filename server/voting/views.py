from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User, Project, Vote, AuditLog
from .serializers import UserSerializer, ProjectSerializer, VoteSerializer, AuditLogSerializer

# Widok dla listy projektów i tworzenia projektów
class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_admin:
            return Response({"error": "Only admins can create projects"}, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        data['created_by'] = request.user.id
        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Widok dla głosowania
class VoteView(APIView):
    def post(self, request):
        user = request.user
        project_id = request.data.get('project_id')

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        if Vote.objects.filter(user=user, project=project).exists():
            return Response({"error": "You have already voted for this project"}, status=status.HTTP_400_BAD_REQUEST)

        vote = Vote.objects.create(user=user, project=project)
        return Response({"message": "Vote recorded", "vote_id": vote.id}, status=status.HTTP_201_CREATED)


# Widok dla logów audytu
class AuditLogView(APIView):
    def get(self, request):
        if not request.user.is_admin:
            return Response({"error": "Only admins can view audit logs"}, status=status.HTTP_403_FORBIDDEN)

        logs = AuditLog.objects.all()
        serializer = AuditLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
