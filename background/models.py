from sqlalchemy import String, Float, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Optional


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
