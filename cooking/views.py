from datetime import datetime

import requests
from django.views import generic
from config_drf import settings


class DishesListView(generic.ListView):
    template_name = 'cooking/index.html'
    paginate_by = 3
    context_object_name = 'dishes'

    def get_queryset(self):
        url = settings.URL
        response = requests.get(url)
        dishes = response.json()
        for dish in dishes:
            dish['created'] = datetime.strptime(dish['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        return dishes

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     url = settings.URL
    #     response = requests.get(url)
    #     context['dishes'] = response.json()
    #     for dish in context['dishes']:
    #         dish['created'] = datetime.strptime(dish['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
    #     return context


class DishDetailView(generic.DetailView):
    template_name = 'cooking/detail.html'
    context_object_name = 'dish'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        url = settings.URL + slug
        response = requests.get(url)
        dish = response.json()
        dish['created'] = datetime.strptime(dish['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        return dish


class CategoryListView(generic.ListView):
    paginate_by = 2
    template_name = 'cooking/category_list.html'
    queryset = None
    context_object_name = 'dishes_by_category'

    def get_queryset(self):
        slug = self.kwargs['slug']
        url = settings.URL + slug + '/category'
        response = requests.get(url)
        dishes_by_category = response.json()
        for dish in dishes_by_category:
            dish['created'] = datetime.strptime(dish['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        print(dishes_by_category)
        return dishes_by_category


class SearchDishesView(generic.ListView):
    template_name = 'cooking/search_list.html'
    context_object_name = 'dishes_by_search'
    paginate_by = 1

    def get_queryset(self):
        url = f'{settings.URL}search_dishes/?search={self.request.GET.get("search")}'
        response = requests.get(url)
        dishes_by_search = response.json()
        for dish in dishes_by_search:
            dish['created'] = datetime.strptime(dish['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        return dishes_by_search


class RandomDishView(generic.TemplateView):
    template_name = 'cooking/random_dish.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        url = f'{settings.URL}1/random_dish/'
        response = requests.get(url)
        context['dish'] = response.json()
        context['dish']['created'] = datetime.strptime(context['dish']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        return context
