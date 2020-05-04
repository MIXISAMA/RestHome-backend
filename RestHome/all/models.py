from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    CompanyType = (
        ("餐饮", "餐饮"),
        ("医护", "医护"),
        ("心理咨询", "心理咨询")
    )
    date_joined = models.DateTimeField('创建日期', default=timezone.now)
    name = models.CharField("企业名", max_length=50)
    tp = models.CharField("类型", choices=CompanyType, max_length=20)
    telephone = models.DecimalField("手机号", max_digits=20, decimal_places=0)
    address = models.CharField("住址", max_length=50)
    introduce = models.TextField("介绍")

    def __str__(self):
        return f"{self.name}【{self.id}】"
    
    class Meta:
        verbose_name = verbose_name_plural = '企业'

class Announcement(models.Model):
    date_joined = models.DateTimeField('创建日期', default=timezone.now)
    title = models.CharField("标题", max_length=50)
    author = models.CharField("作者", max_length=50)
    content = models.TextField("介绍")

    def __str__(self):
        return f"{self.title}【{self.id}】"

    class Meta:
        verbose_name = verbose_name_plural = '公告'
