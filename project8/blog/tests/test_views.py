from django.test import TestCase
from authentification.models import User


class TestViews(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK', email='rien@g.com')
        test_user1.save()

    def test_home_log_fail_view(self):
        resp = self.client.get('/')
         #test if not logged then redirect
        self.assertRedirects(resp, '/login/?next=/')

    def test_home_view(self):
        self.client.login(username='rien@g.com', password='1X<ISRUkw+tuK') #log the user
        resp = self.client.get('/')              
        
        self.assertEqual(str(resp.context['user']), 'rien@g.com')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/db.html')
    
    def test_index_view(self):
        resp = self.client.get('/index/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/index.html')

    def test_base_view(self):
        resp = self.client.get('/base/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/base.html')