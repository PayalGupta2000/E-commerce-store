from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('signin/', views.SigninAPIView.as_view(), name='signin'),
    path('signout/', views.SignoutAPIView.as_view(), name='signout'),
    path('products/',views.ProductListAPIView.as_view(),name="product-list"),
    path('orders/', views.OrderCreateAPIView.as_view(), name='order-create'),
]

