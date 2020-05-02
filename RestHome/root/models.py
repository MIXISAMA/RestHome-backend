from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

# Create your models here.

class Root(User):

    telephone = models.DecimalField("手机号", max_digits=20, decimal_places=0)

    class Meta:
        verbose_name = verbose_name_plural = '管理员'

    def __str__(self):
        return f"{self.first_name}【{self.username}】"

# @receiver(post_save, sender=User, dispatch_uid="创建之后要自动生成令牌")
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)