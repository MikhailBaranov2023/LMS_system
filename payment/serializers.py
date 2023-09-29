from rest_framework import serializers

# from payment.services.payment import create_payment
from payment.models import Payment
from payment.services import create_payment
from materials.serializers import CourseSerializers


class PaymentSerializer(serializers.ModelSerializer):
    course = CourseSerializers(many=True, read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        payment = Payment(
            payment_amount=validated_data["payment_amount"],
            payment_method=validated_data["payment_method"],
            payment_id=create_payment(validated_data['payment_amount']),
        )
        payment.save()
        return payment
