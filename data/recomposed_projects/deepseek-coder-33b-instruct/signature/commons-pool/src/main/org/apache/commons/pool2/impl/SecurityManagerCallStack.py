from __future__ import annotations
import time
import re
import io
import typing
from typing import *


class Snapshot:

    __stack: typing.List[weakref.ref] = None

    __timestampMillis: int = int(time.time() * 1000)

    def __init__(self, stack: typing.List[weakref.ref]) -> None:
        self.__stack = stack


class PrivateSecurityManager:

    def __getCallStack(self) -> typing.List[weakref.ref]:
        return [weakref.ref(cls) for cls in self.__class__.__mro__]


class SecurityManagerCallStack:

    __snapshot: Snapshot = None

    def clear(self) -> None:
        self.__snapshot = None
