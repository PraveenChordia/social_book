from django.urls import path, include
from django.contrib import admin
from .views import login_view, register_view, logout_view
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("admin/", admin.site.urls),
    path("signin", login_view, name="login"),
    path('register', register_view, name="register"),
    path('logout', logout_view, name="logout"),
]
