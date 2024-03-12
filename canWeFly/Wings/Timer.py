from threading import Thread
from typing import Callable

import schedule
import time


class Timer(Thread):
    """
    定时器, 全局唯一
    """
    def __init__(self):
        super().__init__()

    @classmethod
    def add_every_minutes_job(cls, mins: int, function: Callable, *args, **kwargs):
        # 每次重启都会直接执行一次先
        function(*args, **kwargs)
        schedule.every(mins).minutes.do(function, *args, **kwargs)
        # schedule.every(days).days.do(function, *args, **kwargs)

    def run(self) -> None:
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    Timer().start()      # 系统运行时运行

    def a_job(n):
        print(n)

    Timer.add_every_minutes_job(1, a_job, "100")
    Timer.add_every_minutes_job(1, a_job, "100")
    Timer.add_every_minutes_job(0, a_job, "100")
