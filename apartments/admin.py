from django.contrib import admin
from .models import Category, Apartment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "category",
        "city",
        "price",
        "rooms",
        "created_at",
    )

    list_filter = (
        "city",
        "category",
        "rooms",
    )

    search_fields = (
        "title",
        "description",
        "city",
        "address",
    )