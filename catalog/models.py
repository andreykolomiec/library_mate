from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name

class Author(AbstractUser):
    pseudonym = models.CharField(max_length=63, null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="author_groups",  # Унікальна назва
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="author_permissions",  # Унікальна назва
        blank=True
    )

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("catalog:author-detail", kwargs={"pk": self.pk})


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat, on_delete=models.CASCADE,
        related_name="books",
    )
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="books")

    class Meta:
        ordering = ("title", )

    def __str__(self):
        return f"{self.title} (price: {self.price}, format: {self.format.name})"


    # створення URL-адрес (посилання на конкретну книгу) в коді за допомогою функції reverse:

    def get_absolute_url(self):
        return reverse("catalog:book-detail", args=[str(self.id)])
