from datetime import datetime, timedelta
from typing import List, Dict, Optional

import arrow
import requests
from lxml import etree
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from pydantic import ValidationError

from common.default import DEFAULT_CODE
from common.enums import TyphoonGroupEnum
from common.exceptions import NoExistTargetTyphoon
from core.jobs import JobGenerateTyphoonPathFile
from dao.coverage import CoverageDao
from dao.jobs import TaskDao
from dao.typhoon import TyphoonDao
from models.mid_models import TyDetailMidModel, TyPathMidModel
from schema.common import ResponseModel
from schema.task import TyGroupTaskSchema
from schema.typhoon import TyphoonPathSchema, TyphoonPathComplexSchema, TyphoonDistGroupSchema

app = APIRouter()


# @app.get('/surge/max/url',
#          summary="根据group获取对应的增水场url", response_model=str)
# async def get(ty_code: str, task_id: int, group: TyphoonGroupEnum = TyphoonGroupEnum.GROUP_CENTER):
#     """
#         根据 ty_code 获取对应台风的路径(实况|预报)
#     :param params:
#     :return:
#     """
#     try:
#         # 将集合路径 type转换为对应 enmu
#         group_type_enum: TyphoonGroupEnum = TyphoonGroupEnum(group)
#         """集合路径对应的类型"""
#         coverage_dao = CoverageDao()
#         res = coverage_dao.get_tif_file_url(ty_code, task_id, group_type_enum)
#         return res
#
#     except Exception as e:
#         # 异常处理
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )

@app.get('/surge/max/url',
         summary="根据group获取对应的增水场url", response_model=str)
async def get(ty_code: str, issue_ts: int, group: TyphoonGroupEnum = TyphoonGroupEnum.GROUP_CENTER):
    """
        根据 ty_code 获取对应台风的路径(实况|预报)
    :param params:
    :return:
    """
    try:
        # 将集合路径 type转换为对应 enmu
        group_type_enum: TyphoonGroupEnum = TyphoonGroupEnum(group)
        """集合路径对应的类型"""
        coverage_dao = CoverageDao()
        res = coverage_dao.get_tif_file_url(ty_code, issue_ts, group_type_enum)
        return res

    except Exception as e:
        # 异常处理
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
