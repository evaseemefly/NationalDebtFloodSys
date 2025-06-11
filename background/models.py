from arrow import Arrow
from sqlalchemy import String, Float, Boolean, Integer, DateTime, ForeignKey, func, Text, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.mysql import JSON
from geoalchemy2 import Geometry
from datetime import datetime
from typing import Optional, Any

from commons.enums import FloodLevelEnum


class Base(DeclarativeBase):
    pass


class Station(Base):
    __tablename__ = "station_info"
    __table_args__ = {"schema": "sys_flood_nationaldebt"}

    station_name: Mapped[Optional[str]] = mapped_column(String(10))
    station_code: Mapped[Optional[str]] = mapped_column(String(10))
    lat: Mapped[Optional[float]] = mapped_column(Float)
    lon: Mapped[Optional[float]] = mapped_column(Float)
    desc: Mapped[Optional[str]] = mapped_column(String(500))
    is_abs: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    pid: Mapped[Optional[int]] = mapped_column(Integer)
    is_in_common_use: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    rid: Mapped[Optional[int]] = mapped_column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    is_del: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    gmt_create_time: Mapped[Optional[datetime]] = mapped_column(DateTime(6))
    gmt_modify_time: Mapped[Optional[datetime]] = mapped_column(DateTime(6))

    def __repr__(self) -> str:
        return f"Station(id={self.id}, station_name={self.station_name}, station_code={self.station_code})"


class StationForecastRealdataModel(Base):
    __tablename__ = "station_forecast_realdata"
    __table_args__ = {"schema": "sys_flood_nationaldebt"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    is_del: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    ty_code: Mapped[str] = mapped_column(String(200), nullable=False)
    gp_id: Mapped[int] = mapped_column(Integer, nullable=False)
    station_code: Mapped[str] = mapped_column(String(200), nullable=False)
    forecast_dt: Mapped[Optional[datetime]] = mapped_column(DateTime(2))
    forecast_ts: Mapped[int]
    forecast_index: Mapped[int] = mapped_column(Integer, nullable=False)
    surge: Mapped[float] = mapped_column(Float, nullable=False)
    timestamp: Mapped[str] = mapped_column(String(100), nullable=False)
    gmt_created: Mapped[Optional[datetime]] = mapped_column(DateTime(6), default=datetime.utcnow())
    gmt_modified: Mapped[Optional[datetime]] = mapped_column(DateTime(6), default=datetime.utcnow())

    def __repr__(self) -> str:
        return (f"StationForecastRealdata(id={self.id}, ty_code={self.ty_code}, "
                f"station_code={self.station_code}, forecast_dt={self.forecast_dt})")


class GeoFloodLevelPolygon(Base):
    __tablename__ = "geo_floodlevel_polygon"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[float] = mapped_column(Float, comment="增水值")
    ty_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True, comment="台风编号")
    name: Mapped[Optional[str]] = mapped_column(String(100), comment="多边形名称")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    properties: Mapped[Optional[str]] = mapped_column(Text, comment="GeoJSON properties 的 JSON 字符串")
    geom: Mapped[Any] = mapped_column(Geometry("POLYGON", srid=4326), nullable=False, comment="多边形几何数据")
    flood_level: Mapped[int] = mapped_column(Integer, comment="淹没等级——枚举", default=FloodLevelEnum.GTE100.value)
    gmt_create_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        comment="创建时间"
    )
    gmt_update_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        onupdate=func.current_timestamp(),
        comment="更新时间"
    )

    issue_time: Mapped[int] = mapped_column(default=Arrow.utcnow().int_timestamp,
                                            comment="发布时间")

    def __repr__(self) -> str:
        return f"<GeoFloodLevelPolygon(id={self.id}, ty_code='{self.ty_code}', gp_id='{self.gp_id}')>"


class GeoPolygon(Base):
    """存储 GeoJSON 多边形数据的模型"""

    __tablename__ = "geo_polygons"
    __table_args__ = {"extend_existing": True}  # 允许扩展已定义的表

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[float] = mapped_column(Float, comment="增水值")
    ty_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True, comment="台风编号")
    # gp_id: Mapped[str] = mapped_column(String(100), nullable=False, index=True, comment="多边形标识ID")
    name: Mapped[Optional[str]] = mapped_column(String(100), comment="多边形名称")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述信息")
    properties: Mapped[Optional[str]] = mapped_column(Text, comment="GeoJSON properties 的 JSON 字符串")
    geom: Mapped[Any] = mapped_column(Geometry("POLYGON", srid=4326), nullable=False, comment="多边形几何数据")
    gmt_create_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        comment="创建时间"
    )
    gmt_update_time: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        onupdate=func.current_timestamp(),
        comment="更新时间"
    )

    issue_time: Mapped[int] = mapped_column(default=Arrow.utcnow().int_timestamp,
                                            comment="发布时间")

    # 定义索引
    # __table_args__ = (
    #     Index("idx_created_at", "gmt_create_time"),
    #     Index("idx_updated_at", "gmt_update_time"),
    #     {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4", "mysql_collate": "utf8mb4_unicode_ci"}
    # )

    def __repr__(self) -> str:
        return f"<GeoPolygon(id={self.id}, ty_code='{self.ty_code}', gp_id='{self.gp_id}')>"
