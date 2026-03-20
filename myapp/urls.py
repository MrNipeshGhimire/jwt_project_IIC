from django.urls import path
from .views.auth_view import register_view,login_view
from .views.main_view import product_view

urlpatterns = [
    path('register/',register_view),
    path('login/',login_view),
    path('product/', product_view)
]
