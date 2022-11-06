# Generated by Django 4.1.1 on 2022-11-06 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('user', models.IntegerField(null=True, verbose_name='用户的id')),
                ('preferred_payment_method', models.IntegerField(blank=True, choices=[(1, 'cash'), (2, 'credit card'), (3, 'check')], null=True)),
                ('people_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(14)], verbose_name='预定人数')),
                ('desk_no', models.CharField(max_length=255, verbose_name='预定桌子的编号')),
                ('status', models.IntegerField(default=1, verbose_name='预定状态')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('phone_number', models.CharField(max_length=255, verbose_name='手机号码')),
                ('email_address', models.CharField(max_length=255, verbose_name='邮件号码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_no', models.IntegerField(verbose_name='桌子编号')),
                ('desk_seat', models.IntegerField(verbose_name='桌子座位数')),
                ('desk_status', models.IntegerField(verbose_name='桌子状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
            ],
        ),
    ]
