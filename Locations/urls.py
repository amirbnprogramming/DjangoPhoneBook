from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

country_router = DefaultRouter()
state_router = DefaultRouter()
city_router = DefaultRouter()

country_router.register('', views.CountryViewSetApiView, basename='country_view')
state_router.register('', views.StateViewSetApiView, basename='state_view')
city_router.register('', views.CityViewSetApiView, basename='city_view')

# Include the router URLs in your main URL configuration
urlpatterns = [
    path('country/', include(country_router.urls)),
    path('state/', include(state_router.urls)),
    path('city/', include(city_router.urls)),
]
