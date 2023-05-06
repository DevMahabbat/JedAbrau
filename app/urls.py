from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("contact", views.contact, name="contact"),
    path("news",views.news,name='news'),
    path("newssingle/<int:id>",views.newsSingle,name="newsSingle"),
    path("products",views.products,name="products"),
    path("product/<int:id>",views.productSingle,name="productsingle"),
    path("maps",views.maps,name="maps"),
]
