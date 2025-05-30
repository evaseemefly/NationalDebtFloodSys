from typing import List
from datetime import datetime
import arrow


class TyDetailMidModel:
    def __init__(self, ty_code: str, id: int, ty_name_en: str = None, ty_name_ch: str = None):
        self.ty_code = ty_code
        self.id = id
        self.ty_name_en = ty_name_en
        self.ty_name_ch = ty_name_ch

    def __str__(self) -> str:
        return f'TyDetailMidModel:id:{self.id}|ty_code:{self.ty_code}|name_en:{self.ty_name_en}|name_ch：{self.ty_name_ch}'


class TyForecastRealDataMidModelBackup:
    def __init__(self, lat: float, lon: float, bp: int, ts: int, ty_type: str, forecast_ty_path_list: []):
        """

        :param lat:
        :param lon:
        :param bp:
        :param ts:
        :param ty_type:
        """
        self.lat = lat
        self.lon = lon
        self.bp = bp
        self.ts = ts
        self.ty_type = ty_type
        self.forecast_ty_path_list = forecast_ty_path_list


class TyForecastRealDataMidModel:
    def __init__(self, lat: float, lon: float, bp: int, ts: int, ty_type: str,
                 forecast_ty_path_list: []):
        """

        :param lat:
        :param lon:
        :param bp:
        :param ts:
        :param ty_type:
        """
        self.lat = lat
        self.lon = lon
        self.bp = bp
        self.ts = ts
        self.ty_type = ty_type
        self.forecast_ty_path_list = []

    @property
    def forecast_dt(self) -> datetime:
        return arrow.get(self.ts).datetime


class TyPathMidModel:
    def __init__(self, ty_id: int, ty_code: str, ty_name_en: str, ty_name_ch: str,
                 ty_path_list: List[TyForecastRealDataMidModel] = []):
        """

        :param ty_id:
        :param ty_code:
        :param ty_name_en:
        :param ty_name_ch:
        :param ty_rate:
        :param ty_stamp:
        """
        self.ty_id = ty_id
        self.ty_code = ty_code
        self.ty_name_en = ty_name_en
        self.ty_name_ch = ty_name_ch
        self.ty_path_list = ty_path_list

        # self.ty_stamp = ty_stamp

    # @property
    # def ty_forecast_dt(self) -> datetime.datetime:
    #     return arrow.get(self.ty_stamp).datetime
