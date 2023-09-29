import stripe
from django.conf import settings
import requests
from django.urls import reverse


def create_payment(amount):
    stripe.api_key = settings.STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    # print(response)
    return response