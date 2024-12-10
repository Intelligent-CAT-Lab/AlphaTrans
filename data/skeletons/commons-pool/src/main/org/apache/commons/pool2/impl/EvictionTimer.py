from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.BaseGenericObjectPool import *
import datetime
import typing
from typing import *
import io

# Imports End


class Reaper:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    # Class Methods End


class WeakRunner:

    # Class Fields Begin
    __ref: weakref.ref = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    def __init__(self, ref: weakref.ref) -> None:
        pass

    # Class Methods End


class EvictionTimer:

    # Class Fields Begin
    __executor: typing.Union[
        concurrent.futures.ThreadPoolExecutor, concurrent.futures.Future
    ] = None
    __taskMap: typing.Dict[weakref.ref, weakRunner] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    @staticmethod
    def getNumTasks() -> int:
        pass

    @staticmethod
    def cancel(
        evictor: Evictor[typing.Any], timeout: datetime.timedelta, restarting: bool
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __remove(evictor: Evictor[typing.Any]) -> None:
        pass

    # Class Methods End
