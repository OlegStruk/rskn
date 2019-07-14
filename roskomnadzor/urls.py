from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'get_token/', obtain_jwt_token),
    path(r'', include('roskomnadzor_api.urls'))
]
