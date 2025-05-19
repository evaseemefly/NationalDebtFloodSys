from typing import List, Optional, Any, Union

from sqlalchemy import distinct, select

from common.default import MS_UNIT
from common.enums import RasterFileType, TyphoonGroupEnum
from core.jobs import JobGenerateTyphoonPathFile, JobGenerateSurgeRasterPathFile
from dao.base import BaseDao
from models.models import TyphoonForecastGrouppath, TyphoonForecastRealdata, GeoCoverageFiles
from schema.task import TyGroupTaskSchema
from schema.typhoon import TyphoonPathComplexSchema, TyphoonDistGroupSchema, TyphoonPointSchema


class BaseCoverageDao(BaseDao):
    def get_coveage_file_byparams(self, ty_code: str, task_id: int, raster_type: RasterFileType,
                                  group_type: TyphoonGroupEnum, issue_ts: int,
                                  **kwargs) -> GeoCoverageFiles:
        """
            根据 预报 | 发布 时间戳 获取对应的 nc | tif 文件信息
        @param raster_type: 栅格图层种类 nc|tif
        @param area:        预报区域
        @param issue_ts:    发布时间戳
        @param kwargs:
        @return:
        """
        try:
            with self.session as session:
                stmt = select(GeoCoverageFiles).where(
                    GeoCoverageFiles.ty_code == ty_code,
                    GeoCoverageFiles.task_id == task_id,
                    GeoCoverageFiles.coverage_type == raster_type.value)
                res = session.execute(stmt).scalar_one_or_none()
        except Exception as ex:
            print(ex)
        pass
        return res


class CoverageDao(BaseDao):
    pass
# def get_
