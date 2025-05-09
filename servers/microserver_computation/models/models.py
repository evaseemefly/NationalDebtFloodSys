from typing import Optional

from sqlalchemy import create_engine, Column, Float, Integer, String, JSON, ForeignKey, Enum, DateTime, Text, Boolean, \
    UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped, relationship

from common.default import DEFAULT_PATH, DEFAULT_NAME, DEFAULT_ENUM, NONE_ID, DEFAULT_CODE
from common.enums import TaskStatusEnum
from models.base_model import IDel, IForecastTime, IModel, IIdIntModel, IReleaseTime, IIssueTime

Base = declarative_base()


class TaskJobs(Base):
    __tablename__ = 'task_jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ty_code: Mapped[str] = mapped_column(default=DEFAULT_CODE)
    task_name = Column(String(255), nullable=False)
    parameters = Column(JSON, nullable=False)
    status = Column(Integer, default=TaskStatusEnum.pending.value)
    duration = Column(Integer)
    gmt_submit_time = Column(DateTime, default=datetime.utcnow)
    gmt_completed_time = Column(DateTime)
    error_message = Column(Text)


class ICoverageFileModel(Base):
    __abstract__ = True
    relative_path: Mapped[str] = mapped_column(String(50), default=DEFAULT_PATH)
    file_name: Mapped[str] = mapped_column(String(100), default=DEFAULT_NAME)


class GeoCoverageFiles(IDel, IIdIntModel, ICoverageFileModel, IForecastTime, IIssueTime, IModel):
    """

    """
    __tablename__ = 'geo_coverage_files'

    coverage_type: Mapped[int] = mapped_column(default=DEFAULT_ENUM)
    """预报产品类型"""

    task_id: Mapped[int] = mapped_column(default=NONE_ID)
    ty_code: Mapped[str] = mapped_column(default=DEFAULT_CODE)


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    gmt_create_time = Column(DateTime, default=datetime.utcnow)
    gmt_modify_time = Column(DateTime, default=datetime.utcnow)


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(255), nullable=False)
    gmt_create_time = Column(DateTime, default=datetime.utcnow)
    gmt_modify_time = Column(DateTime, default=datetime.utcnow)


class RelaTaskFiles(Base):
    __tablename__ = 'rela_task_files'
    __table_args__ = {'schema': 'sys_flood_nationaldebt'}

    # 主键
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # 外键字段
    file_id: Mapped[int] = mapped_column(ForeignKey('geo_coverage_files.id'), nullable=False)
    file_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    task_id: Mapped[Optional[int]] = mapped_column(ForeignKey('task_jobs.id'), nullable=True)

    # 关系定义
    file: Mapped["GeoCoverageFiles"] = relationship("GeoCoverageFiles")
    task: Mapped[Optional["TaskJobs"]] = relationship("TaskJobs")


class RelaGroupPathTask(Base):
    __tablename__ = 'rela_grouppath_task'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    task_id: Mapped[int] = mapped_column(
        ForeignKey('task_jobs.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey('typhoon_forecast_grouppath.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )

    # 关系定义
    task: Mapped["TaskJobs"] = relationship("TaskJobs", back_populates="group_paths")
    group: Mapped["TyphoonForecastGrouppath"] = relationship("TyphoonForecastGrouppath", back_populates="task_paths")

    # 添加复合唯一约束，防止重复关联
    __table_args__ = (
        UniqueConstraint('task_id', 'group_id', name='uq_task_group'),
    )


class TyphoonForecastDetailinfo(Base):
    """台风预报详细信息表"""
    __tablename__ = 'typhoon_forecast_detailinfo'
    __table_args__ = {'schema': 'sys_flood_nationaldebt'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_del = Column(Boolean, default=False)
    gmt_create_time = Column(DateTime(6), default=datetime.utcnow)
    gmt_modify_time = Column(DateTime(6), default=datetime.utcnow)
    code = Column(String(200), nullable=False)
    name_ch = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=False)
    gmt_start = Column(DateTime(6), nullable=True)
    gmt_end = Column(DateTime(6), nullable=True)
    forecast_source = Column(Integer, nullable=False)
    is_forecast = Column(Boolean, nullable=False, default=True)
    timestamp: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f"<TyphoonForecastDetailinfo(id={self.id}, code={self.code})>"


class TyphoonForecastGrouppath(Base):
    """台风预报路径组表"""
    __tablename__ = 'typhoon_forecast_grouppath'
    __table_args__ = {'schema': 'sys_flood_nationaldebt'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_del = Column(Boolean, nullable=False, default=False)
    gmt_create_time = Column(DateTime(6), default=datetime.utcnow)
    gmt_modify_time = Column(DateTime(6), default=datetime.utcnow)
    ty_id = Column(Integer, nullable=False)
    ty_code = Column(String(200), nullable=False)
    file_name = Column(String(200), nullable=False)
    relative_path = Column(String(500), nullable=False)
    timestamp: Mapped[int] = mapped_column(default=0)
    ty_path_type = Column(String(3), nullable=False)

    def __repr__(self):
        return f"<TyphoonForecastGrouppath(id={self.id}, ty_code={self.ty_code})>"


class TyphoonForecastRealdata(Base):
    """台风预报实际数据表"""
    __tablename__ = 'typhoon_forecast_realdata'
    __table_args__ = {'schema': 'sys_flood_nationaldebt'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_del = Column(Boolean, nullable=False, default=False)
    gmt_create_time = Column(DateTime(6), default=datetime.utcnow)
    gmt_modify_time = Column(DateTime(6), default=datetime.utcnow)
    ty_id = Column(Integer, nullable=False)
    gp_id = Column(Integer, nullable=False)
    forecast_dt = Column(DateTime(6), nullable=True)
    forecast_index = Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    bp = Column(Float, nullable=False)
    gale_radius = Column(Float, nullable=False, default=-1)
    timestamp: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f"<TyphoonForecastRealdata(id={self.id}, ty_id={self.ty_id})>"
