from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonListAPIView, LessonUpdateAPIView, LessonDeleteAPIView, \
    LessonDetailAPIView, LessonCreateAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView, \
    SubscriptionDeleteAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
app_name = MaterialsConfig.name

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/view/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_view'),
                  path('lesson/edit/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_edit'),
                  path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

                  path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscriptions_list'),
                  path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscriptions_create'),
                  path('subscriptions_list/delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(),
                       name='subscriptions_delete')
              ] + router.urls
