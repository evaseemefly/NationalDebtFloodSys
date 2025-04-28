from datetime import datetime, timedelta
from typing import List, Dict, Optional

import requests
from lxml import etree
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from pydantic import ValidationError

from common.default import DEFAULT_CODE
from common.exceptions import NoExistTargetTyphoon
from models.mid_models import TyDetailMidModel, TyPathMidModel
from schema.common import ResponseModel
from schema.typhoon import TyphoonPathSchema

app = APIRouter()


@app.post('/create/typhoon/path',
          summary="获取提交的作业请求")
async def get(params: TyphoonPathSchema):
    """
        根据 ty_code 获取对应台风的路径(实况|预报)
    :param params:
    :return:
    """
    try:
        #
        print(f"Received typhoon path data: {params.dict()}")

        # 测试——返回提交的数据集
        return ResponseModel(
            code=200,
            message="数据提交成功",
            data=params.dict()
        )

    except Exception as e:
        # 异常处理
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
