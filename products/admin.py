from django.contrib import admin
from .models import Category, Author, Product, Photo

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Photo)
