from rest_framework import serializers
from .models import User, Project, Vote, AuditLog

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_admin', 'PESEL', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at']


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'user', 'project', 'created_at']


class AuditLogSerializer(serializers.ModelSerializer):
    performed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #performed_by = UserSerializer(read_only=True)
    class Meta:
        model = AuditLog
        fields = ['id', 'action', 'performed_by', 'details', 'created_at']
