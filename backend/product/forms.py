from django import forms

from product.models import Product


class SellerCreateProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['product_owner'].initial = user
        self.fields['city'].initial = user.city

    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'quantity', 'type', 'product_owner', 'city']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name', 'aria-describedby': 'usernameHelp', 'placeholder': 'نام محصول خود را وارد کنید', 'type': 'text', "name": 'name'}),
            'price': forms.NumberInput(attrs={'min': 0, 'class': 'form-control', 'id': 'exampleInputPrice', 'aria-describedby': 'emailHelp', 'placeholder': 'قیمت محصولات'}),
            'quantity': forms.NumberInput(attrs={'min': 0, 'class': 'form-control', 'id': 'exampleInputQuantity', 'placeholder': 'تعداد محصولات'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputType', 'aria-describedby': 'typeHelp', 'placeholder': 'نوع محصول خود را وارد کنید'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control', 'id': 'formFile', 'aria-describedby': 'typeHelp', 'placeholder': 'عکس محصول خود را انتخاب کنید', 'type': 'file'}),

            'product_owner': forms.HiddenInput(),
            'city': forms.HiddenInput(),
        }