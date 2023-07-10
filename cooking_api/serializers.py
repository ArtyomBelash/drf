from rest_framework import serializers

from .models import Dish, DishImage, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', )


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = ('image',)


class DishSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()  # вложенный сериализатор для категории
    images = DishImageSerializer(many=True)  # вложенный сериализатор для изображений

    class Meta:
        model = Dish
        fields = ('id', 'title', 'recipe', 'created', 'cat', 'images', 'slug')

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
