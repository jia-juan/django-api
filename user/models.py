from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    # 解決 auth.user 與 user.user 對於相同屬性的命名衝突問題
    groups = models.ManyToManyField(
        Group,
        related_name='user_set',  # 添加 related_name 参数
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_set',  # 添加 related_name 参数
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    # Attributes to add ...
    # pass
