from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.task = Task.objects.create(
            user=self.user, title='Test Task', description='Test Desc', status='todo'
        )
        token_response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser', 'password': 'testpass123'
        })
        self.access_token = token_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Desc', 'status': 'todo'}
        response = self.client.post(reverse('task_list_create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_tasks(self):
        response = self.client.get(reverse('task_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
