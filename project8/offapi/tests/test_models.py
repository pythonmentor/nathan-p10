from django.test import TestCase
from ..models import Category, Store, Product, ProductSaved
from django.contrib.auth.models import User


# models test
class CategoryTest(TestCase):

    def create_category(self, name="only a test"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.__str__(), w.name)

class StoreTest(TestCase):

    def create_store(self, name="only a test"):
        return Store.objects.create(name=name)

    def test_store_creation(self):
        w = self.create_store()
        self.assertTrue(isinstance(w, Store))
        self.assertEqual(w.__str__(), w.name)

class ProductTest(TestCase):

    def create_Product(self, product_id=123456789, product_name='justeuntest'):
        category = CategoryTest().create_category()
        return Product.objects.create(product_id=product_id, product_name=product_name, category_id=category) 

    def test_product_creation(self):
        w = self.create_Product()
        self.assertTrue(isinstance(w, Product))
        self.assertEqual(w.__str__(), w.product_name)

class ProductSavedTest(TestCase):

    def create_productsaved(self, a='testuser', b=124578, c=235689):
        user = User.objects.create(username=a)
        product_a = ProductTest().create_Product(product_id=124578)
        product_b = ProductTest().create_Product(product_id=235689)
        return ProductSaved.objects.create(user_id=user, product_id=product_a, sub_id=product_b)

    def test_productsaved_creation(self):
        w = self.create_productsaved()
        self.assertTrue(isinstance(w, ProductSaved))
        self.assertEqual(w.__str__(), '{} - {}'.format(w.user_id, w.product_id))