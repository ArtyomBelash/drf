from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dish, DishImage, Category, UserAndDishes


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = ('image',)


class DishSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()  # вложенный сериализатор для категории
    images = DishImageSerializer(many=True)  # вложенный сериализатор для изображений
    likes_count = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        model = Dish
        fields = ('id', 'title', 'recipe', 'created', 'cat', 'images', 'slug', 'likes_count', 'rating')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class RelationSerializer(serializers.ModelSerializer):
    name_of_dish = serializers.CharField(source='dish.title', read_only=True)

    class Meta:
        model = UserAndDishes
        fields = ('name_of_dish', 'like', 'rate')

    def create(self, validated_data):
        return UserAndDishes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dish = validated_data.get('dish', instance.dish)
        instance.like = validated_data.get('like', instance.like)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance

# class DishSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=155)
#     recipe = serializers.CharField()
#     created = serializers.DateTimeField(read_only=True)
#     cat_id = serializers.IntegerField()
#     images = serializers.PrimaryKeyRelatedField(many=True, queryset=DishImage.objects.all())
#
#     def create(self, validated_data):
#         dish = Dish.objects.create(title=validated_data['title'],
#                                    recipe=validated_data['recipe'],
#                                    cat_id=validated_data['cat_id'], )
#         images = validated_data['images']
#         dish.images.set(images)
#         return dish
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.recipe = validated_data.get('recipe', instance.recipe)
#         instance.created = validated_data.get('created', instance.created)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         images = validated_data.get('images', instance.images)
#         instance.images.set(images)
#         instance.save()
#         return instance
#
#     def delete(self, instance):
#         instance.delete()
#         return instance
