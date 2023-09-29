from django.db import models
from django.conf import settings
from users.models import NULLABLE
from materials.models import Course, Lesson


# Create your models here.
class Payment(models.Model):
    CASH = 'cash'
    TRANSFER_TO_ACCOUNT = 'transfer to account'

    PAYMENT_METHOD = (
        (CASH, 'Наличными'),
        (TRANSFER_TO_ACCOUNT, 'Перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                             **NULLABLE, related_name='user')
    date_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплата курса', **NULLABLE,
                                    related_name='paid_course')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплата урока', **NULLABLE,
                                    related_name='paid_lesson')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50, verbose_name='способ оплаты')

    payment_id = models.TextField(verbose_name="payment_id", **NULLABLE)

    payment_link = models.CharField(max_length=150, verbose_name='ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'оплата: {self.paid_course if self.paid_course else self.paid_lesson} - {self.payment_amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
