from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from old.models import Old

# Create your models here.

class Position(models.Model):
    name = models.CharField('职称', max_length=16, primary_key=True)

    class Meta:
        verbose_name = verbose_name_plural = '职位'

    def __str__(self):
        return self.name

class Emp(models.Model):
    SexType = (
        ("男", "男"),
        ("女", "女"),
    )
    position = models.ForeignKey(Position, models.SET_NULL, null=True, blank=True, verbose_name="职位")
    user = models.OneToOneField(User, models.CASCADE, verbose_name="账户", primary_key=True)
    name = models.CharField('姓名', max_length=8)
    sex = models.CharField('性别', choices=SexType, max_length=2)
    birthday = models.DateField("生日", auto_now=False, auto_now_add=False)
    telephone = models.DecimalField("手机号", max_digits=20, decimal_places=0)
    address = models.CharField("住址", max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = '职员'

    def __str__(self):
        return f"{self.name}【{self.username}】"

    @property
    def username(self):
        return self.user.username

class Room(models.Model):
    id = models.CharField('房间号', max_length=8, primary_key=True)
    emp = models.ForeignKey(Emp, models.SET_NULL, verbose_name="负责职员", null=True, blank=True)
    old = models.ForeignKey(Old, models.SET_NULL, verbose_name="入住老人", null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '房间'

    def __str__(self):
        return self.id

# class Fin(models.Model):
#     # id = models.CharField('财务报表号', max_length=32, primary_key=True)
#     year = models.IntegerField("年")
#     month = models.IntegerField("月")
#     money = models.DecimalField("金额", max_digits=32, decimal_places=4)

#     class Meta:
#         verbose_name = verbose_name_plural = '财务报表'

#     def __str__(self):
#         return f"{self.year}年{self.month}月【{self.id}】"

class Bill(models.Model):
    # id = models.CharField('采购账单号', max_length=32, primary_key=True)
    emp = models.ForeignKey(Emp, models.SET_NULL, verbose_name="采购负责人", null=True)
    date = models.DateField("采购日期", auto_now=False, auto_now_add=False)
    money = models.DecimalField("金额", max_digits=32, decimal_places=4)
    content = models.TextField("内容")

    class Meta:
        verbose_name = verbose_name_plural = '采购账单'

    def __str__(self):
        return f"{self.date} {self.emp}"
