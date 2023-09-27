from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='video_link')]


class CourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, read_only=True)
    count_lesson = serializers.SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_count_lesson(self, instance):
        return instance.lesson.count()

    def get_is_subscribed(self, instance):
        request = self.context.get('request')
        subscription = Subscription.objects.filter(course=instance.pk, user=request.user).exists()
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'count_lesson', 'is_subscribed', 'preview', 'lesson',)
