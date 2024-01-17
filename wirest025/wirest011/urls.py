"""wirest011 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from testapp import views as v1
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('api',v1.EmployeeCRUDCBV)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/',include('rest_framework.urls')),
    path('',include(router.urls)),
    path('auth-jwt/',TokenObtainPairView.as_view()),
    path('auth-jwt-refresh/',TokenRefreshView.as_view()),
    path('auth-jwt-verify/',TokenVerifyView.as_view()),
    # path('api/',views.EmployeeListCreateModelMixin.as_view()),
    # path('api/<int:pk>',views.EmployeeRetrieveUpdateDestroyModelMixin.as_view()),
    # path('api/<int:pk>',views.EmployeeRetriveAPIView.as_view()),
    # path('api/<int:pk>',views.EmployeeUpdateAPIView.as_view()),
    # path('api/<int:pk>',views.EmployeeDestroyAPIView.as_view()),
]
