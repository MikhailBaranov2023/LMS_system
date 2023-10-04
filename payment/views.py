from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework.filters import OrderingFilter
from materials.models import Course
from rest_framework.permissions import AllowAny


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('date_payment',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')


class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        """Сохраняет пользователя и курс"""
        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.paid_course = Course.objects.get(pk=self.kwargs.get('pk'))
        new_payment.save()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """оплучаем платеж"""
    serializer_class = PaymentSerializer

    def get_object(self):
        object = Payment.objects.get(
            user=self.request.user,
            paid_course=Course.objects.get(pk=self.kwargs.get('pk')),
        )
        return object


class PaymentDeleteAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
