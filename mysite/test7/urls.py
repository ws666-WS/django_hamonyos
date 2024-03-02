from django.urls import path
from test7 import views

urlpatterns = [
    path('update/', views.IotData.as_view()),  # 从iot平台推送的信息存入数据库
    path('iotdata1/', views.IotData1.as_view()),  # 调用命令下发API，ON
    path('iotdata2/', views.IotData2.as_view()),  # 调用命令下发API，OFF
    path('app/', views.AppReq.as_view()),  # app
]
