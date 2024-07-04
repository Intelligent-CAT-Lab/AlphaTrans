from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.weight.Monoid import *


class InMemoryWeightedPath(InMemoryPath, WeightedPath):

    __weight: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: Monoid[typing.Any] = None

    __serialVersionUID: int = 7937494144459068796

    def toString(self) -> str:
        return "InMemoryPath [weigth={}, vertices={}, edges={}]".format(
            self.__weight, self.getVertices0(), self.getEdges()
        )

    def hashCode(self) -> int:

        prime = 31
        result = super().hashCode()
        result = prime * result + (0 if self.__weight is None else hash(self.__weight))
        return result

    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True

        if not super().equals(obj):
            return False

        if type(self) is not type(obj):
            return False

        other = typing.cast(
            InMemoryWeightedPath[typing.Any, typing.Any, typing.Any], obj
        )
        return Objects.eq(self.__weight, other.getWeight())

    def addConnectionInTail(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:

        super().addConnectionInTail(head, edge, tail)
        self.__increaseWeight(edge)

    def addConnectionInHead(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        super().addConnectionInHead(head, edge, tail)
        self.__increaseWeight(edge)

    def getWeight(self) -> typing.Any:
        return self.__weight

    def __init__(
        self,
        start: typing.Any,
        target: typing.Any,
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:

        super().__init__(start, target)
        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges

        self.__weight = weightOperations.identity()

    def __increaseWeight(self, edge: typing.Any) -> None:
        self.__weight = self.__weightOperations.append(
            self.__weightedEdges.map(edge), self.__weight
        )
