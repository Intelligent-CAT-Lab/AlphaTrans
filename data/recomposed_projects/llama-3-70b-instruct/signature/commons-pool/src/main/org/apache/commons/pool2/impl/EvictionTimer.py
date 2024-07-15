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

        pass  # LLM could not translate this method


class WeakRunner(typing.Callable):

    __ref: weakref.ref = None

    def run(self) -> None:
        task: Runnable = self.__ref.get()
        if task is not None:
            task.run()
        else:
            executor.remove(self)
            taskMap.remove(self.__ref)

    def __init__(self, ref: weakref.ref) -> None:
        self.__ref = ref


class EvictionTimer:

    __taskMap: typing.Dict[weakref.ref, weakRunner] = {}

    __executor: typing.Union[
        concurrent.futures.ThreadPoolExecutor, concurrent.futures.Future
    ] = None

    def toString(self) -> str:
        builder = StringBuilder()
        builder.append("EvictionTimer []")
        return builder.toString()

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
            and len(EvictionTimer.__taskMap) == 0
        ):
            EvictionTimer.__executor.shutdown()
            try:
                EvictionTimer.__executor.awaitTermination(
                    timeout.total_seconds(), datetime.timedelta(seconds=1)
                )
            except Exception as e:
                pass
            EvictionTimer.__executor.setCorePoolSize(0)
            EvictionTimer.__executor = None

    def __init__(self) -> None:
        self.__ref = weakref.ref(self)

    @staticmethod
    def __remove(evictor: Evictor[typing.Any]) -> None:
        for entry in EvictionTimer.__taskMap.items():
            if entry[0]() == evictor:
                EvictionTimer.__executor.remove(entry[1])
                EvictionTimer.__taskMap.pop(entry[0])
                break
