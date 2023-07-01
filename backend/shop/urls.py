from django.urls import path

from shop.views import (
    AddProductToCart,
    CartListView,
    PayCartView,
    DecreaseProductQuantity,
    IncreaseProductQuantity,
)


app_name = "shop"

urlpatterns = [
    path('add-to-cart/<int:pk>/', AddProductToCart.as_view(), name='add-to-cart'),
    path('cart/', CartListView.as_view(), name='list'),
    path('pay/', PayCartView.as_view(), name='pay'),

    path('increase-quantity/<int:pk>/', IncreaseProductQuantity.as_view(), name='increase_quantity'),
    path('decrease-quantity/<int:pk>/', DecreaseProductQuantity.as_view(), name='decrease_quantity'),
]