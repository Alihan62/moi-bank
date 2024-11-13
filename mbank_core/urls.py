"""
URL configuration for mbank_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mbank.views import AddMoneyView, LoginPageView, MakeLoginView , ProfilePageView, RegistrationPageView, MakeRegistrationPageView, TransactionPageView, MakeTransactionView, MakeMoneyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-money/', AddMoneyView.as_view(), name='add-money-url'),
    path('make-money/', MakeMoneyView.as_view(), name='mk-mn'),
    path('login/', LoginPageView.as_view()),
    path('make-login/', MakeLoginView.as_view(), name='mk-ln'),
    path('profile/', ProfilePageView.as_view(), name='profile-url'),
    path('registration/', RegistrationPageView.as_view()),
    path('make_registration/', MakeRegistrationPageView.as_view(), name='mk-rg'),
    path('transaction/', TransactionPageView.as_view(), name='transaction-url'),
    path('make-transaction/', MakeTransactionView.as_view(), name='mk-tr'),
]
