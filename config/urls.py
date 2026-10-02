"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from apartments.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apartments.views import (
    ApartmentViewSet,
    CategoryViewSet,
    RegisterView,
    BookingViewSet,
    ReviewViewSet,
)   
from apartments.views import ApartmentViewSet, CategoryViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apartments.views import (
    ApartmentViewSet,
    CategoryViewSet,
    RegisterView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Apartment Rental API",
        default_version="v1",
        description="API для сервиса аренды квартир",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()

router.register("apartments", ApartmentViewSet)
router.register("categories", CategoryViewSet)
router.register("bookings", BookingViewSet, basename="booking")
router.register("reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include(router.urls)),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),
    path("api/register/", RegisterView.as_view()),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/login/", LoginView.as_view()),
    path("api/logout/", LogoutView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

