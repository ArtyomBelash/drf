from django.contrib import admin
from .models import *


class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(DishImage)
admin.site.register(UserAndDishes)
