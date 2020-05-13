from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from employee.models import Room

# Create your models here.
class Old(User):
    SexType = (
        ("男", "男"),
        ("女", "女"),
    )
    sex = models.CharField('性别', choices=SexType, max_length=2)
    birthday = models.DateField("生日", auto_now=False, auto_now_add=False)
    telephone = models.DecimalField("手机号", max_digits=20, decimal_places=0)
    address = models.CharField("住址", max_length=50)
    room = models.ForeignKey(Room, models.SET_NULL, "olds", null=True, blank=True, default=None)

    class Meta:
        verbose_name = verbose_name_plural = '老人'

    def __str__(self):
        return f"{self.first_name}【{self.username}】"

