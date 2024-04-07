from django.core.management import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удалите все продукты
        Category.objects.all().delete()
        # Удалите все категории
        Product.objects.all().delete()

        products_list = [
            [
                {
                    "product_name": "Personal Computer",
                    "product_description": "Description of Computers Product",
                    "product_category": "Computers",
                    "product_price": 95678
                },
                {
                    "product_name": "Toaster",
                    "product_description": "Description of Electronics Product",
                    "product_category": "Electronics",
                    "product_price": 3491
                },
                {
                    "product_name": "Blue Jeans",
                    "product_description": "Description of Clothing Product",
                    "product_category": "Clothing",
                    "product_price": 2200
                },
                {
                    "product_name": "Game Of Thrones",
                    "product_description": "Description of Books Product",
                    "product_category": "Books",
                    "product_price": 589
                },
                {
                    "product_name": "Candle",
                    "product_description": "Description of Home Decor Product",
                    "product_category": "Home Decor",
                    "product_price": 785
                },
                {
                    "product_name": "Bicycle",
                    "product_description": "Description of Sports Product",
                    "product_category": "Sports",
                    "product_price": 14398
                },
                {
                    "product_name": "Pokemon",
                    "product_description": "Description of Toys Product",
                    "product_category": "Toys",
                    "product_price": 429
                },
                {
                    "product_name": "Concealer",
                    "product_description": "Description of Beauty Product",
                    "product_category": "Beauty",
                    "product_price": 1350
                },
                {
                    "product_name": "Gaming Chair",
                    "product_description": "Description of Furniture Product",
                    "product_category": "Furniture",
                    "product_price": 12000
                },
                {
                    "product_name": "Bread",
                    "product_description": "Description of Food Product",
                    "product_category": "Food",
                    "product_price": 70
                }
            ]

        ]
        categories_list = [
            {"category_name": "Computers", "category_description": "Computers and peripherals"},
            {"category_name": "Electronics", "category_description": "Electronic devices and accessories"},
            {"category_name": "Clothing", "category_description": "Clothing and apparel"},
            {"category_name": "Books", "category_description": "Books and literature"},
            {"category_name": "Home Decor", "category_description": "Home decoration and accessories"},
            {"category_name": "Sports", "category_description": "Sports equipment and gear"},
            {"category_name": "Toys", "category_description": "Toys and games for children"},
            {"category_name": "Beauty", "category_description": "Beauty products and cosmetics"},
            {"category_name": "Furniture", "category_description": "Furniture and furnishings"},
            {"category_name": "Food", "category_description": "Food and beverages"},
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        for product in products_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_for_create)
