from rest_framework import serializers
from materials.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, read_only=True)
    count_lesson = serializers.SerializerMethodField()

    def get_count_lesson(self, instance):
        return instance.lesson.count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'lesson', 'count_lesson',)
