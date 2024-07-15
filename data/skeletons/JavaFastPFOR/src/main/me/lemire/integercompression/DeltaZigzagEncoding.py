from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Context:

    # Class Fields Begin
    contextValue: int = None
    # Class Fields End

    # Class Methods Begin
    def getContextValue(self) -> int:
        pass

    def setContextValue(self, contextValue: int) -> None:
        pass

    def __init__(self, contextValue: int) -> None:
        pass

    # Class Methods End


class Decoder(Context):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decodeArray2(self, src: typing.List[int]) -> typing.List[int]:
        pass

    def decodeArray1(
        self, src: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        pass

    def decodeArray0(
        self,
        src: typing.List[int],
        srcoff: int,
        length: int,
        dst: typing.List[int],
        dstoff: int,
    ) -> typing.List[int]:
        pass

    def decodeInt(self, value: int) -> int:
        pass

    def __init__(self, contextValue: int) -> None:
        pass

    # Class Methods End


class Encoder(Context):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def encodeArray3(self, src: typing.List[int]) -> typing.List[int]:
        pass

    def encodeArray2(
        self, src: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        pass

    def encodeArray1(
        self, src: typing.List[int], srcoff: int, length: int, dst: typing.List[int]
    ) -> typing.List[int]:
        pass

    def encodeArray0(
        self,
        src: typing.List[int],
        srcoff: int,
        length: int,
        dst: typing.List[int],
        dstoff: int,
    ) -> typing.List[int]:
        pass

    def encodeInt(self, value: int) -> int:
        pass

    def __init__(self, contextValue: int) -> None:
        pass

    # Class Methods End


class DeltaZigzagEncoding:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass
