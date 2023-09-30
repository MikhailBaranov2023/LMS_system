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


def create_session_payment(amount: int, name_product: str):
    # stripe.api_key = settings.STRIPE_API_KEY
    stripe.api_key = "sk_test_51NvSQBG1tycGbCbRdjRZc9mldsBVskffmETDlUa35Mva9xGnXezRbIu2A92Sr7OHO5vmK33k78X3jQLbEDH4fJ6400kP9yNGr3"
    product = stripe.Product.create(name=name_product)
    price = stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        recurring={"interval": "month"},
        product=product['id'],
    )
    response = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price['id'],
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return response


# print(create_session_payment(1000, 'Python course')['url'])
