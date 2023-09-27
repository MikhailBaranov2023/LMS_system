from rest_framework.test import APITestCase
from rest_framework import status
from materials.models import Course, Lesson, Subscription
from users.models import User
from django.urls import reverse


class LessonTestCase(APITestCase):
    def create_user(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            username='test',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('1234')
        self.user.save()

    def setUp(self) -> None:
        """Подготовка данных"""
        self.create_user()

        self.course = Course.objects.create(
            name='course test',
            description='list test description',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='list test',
            description='list test description',
            owner=self.user
        )

    def test_lesson_list(self):
        """Проверка отображения всех уроков"""
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse('materials:lesson_list'))

        self.assertEquals(response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': 5, 'name': 'list test', 'description': 'list test description', 'preview': None, 'video_link': None,
             'course': None, 'owner': 4}]})
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_lesson(self):
        """Проверка создания урока"""
        self.client.force_authenticate(self.user)
        data = {
            "course": 1,
            "name": "create test",
            "description": "create test",
        }
        response = self.client.post(reverse('materials:lesson_create'), data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            Lesson.objects.count(), 2)

        self.assertTrue(Lesson.objects.all().exists())

    def test_lesson_delete(self):
        """Проверка удаления урока"""
        self.client.force_authenticate(self.user)
        response = self.client.delete(reverse('materials:lesson_delete', kwargs={'pk': self.lesson.id}))

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.exists())

    def test_edit_lesson(self):
        """Проверка изменения урока"""
        data = {
            "name": "update test",
            "description": "update test",
        }
        self.client.force_authenticate(self.user)
        response = self.client.patch(reverse('materials:lesson_edit', kwargs={'pk': self.lesson.id}), data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertTrue(Lesson.objects.all().exists())
