from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

person_router = DefaultRouter()
address_router = DefaultRouter()

person_router.register('', views.PersonViewSetApiView, basename='person_view')
# address_router.register('', views.AddressViewSetApiView, basename='address_view')

# Include the router URLs in your main URL configuration
urlpatterns = [
    path('person/', include(person_router.urls)),
    # path('address/', include(address_router.urls)),
]
