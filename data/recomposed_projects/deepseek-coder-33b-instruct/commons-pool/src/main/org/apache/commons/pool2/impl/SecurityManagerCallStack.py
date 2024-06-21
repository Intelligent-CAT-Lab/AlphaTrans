from __future__ import annotations
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

        class_context = inspect.stack()
        map_stream = map(
            lambda x: weakref.ref(x.frame.f_locals.get("self").__class__), class_context
        )
        return list(map_stream)


class SecurityManagerCallStack:

    __snapshot: Snapshot = None

    def clear(self) -> None:

        self.__snapshot = None
