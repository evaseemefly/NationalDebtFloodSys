from typing import List, Optional, Any

from sqlalchemy import distinct, select

from common.default import MS_UNIT
from core.jobs import JobGenerateTyphoonPathFile
from dao.base import BaseDao
from schema.typhoon import TyphoonPathComplexSchema


class TaskDao(BaseDao):
    def submit_task(self, user_id: int, params: TyphoonPathComplexSchema):
        # 处理结束自动释放
        try:
            with self.session as session:
                timestamp = params.tyDetail.timeStamp / MS_UNIT
                job = JobGenerateTyphoonPathFile(user_id, params.tyDetail.tyCode, params.tyDetail.tyNameEn,
                                                 params.tyDetail.tyNameCh,
                                                 params.tyDetail.timeStamp)
                job.to_do(session)
                pass
        except Exception as ex:
            # TODO:[*] 25-05-07 Invalid argument(s) 'encoding' sent to create_engine(), using configuration MySQLDialect_mysqldb/QueuePool/Engine.  Please check that the keyword arguments are appropriate for this combination of components.
            # 在 create_engine 传入 encoding ，提示以上错误
            print(ex)
        pass
        pass
