from ...models import Product, Category, Store
from django.db import IntegrityError


class Storedb:
    """this class purpose is to insert all data received to the database"""

    def insert_product(self, data, stores_list):
        """ this method insert the products' items into the 'Product' 
            table, it require the product list as a first argument
            and the store list as the second argument"""

        b = Product(product_name=data["product_name_fr"],
                    product_id=data["id"],
                    category_id=Category.objects.get(name="Boissons gazeuses"),
                    link=data["url"],
                    description=data["ingredients_text"],
                    nutriscore=data["nutrition_grade_fr"],
                    mini_image=data["image_front_small_url"],
                    image=data["image_front_url"]
                    )
        b.save()
        for store in stores_list:
            b.stores.add(Store.objects.get(name=store))

    def insert_store(self, product):
        """this method insert the store's item into the 'store' table"""

        store_list = self.storecleaner(product)
        for i in store_list:
            try:
                b = Store(name=i)
                b.save()
            except IntegrityError as e:
                print(str(e))
        return store_list

    def storecleaner(self, data):
        """clean the string of stores received into a list and return it"""
        
        store = data['stores']
        store_list = store.split(",")
        for c in range(len(store_list)):
            store_list[c] = store_list[c].strip()
        return store_list


