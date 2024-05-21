from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io
import pathlib

# Imports End


class InMemoryWeightedPath(InMemoryPath, WeightedPath):

    # Class Fields Begin
    __serialVersionUID: int = None
    __weightOperations: Monoid[typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __weight: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def addConnectionInTail(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def addConnectionInHead(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def getWeight(self) -> typing.Any:
        pass

    def __init__(
        self,
        start: typing.Any,
        target: typing.Any,
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    def __increaseWeight(self, edge: typing.Any) -> None:
        pass

    # Class Methods End
