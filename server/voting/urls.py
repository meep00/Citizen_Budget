from django.urls import path
from .views import ProjectListView, VoteView, AuditLogView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('audit-logs/', AuditLogView.as_view(), name='audit-logs'),
    path('api/v1/projectlist/', ProjectListView.as_view(), name='api-project-list'),
]
