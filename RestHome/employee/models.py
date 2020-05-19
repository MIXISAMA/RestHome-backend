from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

# Create your models here.

class Position(models.Model):
    name = models.CharField('职称', max_length=16, primary_key=True)

    class Meta:
        verbose_name = verbose_name_plural = '职位'

    def __str__(self):
        return self.name

class Emp(User):
    SexType = (
        ("男", "男"),
        ("女", "女"),
    )
    position = models.ForeignKey(Position, models.SET_NULL, null=True, blank=True, verbose_name="职位")
    sex = models.CharField('性别', choices=SexType, max_length=2)
    birthday = models.DateField("生日", auto_now=False, auto_now_add=False)
    telephone = models.DecimalField("手机号", max_digits=20, decimal_places=0)
    address = models.CharField("住址", max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = '职员'

    def __str__(self):
        return f"{self.first_name}【{self.username}】"

class Room(models.Model):
    StatusType = (
        ("正在使用", "正在使用"),
        ("未使用", "未使用"),
    )
    id = models.CharField('房间号', max_length=8, primary_key=True)
    emp = models.ForeignKey(Emp, models.SET_NULL, 'rooms',verbose_name="负责职员", null=True, blank=True)
    status = models.CharField('状态', choices=StatusType, max_length=10, default="未使用")

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

class OrderForm(models.Model):
    date_joined = models.DateTimeField('创建日期', default=timezone.now)
    old = models.ForeignKey('old.Old', models.SET_NULL, "老人", null=True)
    company_name = models.CharField("机构名称", max_length=50)
    company_id = models.IntegerField("机构id")
    status = models.CharField("状态", max_length=50)
    comment = models.TextField("评价", null=True, blank=True, default=None)
    mark = models.FloatField("评分", null=True, blank=True, default=None)

    class Meta:
        verbose_name = verbose_name_plural = '订单'

    def __str__(self):
        return f"{self.id}"
