from rest_framework import serializers
from payment.serializers import PaymentSerializer
from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка пользователей"""
    payments_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "city", "avatar", "payments_history"]


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для одного пользователя"""
    payments_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "city", "avatar", "payments_history"]


class UserLimitSerializer(serializers.ModelSerializer):
    """Сериализатор выводит информацию для сторонненго пользователя"""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "city", "avatar"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания пользователя
    """

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "phone", "city", "is_active", "password"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
