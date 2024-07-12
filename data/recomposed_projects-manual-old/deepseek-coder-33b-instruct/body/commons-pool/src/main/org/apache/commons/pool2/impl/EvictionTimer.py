from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *


class Reaper(typing.Callable):

    def run(self) -> None:

        with EvictionTimer:
            for entry in self.taskMap.items():
                if entry[0].get() is None:
                    self.executor.remove(entry[1])
                    del self.taskMap[entry[0]]

            if not self.taskMap and self.executor is not None:
                self.executor.shutdown()
                self.executor.setCorePoolSize(0)
                self.executor = None


class WeakRunner(typing.Callable):

    __ref: weakref.ref = None

    def run(self) -> None:

        task: typing.Callable = self.__ref()
        if task is not None:
            task()
        else:
            self.executor.remove(self)
            self.taskMap.pop(self.__ref, None)

    def __init__(self, ref: weakref.ref) -> None:
        self.__ref = ref


class EvictionTimer:

    __taskMap: typing.Dict[weakref.ref, weakRunner] = {}

    __executor: typing.Union[
        concurrent.futures.ThreadPoolExecutor, concurrent.futures.Future
    ] = None

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("EvictionTimer []")
        return builder.getvalue()

    @staticmethod
    def getNumTasks() -> int:
        return len(EvictionTimer.__taskMap)

    @staticmethod
    def cancel(
        evictor: Evictor[typing.Any], timeout: datetime.timedelta, restarting: bool
    ) -> None:

        if evictor is not None:
            evictor.cancel()
            EvictionTimer.__remove(evictor)

        if (
            not restarting
            and EvictionTimer.__executor is not None
            and not EvictionTimer.__taskMap
        ):
            EvictionTimer.__executor.shutdown()
            try:
                EvictionTimer.__executor.awaitTermination(
                    timeout.total_seconds(), TimeUnit.SECONDS
                )
            except InterruptedException:
                pass
            EvictionTimer.__executor.setCorePoolSize(0)
            EvictionTimer.__executor = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def __remove(evictor: Evictor[typing.Any]) -> None:

        for key, value in EvictionTimer.__taskMap.items():
            if key() == evictor:
                EvictionTimer.__executor.remove(value)
                del EvictionTimer.__taskMap[key]
                break
