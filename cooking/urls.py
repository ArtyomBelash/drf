from django.urls import path
from .views import *

urlpatterns = [
    path('', DishesListView.as_view(), name='index'),
    path('dish/<slug:slug>/', DishDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('search/', SearchDishesView.as_view(), name='search'),
    path('random_dish/', RandomDishView.as_view(), name='random'),
]
