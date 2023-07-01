from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from account.models import User
from city.models import City


class UserRegistrationForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'id': 'exampleInputCity', 'class': 'form-control', 'aria-describedby': 'cityHelp'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'city', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputFirstName', 'aria-describedby': 'firstnameHelp', 'placeholder': 'نام خود را وارد کنید'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputLastName', 'aria-describedby': 'lastnameHelp', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputUsername', 'aria-describedby': 'usernameHelp', 'placeholder': 'نام کاربری خود را وارد کنید'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'exampleInputEmail', 'aria-describedby': 'emailHelp', 'placeholder': 'ایمیل خود را وارد کنید'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputPassword', 'placeholder': 'رمز ورود'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = 'انتخاب شهر'
        self.fields['username'].error_messages['unique'] = 'نام کاربری تکراری است'


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
            self.add_error('email', 'مخاطب وجود دارد')
        except User.DoesNotExist: ...

        return cleaned_data


class SellerRegistrationForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'id': 'exampleInputCity', 'class': 'form-control', 'aria-describedby': 'cityHelp', 'placeholder': 'شهر', }))
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='S')

    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'username', 'email', 'city', 'user_type', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputFirstName', 'aria-describedby': 'firstnameHelp', 'placeholder': 'نام خود را وارد کنید'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputLastName', 'aria-describedby': 'lastnameHelp', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputUsername', 'aria-describedby': 'usernameHelp', 'placeholder': 'نام کاربری خود را وارد کنید'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'exampleInputEmail', 'aria-describedby': 'emailHelp', 'placeholder': 'ایمیل خود را وارد کنید'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputPassword', 'placeholder': 'رمز ورود'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = 'انتخاب شهر'
        self.fields['username'].error_messages['unique'] = 'نام کاربری تکراری است'


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
            self.add_error('email', 'مخاطب وجود دارد')
        except User.DoesNotExist: ...

        return cleaned_data


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'email', 'id': 'exampleInputEmail', 'aria-describedby': 'emailHelp', 'placeholder':  ' ایمیل خود را وارد کنید'}
        ),
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('ایمیل شما وجود ندارد‍')

        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'exampleInputUsername', 'aria-describedby': 'usernameHelp', 'placeholder': 'نام کاربری خود را وارد کنید'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'id': 'exampleInputPassword1', 'placeholder': 'رمز ورود'}
        )
    )

    error_messages = {
        "invalid_login": "مشخصات ورود اشتباه است",
        "inactive": "این اکانت اجازه فعالیت ندارد",
    }
