from django.urls import include, path
from guestapi.urls import urlpatterns as guestapi_urls
from webapp.urls import urlpatterns as webapp_urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(guestapi_urls)),
    path('', include(webapp_urls))
]