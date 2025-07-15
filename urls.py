from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TestAPIView, TestViewset, ProductViewSet

router = DefaultRouter()
router.register("test-viewset", TestViewset, basename="test-viewset")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", TestAPIView.as_view()),
    path("", include(router.urls)),
    path("", include(router.urls))
]