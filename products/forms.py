from django import forms
from .models import Product
# forms.py
from django import forms
from .models import Product, Category, Author


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Product
        fields = ('brand', 'model', 'price', 'description', 'category', 'author', 'photo')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)