from django.db.models import Count, Case, When, Avg
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Dish, Category, UserAndDishes
from .pagination import DefaultPagination
from .serializers import DishSerializer, CategorySerializer, UserSerializer, RelationSerializer
from .permissions import IsAdminOrReadOnly
import random


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().select_related('cat').annotate(rating=Avg('useranddishes__rate'),
                                                                 likes_count=Count(Case(
                                                                     When(useranddishes__like=True, then=1))))
    serializer_class = DishSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'

    # pagination_class = DefaultPagination

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = Category.objects.all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def category(self, request, slug=None):
        cat = Category.objects.get(slug=slug)
        dishes = Dish.objects.filter(cat=cat).select_related('cat').annotate(rating=Avg('useranddishes__rate'),
                                                                             likes_count=Count(Case(
                                                                                 When(useranddishes__like=True,
                                                                                      then=1))))
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def search_dishes(self, request):
        if self.request.method == 'GET':
            search_query = self.request.GET.get('search').lower()
            dishes = Dish.objects.filter(title__regex=fr'(?i){search_query}').select_related('cat').annotate(
                rating=Avg('useranddishes__rate'),
                likes_count=Count(Case(
                    When(useranddishes__like=True, then=1))))
            if dishes:
                return Response(DishSerializer(dishes, many=True).data)
            return Response([{'error': 'Nothing. Change search term'}])

    @action(methods=['get'], detail=True)
    def random_dish(self, request, slug=None):
        length = len(self.queryset)
        pk = random.randint(1, length)
        dish = Dish.objects.get(pk=pk)
        return Response(DishSerializer(dish).data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RelationAPIViewSet(UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserAndDishes.objects.all()
    serializer_class = RelationSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'dish'

    def get_object(self):
        obj, _ = UserAndDishes.objects.get_or_create(user_id=self.request.user.id, dish_id=self.kwargs['dish'])
        return obj

# class DishesAPIView(generics.ListCreateAPIView):
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#
#
# def post(self, request):
#     serializer = DishSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     new_dish = Dish.objects.create(
#         title=request.data['title'],
#         recipe=request.data['recipe'],
#         cat_id=request.data['cat_id']
#     )
#     return Response({'post': DishSerializer(new_dish).data})
#     serializer.save()
#     return Response({'dish': serializer.data})
#
#
# def put(self, request, *args, **kwargs):
#     pk = kwargs.get('pk', None)
#     if not pk:
#         return Response({'error': 'Method PUT not allowed'})
#     try:
#         instance = Dish.objects.get(pk=pk)
#     except TypeError:
#         return Response({'error': 'Object does not exist'})
#     serializer = DishSerializer(data=request.data, instance=instance)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response({'dish': serializer.data})
#
#
# def delete(self, request, *args, **kwargs):
#     pk = kwargs.get('pk', None)
#     if not pk:
#         return Response({'error': 'Method DELETE not allowed'})
#     try:
#         instance = Dish.objects.get(pk=pk)
#     except (TypeError, AttributeError):
#         return Response({'error': 'Object does not exist'})
#     instance.delete()
#     return Response({'dish': f'Delete object {pk}'})
