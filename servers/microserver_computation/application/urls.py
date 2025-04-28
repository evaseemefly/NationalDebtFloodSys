# from controller import *
from controller.tasks import app as tasks_app

urlpatterns = [
    {"ApiRouter": tasks_app, "prefix": "/tasks", "tags": ["创建数值模式计算作业"]},
]
