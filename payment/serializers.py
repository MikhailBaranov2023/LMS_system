from rest_framework import serializers

# from payment.services.payment import create_payment
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"