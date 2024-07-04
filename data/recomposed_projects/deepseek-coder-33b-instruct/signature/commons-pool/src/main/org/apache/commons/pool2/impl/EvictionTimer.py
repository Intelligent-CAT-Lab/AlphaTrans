from __future__ import annotations
import time
import re
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *


class Reaper(typing.Callable):

    def run(self) -> None:
        with EvictionTimer:
            for entry in taskMap.items():
                if entry[0].get() is None:
                    executor.remove(entry[1])
                    taskMap.pop(entry[0])
            if not taskMap and executor is not None:
                executor.shutdown()
                executor.setCorePoolSize(0)
                executor = None


class WeakRunner(typing.Callable):

    __ref: weakref.ref = None

    def run(self) -> None:
        task = self.__ref()
        if task is not None:
            task()
        else:
            self.executor.remove(self)
            self.taskMap.remove(self.__ref)

    def __init__(self, ref: weakref.ref) -> None:
        self.__ref = ref


class EvictionTimer:

    __taskMap: typing.Dict[weakref.ref, weakRunner] = {}

    __executor: typing.Union[
        concurrent.futures.ThreadPoolExecutor, concurrent.futures.Future
    ] = None

    def toString(self) -> str:
        return "EvictionTimer []"

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

        pass  # LLM could not translate this method

    @staticmethod
    def __remove(evictor: Evictor[typing.Any]) -> None:

        for key, value in EvictionTimer.__taskMap.items():
            if key() == evictor:
                EvictionTimer.__executor.remove(value)
                del EvictionTimer.__taskMap[key]
                break
