from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from roskomnadzor_api.heplers import Helper
from roskomnadzor_api.models import BlockedIP
from roskomnadzor_api.permissions import IsAnonymous
from roskomnadzor_api.serializers import BlockedIPSerializer


class BlockIPAdminView(viewsets.ModelViewSet):
    queryset = BlockedIP.objects.all()
    serializer_class = BlockedIPSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ["get", "post", "head", "put", "delete"]

    @atomic
    def perform_create(self, serializer):
        super().perform_create(serializer.save(created_by=self.request.user, status=BlockedIP.ADMIN_BLOCK))


class BlockIPAnonymousView(viewsets.ModelViewSet):
    queryset = BlockedIP.objects.all()
    serializer_class = BlockedIPSerializer
    permission_classes = (IsAnonymous,)
    http_method_names = ["post"]

    @atomic
    def perform_create(self, serializer):
        super().perform_create(
            serializer.save(status=BlockedIP.N_A_BLOCK_REQUEST, non_auth_user_ip=Helper.get_user_ip(self.request)))
