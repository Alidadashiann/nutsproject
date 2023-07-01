from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView
from django.views import View
from django.http import HttpResponseRedirect

from product.models import Product, ProductVariation
from product.forms import SellerCreateProductForm
from shop.models import SellStatus


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            city=self.request.user.city,
            quantity__gt=0
        )
        return queryset


class ProductSearchView(ListView):
    model = Product
    template_name = "product/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        queryset = queryset.filter(name__contains=search)
        return queryset


class HomePageView(TemplateView):
    template_name = "home.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = SellerCreateProductForm
    template_name = 'product/panel.html'
    success_url = reverse_lazy('product:panel')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class SellerProductListView(LoginRequiredMixin, ListView):
    template_name = "product/panel.html"

    def get_queryset(self):
        queryset = Product.objects.filter(
            product_owner=self.request.user
        ).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SellerCreateProductForm(user=self.request.user)

        sell_status = SellStatus.objects.filter(
            product__product_owner=self.request.user
        )
        context['sells'] = sell_status

        return context

class PostProductView(View):
    def get(self, request, *args, **kwargs):
        sell_status_id = kwargs.get("pk")
        sell_status = SellStatus.objects.get(id=sell_status_id)
        sell_status.status = "S"
        sell_status.save()
        return HttpResponseRedirect(reverse_lazy('product:panel'))
