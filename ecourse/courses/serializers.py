from rest_framework.serializers import ModelSerializer
from .models import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'description', 'created_date', 'category']