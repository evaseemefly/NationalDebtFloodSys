import enum

class TaskStatus(enum.Enum):
    """
        任务枚举类
    """
    pending = 4001
    in_progress = 4002
    completed = 4003
    failed = 4004