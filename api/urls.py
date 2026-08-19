from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LoginView,
    RegisterView,
    ProfileView,
    SensorReadingViewSet,
    DeviceViewset
)

router = DefaultRouter()
router.register(r'devices', DeviceViewset)
router.register(r'readings', SensorReadingViewSet)

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(),
    ),
    path(
        "register/",
        RegisterView.as_view(),
    ),
    path(
        "profile/",
        ProfileView.as_view(),
    )
] + router.urls