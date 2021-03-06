from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index_list'),
    path("about-1/", views.AboutView.as_view(), name='about'),
    path("error404/", views.Error404View.as_view(), name='error'),
    path("careers/", views.CareersView.as_view(), name='careers'),
    path("components/lists/", views.ListsView.as_view(), name='list'),
    path("components/maps/", views.MapsView.as_view(), name='map'),
    path("product/", views.ProductsView.as_view(), name='products'),

]
