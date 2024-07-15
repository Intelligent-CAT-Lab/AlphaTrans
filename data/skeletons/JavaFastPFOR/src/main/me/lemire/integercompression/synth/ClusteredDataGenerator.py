from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.synth.UniformDataGenerator import *
import typing
from typing import *
import io

# Imports End


class ClusteredDataGenerator:

    # Class Fields Begin
    unidg: UniformDataGenerator = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    def generateClustered(self, N: int, Max: int) -> typing.List[int]:
        pass

    def __init__(self) -> None:
        pass

    def fillClustered(
        self, array: typing.List[int], offset: int, length: int, Min: int, Max: int
    ) -> None:
        pass

    def fillUniform(
        self, array: typing.List[int], offset: int, length: int, Min: int, Max: int
    ) -> None:
        pass

    # Class Methods End
