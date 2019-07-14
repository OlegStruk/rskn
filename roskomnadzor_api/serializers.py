from rest_framework import serializers
from roskomnadzor_api.models import BlockedIP


class BlockedIPSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = BlockedIP
        fields = "__all__"
        read_only_fields = ("status_display", "non_auth_user_ip", "status", "created_by", "created_at", "updated_at")

    def get_status_display(self, obj):
        return obj.get_status_display()
