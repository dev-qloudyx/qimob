from django.test import TestCase, Client
from django.urls import reverse

from apps.docs.models import File
from apps.users.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", email='test@qloudyx.pt', password='12345')
        self.file = File.objects.create(token='testtoken', app='testapp', model='testmodel', upload='testfile.txt')
        self.client.login(email='test@qloudyx.pt', password='12345')
    
    def test_file_delete_view(self):
        response = self.client.post(reverse('docs:file_delete_view', args=[self.file.token]))
        self.assertEquals(response.status_code, 200)
        self.assertTrue(File.objects.get(id=self.file.token).deleted)

    def test_file_view(self):
        response = self.client.get(reverse('docs:file_view', args=[self.file.token]))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.file.token)

    def test_file_list_view(self):
        response = self.client.get(reverse('docs:file_list_view'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.file.token)

    def test_file_upload_view_get(self):
        response = self.client.get(reverse('docs:file_upload_view'))
        self.assertEquals(response.status_code, 200)

    def test_file_upload_view_post(self):
        with open('testfile.txt', 'w') as file:
            response = self.client.post(reverse('docs:file_upload_view'), {'upload': file})
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(File.objects.all(), ['<File: testfile.txt>'])
