from django.shortcuts import render, redirect # here by default
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True, min_value=0.01)

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
        # Aquí podrías guardar el producto si estuvieras usando un modelo
            return redirect(reverse('index'))  # Redirige a la lista de productos
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price":"1000"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"1000"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"1000"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"1000"}
]
    
class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    

class ProductShowView(View):
    template_name = 'products/show.html'
    
    def get(self, request, id):
        viewData = {}
        # Verificar si el id es válido
        if int(id) < 1 or int(id) > len(Product.products):
            # Redireccionar a la página de inicio si el id no es válido
            return HttpResponseRedirect(reverse('home'))

        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        viewData["price"] = float(product["price"])
        return render(request, self.template_name, viewData)

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "address": "Calle 99 # 10 -11",
            "email": "pedro@eafit.edu.co",
            "phone": "309293021",
        })
        return context