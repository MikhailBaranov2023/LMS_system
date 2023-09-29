from payment.apps import PaymentConfig
from django.urls import path
from payment.views import PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView, PaymentDeleteAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/courses/<int:pk>/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_status'),
    path('delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment_delete')
]
