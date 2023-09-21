from django.db import models
from users.models import NULLABLE
from django.conf import settings


class Course(models.Model):
    """Информация о курсе"""
    name = models.CharField(max_length=100, unique=True, verbose_name=' Название')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    video_link = models.URLField(max_length=150, verbose_name="Ссылка на видео", **NULLABLE)

    course = models.ForeignKey(Course, verbose_name='курс', on_delete=models.CASCADE, related_name='lesson')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'
