from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io

# Imports End


class Util:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def greatestMultiple(value: int, factor: int) -> int:
        pass

    @staticmethod
    def _unpackw(
        sourcearray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        num: int,
        b: int,
    ) -> int:
        pass

    @staticmethod
    def _packw(
        outputarray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        num: int,
        b: int,
    ) -> int:
        pass

    @staticmethod
    def _packsizew(num: int, b: int) -> int:
        pass

    @staticmethod
    def _unpack(
        sourcearray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        datapos: int,
        num: int,
        b: int,
    ) -> int:
        pass

    @staticmethod
    def _pack(
        outputarray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        datapos: int,
        num: int,
        b: int,
    ) -> int:
        pass

    @staticmethod
    def _packsize(num: int, b: int) -> int:
        pass

    @staticmethod
    def bits(i: int) -> int:
        pass

    @staticmethod
    def maxdiffbits(initoffset: int, i: typing.List[int], pos: int, length: int) -> int:
        pass

    @staticmethod
    def _maxbits32(i: typing.List[int], pos: int) -> int:
        pass

    @staticmethod
    def maxbits(i: typing.List[int], pos: int, length: int) -> int:
        pass

    @staticmethod
    def _smallerorequalthan(x: int, y: int) -> bool:
        pass

    # Class Methods End
