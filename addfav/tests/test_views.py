from django.test import TestCase
from authentification.models import User
from offapi.tests.test_models import ProductTest


class Test_views(TestCase):

    def test_add_view(self):
        resp = self.client.get('/rien/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'addfav/add.html')
    
    def test_favorite_view(self):
        # test a revoir meme si il fonctionne"
        user = User(username='admin' , password='rien123456789')
        user.save()
        ProductTest().create_Product(product_id='5449000000996')
        ProductTest().create_Product(product_id='3068320114453')
        resp = self.client.get('/nop/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'addfav/add.html')