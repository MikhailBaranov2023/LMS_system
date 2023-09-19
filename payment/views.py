from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework.filters import OrderingFilter


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('date_payment',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
