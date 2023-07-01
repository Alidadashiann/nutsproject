from django.urls import path

from product.views import (
    ProductListView,
    HomePageView,
    ProductSearchView,
    SellerProductListView,
    ProductCreateView,
    PostProductView,
)


app_name = "product"

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('search/', ProductSearchView.as_view(), name="search"),
    path('', HomePageView.as_view(), name="home"),
    path('panel/', SellerProductListView.as_view(), name="panel"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('post/<int:pk>/', PostProductView.as_view(), name="post"),
]
