from rest_framework import serializers
from materials.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'lesson')
