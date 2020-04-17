# Generated by Django 3.0.5 on 2020-04-17 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Old',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='账户')),
                ('name', models.CharField(max_length=8, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=2, verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('telephone', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='手机号')),
                ('address', models.CharField(max_length=50, verbose_name='住址')),
            ],
            options={
                'verbose_name': '老人',
                'verbose_name_plural': '老人',
            },
        ),
    ]
