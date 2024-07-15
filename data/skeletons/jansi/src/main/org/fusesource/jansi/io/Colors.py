from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Colors:

    # Class Fields Begin
    __epsilon: float = None
    __kappa: float = None
    DEFAULT_COLORS_256: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def roundRgbColor(r: int, g: int, b: int, max_: int) -> int:
        pass

    @staticmethod
    def roundColor0(col: int, max_: int) -> int:
        pass

    @staticmethod
    def __sqr(n: float) -> float:
        pass

    @staticmethod
    def __pivotXyz(n: float) -> float:
        pass

    @staticmethod
    def __xyz2lab(xyz: typing.List[float]) -> typing.List[float]:
        pass

    @staticmethod
    def __pivotRgb(n: float) -> float:
        pass

    @staticmethod
    def __rgb2xyz(rgb: typing.List[float]) -> typing.List[float]:
        pass

    @staticmethod
    def __rgb2cielab1(rgb: typing.List[float]) -> typing.List[float]:
        pass

    @staticmethod
    def __rgb2cielab0(color: int) -> typing.List[float]:
        pass

    @staticmethod
    def __rgb(color: int) -> typing.List[float]:
        pass

    @staticmethod
    def __scalar(c1: typing.List[float], c2: typing.List[float]) -> float:
        pass

    @staticmethod
    def __cie76(c1: int, c2: int) -> float:
        pass

    @staticmethod
    def __roundColor1(color: int, colors: typing.List[int], max_: int) -> int:
        pass

    # Class Methods End
