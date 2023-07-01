from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from shop.models import Cart, SellStatus
from product.models import Product


class AddProductToCart(View):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        product = Product.objects.get(id=kwargs.get("pk"))
        cart_item, created = Cart.objects.get_or_create(
            user=user, product=product,
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return HttpResponseRedirect(reverse_lazy('product:list'))


class CartListView(LoginRequiredMixin, ListView):
    template_name = "shop/list.html"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class PayCartView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user)
        error_products = []

        for cart_item in cart_items:
            product = cart_item.product
            if product.quantity >= cart_item.quantity:
                product.quantity -= cart_item.quantity
                product.save()

                SellStatus.objects.update_or_create(
                    product=cart_item.product,
                    user=cart_item.user,
                    quantity=cart_item.quantity,
                )

            else:
                error_products.append(product)

        cart_items.delete()
        if error_products:
            return render(request, 'shop/list.html', {'error_products': error_products})

        return HttpResponseRedirect(reverse_lazy('product:list'))


class DecreaseProductQuantity(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        product_id = kwargs.get("pk")
        cart_item = get_object_or_404(Cart, user=user, product__id=product_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return HttpResponseRedirect(reverse_lazy('shop:list'))


class IncreaseProductQuantity(AddProductToCart):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        product_id = id=kwargs.get("pk")

        print(f'{product_id}')
        
        cart_item = get_object_or_404(Cart, user=user, product__id=product_id)
        cart_item.quantity += 1
        cart_item.save()

        return HttpResponseRedirect(reverse_lazy('shop:list'))

