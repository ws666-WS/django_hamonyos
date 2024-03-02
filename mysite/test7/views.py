from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from jsonpath import jsonpath
from django.http import HttpResponse
from test7.models import Data
# 华为云IotDA的SDK
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


# 定义一个IotData类用于继承自Django REST framwork中的APIView基类，用于处理与物联网设备数据相关的API请求
class IotData(APIView):
    # 定义一个处理post请求的方法
    def post(self, request, *args, **kwargs):
        # 从请求对象中获取原始的POST数据，json数据
        data = request.data
        # 打印原始的数据
        print(data)
        # 使用get方法从原始的POST数据中提取'notify_data'字段的值
        notify_data = request.data.get('notify_data')
        # 使用jsonpath解析'notify_data',获取其中的'event_time'字段的所有值
        event_time = jsonpath(notify_data, '$..event_time')
        # 使用jsonpath解析'notify_data',获取其中的'device_id'字段的所有值
        device_id = jsonpath(notify_data, '$..device_id')
        # 使用jsonpath解析'notify_data',获取其中的'service_id'字段的所有值
        service_id = jsonpath(notify_data, '$..service_id')
        # 使用jsonpath解析'notify_data',获取其中的'adc_value'字段的所有值
        adc_value = jsonpath(notify_data, '$..ADC_Value')
        # 创建一个新的Data模型实例，提取出数据到对应字段
        iota = Data.objects.create(
            event_time=event_time[0],  # 事件时间
            device_id=device_id[0],  # 设备ID
            service_id=service_id[0],  # 服务ID
            adc_value=adc_value[0],  # 设备数据
            notify_data=data  # 原始数据
        )
        # 将新建的模型示例保存到数据库
        iota.save()
        # 处理完成后，返回HTTP响应，状态码为200，内容为"200 OK"
        return HttpResponse("200 OK")


class IotData1(APIView):
    def post(self, request):

        ak = "0QOEBQ4Y9GQ4YRFKH8QF"

        sk = "FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1"
        credentials = BasicCredentials(ak, sk).with_derived_predicate(
            DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(IoTDARegion.value_of("cn-north-4")) \
            .build()

        try:
            request = CreateCommandRequest()
            request.device_id = "65e1aeee7bdccc0126c5207a_1234567"
            request.body = DeviceCommandRequest(
                paras="{\"Control\":\"ON\"}",
                command_name="ADC_Control",
                service_id="Test7"
            )
            response = client.create_command(request)
            return HttpResponse(response)
        except exceptions.ClientRequestException as e:
            error_response = {
                'status_code': e.status_code,
                'request_id': e.request_id,
                'error_code': e.error_code,
                'error_msg': e.error_msg
            }
            return HttpResponse(error_response)


class IotData1(APIView):
    def post(self, request):

        ak = "0QOEBQ4Y9GQ4YRFKH8QF"

        sk = "FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1"

        credentials = BasicCredentials(ak, sk).with_derived_predicate(
            DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(IoTDARegion.value_of("cn-north-4")) \
            .build()

        try:
            request = CreateCommandRequest()
            request.device_id = "65e1aeee7bdccc0126c5207a_1234567"
            request.body = DeviceCommandRequest(
                paras="{\"Control\":\"ON\"}",
                command_name="ADC_Control",
                service_id="Test7"
            )
            response = client.create_command(request)
            return Response(response.to_dict())  # 返回JSON格式响应
        except exceptions.ClientRequestException as e:
            error_response = {
                'status_code': e.status_code,
                'request_id': e.request_id,
                'error_code': e.error_code,
                'error_msg': e.error_msg
            }
            return Response(error_response)  # 返回JSON格式错误响应


class IotData2(APIView):
    def post(self, request):
        ak = __import__('os').getenv("0QOEBQ4Y9GQ4YRFKH8QF")
        sk = __import__('os').getenv("FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1")
        credentials = BasicCredentials(ak, sk).with_derived_predicate(
            DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(IoTDARegion.value_of("cn-north-4")) \
            .build()

        try:
            request = CreateCommandRequest()
            request.device_id = "65e1aeee7bdccc0126c5207a_1234567"
            request.body = DeviceCommandRequest(
                paras="{\"Control\":\"OFF\"}",
                command_name="ADC_Control",
                service_id="Test7"
            )
            response = client.create_command(request)
            return HttpResponse(response)
        except exceptions.ClientRequestException as e:
            error_response = {
                'status_code': e.status_code,
                'request_id': e.request_id,
                'error_code': e.error_code,
                'error_msg': e.error_msg
            }
            return HttpResponse(error_response)


class AppReq(APIView):
    def post(self, request):
        try:
            # 获取最新的 Data 对象
            mysqlData = Data.objects.last()
            # 打印 abc_value 的值到控制台
            print(mysqlData.adc_value)

            # 返回 HttpResponse 包含 abc_value 的值
            return HttpResponse(mysqlData.adc_value)
        except Data.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")
