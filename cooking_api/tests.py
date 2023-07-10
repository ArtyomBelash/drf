from django.urls import reverse
from rest_framework.test import APITestCase

from cooking_api.models import Dish, Category
from cooking_api.serializers import DishSerializer


class TestDishAPI(APITestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='fff', slug='fff')
        self.dish = Dish.objects.create(
            title='aaa', recipe='bbbb', cat_id=1, slug='aaa')

    def test_retrieve_dish(self):
        url = reverse('dish-detail', args=[self.dish.slug])
        response = self.client.get(url)
        serializer_data = DishSerializer(self.dish).data
        self.assertEqual(serializer_data, response.data)
