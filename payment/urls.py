from payment.apps import PaymentConfig
from django.urls import path
from payment.views import PaymentListAPIView, PaymentCreateAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/',PaymentCreateAPIView.as_view(), name='payment_create'),

]
