from common.enums import TyphoonGroupEnum, NullEnum

switch_dict = {'center': TyphoonGroupEnum.GROUP_CENTER,
               'fast': TyphoonGroupEnum.GROUP_FAST,
               'slow': TyphoonGroupEnum.GROUP_SLOW,
               'left': TyphoonGroupEnum.GROUP_LEFT,
               'right': TyphoonGroupEnum.GROUP_RIGHT}


def get_ty_group_enum(val: str) -> TyphoonGroupEnum:
    """
        根据 group stamp 获取对应的集合路径类型枚举
    @param val:
    @return:
    """
    return switch_dict.get(val, NullEnum)
