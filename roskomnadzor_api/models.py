from django.db import models
from django.contrib.auth.models import User


class BlockedIP(models.Model):
    class Meta:
        db_table = "blocked_ips"
        verbose_name = "Blocked IP"
        verbose_name_plural = "Blocked IPs"
        ordering = ["-id"]

    ADMIN_BLOCK = 1
    N_A_BLOCK_REQUEST = 2

    STATUS = (
        (ADMIN_BLOCK, "admin_block"),
        (N_A_BLOCK_REQUEST, "non_auth_block_request"),
    )

    name = models.CharField(max_length=40, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=False, blank=False, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    non_auth_user_ip = models.GenericIPAddressField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.name, str(self.ip_address))
