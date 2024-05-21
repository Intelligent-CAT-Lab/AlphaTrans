from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
import typing
from typing import *
import io

# Imports End


class ShortestDistances:

    # Class Fields Begin
    __distances: typing.Dict[typing.Any, typing.Any] = None
    __weightOperations: OrderedMonoid[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def setWeight(self, vertex: typing.Any, distance: typing.Any) -> None:
        pass

    def getWeight(self, vertex: typing.Any) -> typing.Any:
        pass

    def compare(self, left: typing.Any, right: typing.Any) -> int:
        pass

    def alreadyVisited(self, vertex: typing.Any) -> bool:
        pass

    def __init__(self, weightOperations: OrderedMonoid[typing.Any]) -> None:
        pass

    # Class Methods End
