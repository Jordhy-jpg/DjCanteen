from django.core.management.base import BaseCommand
from django.db import transaction

from catalogue.models import Category, Detail, Product


class Command(BaseCommand):
    help = "Create or update sample catalogue categories, products, and details."

    @transaction.atomic
    def handle(self, *args, **options):
        catalogue = [
            (
                "Meals",
                "Main meals prepared in the canteen.",
                [
                    ("Fried Rice", "Rice fried with vegetables and egg.", "15000.00",
                     "550.00", "Rice, egg, carrot, spring onion, soy sauce, cooking oil"),
                    ("Chicken Noodles", "Noodles topped with seasoned chicken.", "18000.00",
                     "480.00", "Wheat noodles, chicken, bok choy, soy sauce, garlic"),
                    ("Chicken Fried Rice", "Fried rice with chicken and vegetables.", "20000.00",
                     "620.00", "Rice, chicken, egg, carrot, soy sauce, cooking oil"),
                    ("Vegetable Fried Noodles", "Stir-fried noodles with mixed vegetables.", "15000.00",
                     "420.00", "Wheat noodles, cabbage, carrot, bok choy, soy sauce"),
                    ("Chicken Satay", "Grilled chicken skewers served with rice.", "25000.00",
                     "650.00", "Chicken, rice, peanuts, sweet soy sauce, shallot"),
                ],
            ),
            (
                "Snacks",
                "Light bites between meals.",
                [
                    ("Fried Tempeh", "Crispy battered tempeh.", "5000.00",
                     "200.00", "Soybean tempeh, wheat flour, garlic, coriander, cooking oil"),
                    ("Banana Fritters", "Sweet bananas fried in a light batter.", "7000.00",
                     "250.00", "Banana, wheat flour, rice flour, sugar, cooking oil"),
                    ("Vegetable Spring Rolls", "Crispy rolls filled with vegetables.", "8000.00",
                     "220.00", "Spring roll wrappers, cabbage, carrot, bean sprouts, cooking oil"),
                    ("Stuffed Tofu", "Fried tofu filled with seasoned vegetables.", "6000.00",
                     "180.00", "Tofu, carrot, cabbage, wheat flour, garlic, cooking oil"),
                    ("Potato Fritters", "Golden potato patties with herbs.", "6000.00",
                     "210.00", "Potato, egg, celery, shallot, pepper, cooking oil"),
                ],
            ),
            (
                "Drinks",
                "Refreshing drinks to accompany your meal.",
                [
                    ("Iced Tea", "Freshly brewed sweet iced tea.", "5000.00",
                     "80.00", "Black tea, sugar, water, ice"),
                    ("Orange Juice", "Freshly squeezed orange juice.", "10000.00",
                     "110.00", "Orange, water, ice"),
                    ("Lime Iced Tea", "Sweet iced tea with fresh lime.", "7000.00",
                     "90.00", "Black tea, lime, sugar, water, ice"),
                    ("Avocado Juice", "Creamy blended avocado drink.", "15000.00",
                     "280.00", "Avocado, milk, condensed milk, water, ice"),
                    ("Mineral Water", "Bottled drinking water.", "4000.00",
                     "0.00", "Mineral water"),
                ],
            ),
            (
                "Desserts",
                "Sweet treats to finish your meal.",
                [
                    ("Chocolate Pudding", "Smooth chilled chocolate pudding.", "10000.00",
                     "190.00", "Milk, cocoa powder, sugar, cornstarch"),
                    ("Fruit Salad", "Mixed fresh fruit with a creamy dressing.", "12000.00",
                     "180.00", "Apple, melon, grape, yogurt, condensed milk"),
                    ("Coconut Jelly", "Chilled coconut milk jelly.", "8000.00",
                     "140.00", "Coconut milk, agar, sugar, water"),
                    ("Black Rice Pudding", "Sweet black rice with coconut milk.", "10000.00",
                     "260.00", "Black glutinous rice, coconut milk, palm sugar, pandan"),
                    ("Steamed Banana Cake", "Soft banana cake steamed until fluffy.", "9000.00",
                     "230.00", "Banana, wheat flour, egg, sugar, cooking oil"),
                ],
            ),
            (
                "Breakfast",
                "Morning favourites to start your day.",
                [
                    ("Chicken Porridge", "Rice porridge topped with shredded chicken.", "12000.00",
                     "350.00", "Rice, chicken, chicken broth, spring onion, fried shallot"),
                    ("Egg Sandwich", "Toasted bread with egg and vegetables.", "12000.00",
                     "320.00", "Bread, egg, lettuce, tomato, mayonnaise"),
                    ("Peanut Butter Toast", "Crisp toast spread with peanut butter.", "8000.00",
                     "290.00", "Bread, peanut butter, butter"),
                    ("Vegetable Omelette", "Egg omelette with fresh vegetables.", "10000.00",
                     "240.00", "Egg, carrot, spring onion, tomato, cooking oil"),
                    ("Coconut Rice", "Fragrant coconut rice with egg and tempeh.", "15000.00",
                     "520.00", "Rice, coconut milk, egg, tempeh, cucumber, sambal"),
                ],
            ),
        ]

        for category_name, description, products in catalogue:
            category, _ = Category.objects.update_or_create(
                name=category_name,
                defaults={"description": description},
            )

            for name, description, price, calories, ingredients in products:
                product, _ = Product.objects.update_or_create(
                    category=category,
                    name=name,
                    defaults={"description": description, "price": price},
                )
                Detail.objects.update_or_create(
                    product=product,
                    defaults={"calories": calories, "ingredients": ingredients},
                )

        self.stdout.write(self.style.SUCCESS(
            "Catalogue seeded: 5 categories, 25 products, and 25 details."
        ))
