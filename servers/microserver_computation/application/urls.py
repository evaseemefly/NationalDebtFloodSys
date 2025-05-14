# from controller import *
from controller.tasks import app as tasks_app
from controller.typhoon import app as ty_app

urlpatterns = [
    {"ApiRouter": tasks_app, "prefix": "/tasks", "tags": ["创建数值模式计算作业"]},
    {"ApiRouter": ty_app, "prefix": "/flood", "tags": ["台风模块"]},
]
