from django.test import TestCase
from authentification.models import User


class TestViews(TestCase):
    """ class that test the view of the 'authentification' app """

    def setUp(self):
        test_user1 = User.objects.create_user(username='rien@g.com', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_profil_view_logged(self):
        self.client.login(username='rien@g.com', password='1X<ISRUkw+tuK')
        resp = self.client.get('/profil/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'authentification/profil.html')
    
    def test_profil_view_not_logged(self):
        resp = self.client.get('/profil/')

        self.assertEqual(resp.status_code, 302)
    