from django.shortcuts import render
from rest_framework import viewsets, generics
from materials.models import Course, Lesson, Subscription
from materials.serializers import CourseSerializers, LessonSerializers, SubscriptionSerializers
from materials.permissions import IsOwner, IsStaff
from rest_framework.permissions import IsAuthenticated, AllowAny
from materials.paginators import MaterialsPaginator
from materials.tasks import _send_email


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated | IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        update_course = serializer.save()
        _send_email.delay(update_course.pk)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsStaff]
    pagination_class = MaterialsPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated | IsStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
        _send_email.delay(new_lesson.course_id)


class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializers

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.user = self.request.user
        new_sub.save()


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner, IsStaff]


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner, IsStaff]
