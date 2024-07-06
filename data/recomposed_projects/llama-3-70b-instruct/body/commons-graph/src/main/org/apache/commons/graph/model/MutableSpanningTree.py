from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *


class MutableSpanningTree(UndirectedMutableGraph, SpanningTree):

    __weight: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: Monoid[typing.Any] = None

    __serialVersionUID: int = -4371938772248573879

    def _decorateRemoveEdge(self, e: typing.Any) -> None:
        self.__weight = self.__weightOperations.append(
            self.__weight, self.__weightOperations.inverse(self.__weightedEdges.map(e))
        )

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        super()._decorateAddEdge(head, e, tail)
        self.__weight = self.__weightOperations.append(
            self.__weight, self.__weightedEdges.map(e)
        )

    def getWeight(self) -> typing.Any:
        return self.__weight

    def __init__(
        self,
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges
        self.__weight = weightOperations.identity()
