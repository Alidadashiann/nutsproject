from django.urls import path

from account.views import (
    UserRegistrationView,
    UserLoginView,
    AboutUsView,
    RestPasswordView,
    SellerRegistrationView,
    CustomLogoutView,
)


app_name = 'account'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('register/seller/', SellerRegistrationView.as_view(), name="register-seller"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('about-us/', AboutUsView.as_view(), name="about-us"),
    path('rest-password/', RestPasswordView.as_view(), name="rest-password"),
]
