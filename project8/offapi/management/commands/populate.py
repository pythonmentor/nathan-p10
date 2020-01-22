from django.core.management.base import BaseCommand, CommandError
from ...models import Category
import offapi.management.commands._api as offapi
import offapi.management.commands._updatedb as update

class Command(BaseCommand):
    help = 'call the OFF api and populate the DB'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        Category.objects.get_or_create(name="Boissons gazeuses")
        api = offapi.ApiRetriever()
        data = api.get_data('Boissons gazeuses')
        for it in data:
            db = update.Storedb()
            liste = db.insert_store(it)
            db.insert_product(it, liste)
