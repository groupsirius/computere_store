from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# models.py
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Photo(models.Model):
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)

    def __str__(self):
        return self.image.name


class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model}'
