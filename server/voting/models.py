from django.contrib.auth.models import User
from django.db import models

# Model Users
# class User(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     password_hash = models.CharField(max_length=255)
#     is_admin = models.BooleanField(default=False)
#     PESEL = models.CharField(max_length=50, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.username


# Model Projects
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Model Votes
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')  # Zapewnia, że użytkownik może głosować na dany projekt tylko raz

    def __str__(self):
        return f"Vote by {self.user.username} on {self.project.title}"


# Model AuditLogs
class AuditLog(models.Model):
    action = models.CharField(max_length=100)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="audit_logs")
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Action: {self.action} by {self.performed_by.username if self.performed_by else 'Unknown'}"
