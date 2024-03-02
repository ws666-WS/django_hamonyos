from django.db import models

# original_data
class Data(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # ADC值字段，用于存储模拟信号转换后的数字值，可以为空（null=Ture）且允许留空（blank=Ture）
    adc_value = models.IntegerField(null=True, blank=True)

# Create your models here.
