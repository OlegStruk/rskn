from django.urls import path, include
from rest_framework import routers
from roskomnadzor_api.views import BlockIPAdminView, BlockIPAnonymousView

router = routers.DefaultRouter()
router.register(r"block_ip_admin", BlockIPAdminView, basename="block_ip_admin"),
router.register(r"block_ip_anonymous_request", BlockIPAnonymousView, basename="block_ip_anonymous_request")

urlpatterns = [
    path(r'', include(router.urls))
]
