from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import ProductForm, CategoryForm
from django.views.generic import ListView, CreateView
# from .models import Product
from .models import Product, Category, Author, Category, Photo


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product/product_detail.html', {'product': product})


def product_detail_category(request, id, category_id):
    product = get_object_or_404(Product, id=id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'products/product/product_detail.html', {'product': product, 'category': category})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.product_set.all()
    return render(request, 'products/category/category_products.html', {'category': category, 'products': products})


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category/category_list.html'
    context_object_name = 'categories'


def Add_CategoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category/add_category.html', {'form': form})


def productCreate(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        photo = request.FILES.get('photo')

        # Get the Category and Author objects for the foreign keys
        category = Category.objects.get(pk=category_id)
        author = Author.objects.get(pk=author_id)

        # Create a new Product object
        new_product = Product(
            brand=brand,
            model=model,
            price=price,
            description=description,
            category=category,
            author=author
        )

        # Save the new Product object
        new_product.save()

        # Add any uploaded photos to the new Product object
        if photo:
            new_photo = Photo(image=photo)
            new_photo.save()
            new_product.photo.add(new_photo)

        # Redirect to the product detail page for the new product
        return redirect('product_detail', id=new_product.pk)
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'categories': categories,
        'authors': authors
    }
    # Render the form for creating a new product
    return render(request, 'products/product/add_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/product/product_list.html'
    context_object_name = 'products'


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].queryset = Category.objects.all()
    self.fields['author'].queryset = Author.objects.all()
