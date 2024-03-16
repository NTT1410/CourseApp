from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]