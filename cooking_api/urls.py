from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'dish', DishViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls),)
    # path('api/v1/all_dishes', DishesAPIView.as_view(), name='api_dishes'),
    # path('api/v1/dish_detail/<int:pk>/', DishAPIDetail.as_view(), name='api_detail'),
    # path('api/v1/all_dishes/<int:pk>/', DishesAPIView.as_view(), name='update_dish'),
    # path('api/v1/all_dishes/delete/<int:pk>/', DishesAPIView.as_view(), name='delete_dish'),
]
