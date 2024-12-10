from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io

# Imports End


class MutableSpanningTree(UndirectedMutableGraph, SpanningTree):

    # Class Fields Begin
    __serialVersionUID: int = None
    __weightOperations: Monoid[typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __weight: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def _decorateRemoveEdge(self, e: typing.Any) -> None:
        pass

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def getWeight(self) -> typing.Any:
        pass

    def __init__(
        self,
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
