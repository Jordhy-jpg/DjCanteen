from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from .models import Category, Detail, Product


class AddProductTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Lunch")
        self.data = {
            "category": category.pk,
            "name": "Rice bowl",
            "price": "25000.00",
            "stock": "5",
            "calories": "320.50",
            "ingredients": "Rice, vegetables",
        }

    def test_creates_product_with_details(self):
        response = self.client.post(reverse("add_product"), self.data)

        self.assertEqual(response.headers["HX-Location"], reverse("products_index"))
        product = Product.objects.get()
        self.assertEqual(product.details.ingredients, "Rice, vegetables")
        self.assertEqual(str(product.details.calories), "320.50")
        self.assertEqual(Detail.objects.count(), 1)

    def test_invalid_forms_report_both_errors_without_saving(self):
        self.data.update(name="", calories="")
        response = self.client.post(reverse("add_product"), self.data)

        self.assertContains(response, "name")
        self.assertContains(response, "calories")
        self.assertNotIn("HX-Location", response.headers)
        self.assertFalse(Product.objects.exists())
        self.assertFalse(Detail.objects.exists())

    def test_invalid_details_do_not_create_product(self):
        self.data["calories"] = "invalid"
        self.client.post(reverse("add_product"), self.data)

        self.assertFalse(Product.objects.exists())
        self.assertFalse(Detail.objects.exists())

    def test_ingredients_are_optional(self):
        self.data["ingredients"] = ""
        response = self.client.post(reverse("add_product"), self.data)

        self.assertIn("HX-Location", response.headers)
        self.assertEqual(Detail.objects.count(), 1)

    def test_detail_save_failure_rolls_back_product(self):
        with patch.object(Detail, "save", side_effect=RuntimeError("Save failed")):
            with self.assertRaises(RuntimeError):
                self.client.post(reverse("add_product"), self.data)

        self.assertFalse(Product.objects.exists())
        self.assertFalse(Detail.objects.exists())

    def test_modal_includes_detail_fields(self):
        response = self.client.get(reverse("products_index"))

        self.assertContains(response, 'name="calories"')
        self.assertContains(response, 'name="ingredients"')
