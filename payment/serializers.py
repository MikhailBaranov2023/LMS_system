from rest_framework import serializers

from payment.models import Payment
from payment.services import create_payment, create_session_payment
from materials.serializers import CourseSerializers


class PaymentSerializer(serializers.ModelSerializer):
    Course = CourseSerializers(many=True, read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        course = validated_data.pop('paid_course')
        payment_intent = create_payment(validated_data['payment_amount'])
        session_payment = create_session_payment(payment_intent['amount'], course.name)
        payment = Payment(
            payment_amount=validated_data["payment_amount"],
            payment_method=validated_data["payment_method"],
            payment_id=payment_intent['id'],
            payment_link=session_payment['url'],
        )
        payment.save()
        return payment
