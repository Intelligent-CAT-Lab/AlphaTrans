from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io

# Imports End


class XXHash32:

    # Class Fields Begin
    __BUF_SIZE: int = None
    __ROTATE_BITS: int = None
    __PRIME1: int = None
    __PRIME2: int = None
    __PRIME3: int = None
    __PRIME4: int = None
    __PRIME5: int = None
    __oneByte: typing.List[int] = None
    __state: typing.List[int] = None
    __buffer: typing.List[int] = None
    __seed: int = None
    __totalLen: int = None
    __pos: int = None
    __stateUpdated: bool = None
    # Class Fields End

    # Class Methods Begin
    def getValue(self) -> int:
        pass

    def update(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def update(self, b: int) -> None:
        pass

    def reset(self) -> None:
        pass

    def update1(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def update0(self, b: int) -> None:
        pass

    @staticmethod
    def XXHash321() -> XXHash32:
        pass

    def __init__(self, seed: int) -> None:
        pass

    def __process(self, b: typing.List[int], offset: int) -> None:
        pass

    def __initializeState(self) -> None:
        pass

    @staticmethod
    def __getInt(buffer: typing.List[int], idx: int) -> int:
        pass

    # Class Methods End
