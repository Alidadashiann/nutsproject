from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView

from account.forms import UserRegistrationForm, EmailForm, UserLoginForm, SellerRegistrationForm
from account.models import User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('account:login')


class SellerRegistrationView(CreateView):
    model = User
    form_class = SellerRegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('account:login')


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('product:home')


class RestPasswordView(View):

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        return render(request, 'account/rest_password.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error(field='email', error='user dose not exists!')
                return render(request, 'account/rest_password.html', {'form': form})

            new_password = user.rest_password()
            message = "کاربر گرامی, \n" \
                    "درخواست بازیابی گذرواژه توسط شما ارسال شده.\n" \
                    "در صورتی که این درخواست توسط شما ارسال نشده، آن را نادیده بگیرید.\n" \
                    f" گذرواژه جدید شما : \n{new_password}" 

            send_mail(
                subject="rest password ",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
            return redirect('account:login')
        else:
            return render(request, 'account/rest_password.html', {'form': form})


class AboutUsView(TemplateView):
    template_name = "about_us.html"


class CustomLogoutView(LogoutView):
    next_page = '/'
