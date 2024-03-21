from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]