from django.urls import path

#from .views import posts,home,post,create_post,edit_post, delete_post

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.home, name='product_home'),
    path('search', views.search_product, name='product_search'),
    path('category/<int:idCategory>', views.filter_by_category, name='product_filter_category'),
    path('price/<int:asc>', views.filter_by_price, name='product_filter_price')
]
