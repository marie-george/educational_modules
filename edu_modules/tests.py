from rest_framework import status
from django.urls import reverse
from edu_modules.models import EduModule
from users.models import User
from rest_framework.test import APITestCase, APIClient


class EduModulTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='user@mail.ru',
            first_name='test',
            last_name='test',
            is_staff=False,
            is_superuser=False
        )

        self.user.set_password('123')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.edu_module = EduModule.objects.create(
            name='test_name',
            description='test_description',
            owner=self.user
        )

    def test_get_list(self):
        """Проверка получения списка модулей"""

        response = self.client.get(reverse('edu_modules:modules_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [
                 {'id': self.edu_module.id,
                  'name': self.edu_module.name,
                  'description': self.edu_module.description,
                  'owner': 1}
             ]
             }
        )

    def test_module_create(self):
        """Проверка создания модуля"""

        response1 = self.client.post(
            reverse('edu_modules:module_create'),
            data={
                'name': 'test_name_2',
                'description': 'test_description_2',
                'owner': self.user.id
            }
        )

        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED
        )

    def test_module_update(self):
        """Проверка редактирования модуля"""

        response = self.client.put(
            f'/modules/update/{self.edu_module.id}/',
            data={
                'name': 'test_name',
                'description': 'test_description',
                'owner': self.user.id
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_module_delete(self):
        """Проверка удаления модуля"""

        response = self.client.delete(f'/modules/delete/{self.edu_module.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            EduModule.objects.all().count(),
            0
        )

    def test_get_module(self):
        """Проверка получения отдельного модуля"""

        response = self.client.get(f'/modules/{self.edu_module.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.edu_module.id,
                'name': self.edu_module.name,
                'description': self.edu_module.description,
                'owner': self.edu_module.owner_id
            }
        )
