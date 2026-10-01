from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="apartments"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="apartments"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    rooms = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to="apartments/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title