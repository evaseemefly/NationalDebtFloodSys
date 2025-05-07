from sqlalchemy import create_engine, Column, Float, Integer, String, JSON, ForeignKey, Enum, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from common.enums import TaskStatusEnum

Base = declarative_base()


class TaskJobs(Base):
    __tablename__ = 'task_jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(255), nullable=False)
    parameters = Column(JSON, nullable=False)
    status = Column(Integer, default=TaskStatusEnum.pending.value)
    duration = Column(Integer)
    gmt_submit_time = Column(DateTime, default=datetime.utcnow)
    gmt_completed_time = Column(DateTime)
    error_message = Column(Text)


class GeoCoverageFiles(Base):
    __tablename__ = 'geo_coverage_files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pid = Column(Integer, nullable=False)
    is_del = Column(Integer, nullable=False)
    forecast_dt = Column(DateTime)
    forecast_ts = Column(Integer, nullable=False)
    issue_dt = Column(DateTime)
    issue_ts = Column(Integer)
    relative_path = Column(String(50), nullable=False)
    file_name = Column(String(100), nullable=False)
    file_ext = Column(String(50), nullable=False)
    coverage_type = Column(Integer, nullable=False)
    gmt_create_time = Column(DateTime, default=datetime.utcnow)
    gmt_modify_time = Column(DateTime)
    task_id = Column(Integer, ForeignKey('task_jobs.id'), nullable=False)


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


class RelaUserGroupFile(Base):
    __tablename__ = 'rela_user_group_file'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('auth_user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('auth_group.id'), nullable=False)
    file_id = Column(Integer, ForeignKey('geo_coverage_files.id'), nullable=False)
    file_type = Column(Integer)
    task_id = Column(Integer, ForeignKey('task_jobs.id'))


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
