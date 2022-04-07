from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product
# from backend.apps.cart.cart import Cart


class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     cart = Cart(self.request)
    #
    #     context['categories'] = Category.objects.all()
    #     context['cart'] = cart
    #     return context


class AboutView(TemplateView):
    template_name = "about-1.html"


class CareersView(TemplateView):
    template_name = "careers.html"


class CartView(TemplateView):
    template_name = "cart.html"


class Error404View(TemplateView):
    template_name = "404.html"


class ListsView(TemplateView):
    template_name = "components/lists.html"


class MapsView(TemplateView):
    template_name = "components/maps.html"


class ProductsView(ListView):
    model = Product
    template_name = "menu-grid.html"
    context_object_name = 'products_grid'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
