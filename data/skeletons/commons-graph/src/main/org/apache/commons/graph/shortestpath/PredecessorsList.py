from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
import pathlib

# Imports End


class PredecessorsList:

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __weightOperations: Monoid[typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __predecessors: typing.Dict[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def isEmpty(self) -> bool:
        pass

    def buildPath1(
        self,
        source: typing.Any,
        touch: typing.Any,
        target: typing.Any,
        backwardsList: PredecessorsList,
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def buildPath0(
        self, source: typing.Any, target: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def addPredecessor(self, tail: typing.Any, head: typing.Any) -> None:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
