from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item
from webapp import views

urlpatterns = {
    path('test/', views.hello_world, name='hello_world'),
    path('db/', manage_items, name="items"),
    path('db/<slug:key>', manage_item, name="single_item"),
    path('pd/', views.product, name="product"),
    path('pd/<slug:product_id>', views.detail, name="single_product"),
    path('cart/', views.cart, name="cart"),
    path('addcart/', views.add_pd, name="add"), 
}
urlpatterns = format_suffix_patterns(urlpatterns)