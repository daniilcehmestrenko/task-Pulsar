from django.urls import path

from .views import ProductDetailAPIView, ProductListAPIView


urlpatterns = [
        path(
            '', ProductListAPIView.as_view(),
            name='product_list'
        ),
        path(
            '<int:pk>', ProductDetailAPIView.as_view(),
            name='product_detail'
        ),
    ]
