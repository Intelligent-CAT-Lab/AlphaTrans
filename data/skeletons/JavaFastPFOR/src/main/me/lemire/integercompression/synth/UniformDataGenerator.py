from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class UniformDataGenerator:

    # Class Fields Begin
    rand: random.Random = None
    # Class Fields End

    # Class Methods Begin
    def generateUniform(self, N: int, Max: int) -> typing.List[int]:
        pass

    @staticmethod
    def negate(x: typing.List[int], Max: int) -> typing.List[int]:
        pass

    def __init__(self, constructorId: int, seed: int) -> None:
        pass

    def generateUniformBitmap(self, N: int, Max: int) -> typing.List[int]:
        pass

    def generateUniformHash(self, N: int, Max: int) -> typing.List[int]:
        pass

    # Class Methods End
