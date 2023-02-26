from django.urls import include, path
from guestapi.urls import urlpatterns as guestapi_urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(guestapi_urls))
]