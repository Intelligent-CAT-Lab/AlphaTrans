from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.VertexPair import *
import typing
from typing import *
import io
import pathlib

# Imports End


class AllVertexPairsShortestPath:

    # Class Fields Begin
    __paths: typing.Dict[
        VertexPair[typing.Any], WeightedPath[typing.Any, typing.Any, typing.Any]
    ] = None
    __shortestDistances: typing.Dict[VertexPair[typing.Any], typing.Any] = None
    __weightOperations: OrderedMonoid[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def findShortestPath(
        self, source: typing.Any, target: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def hasShortestDistance(self, source: typing.Any, target: typing.Any) -> bool:
        pass

    def getShortestDistance(self, source: typing.Any, target: typing.Any) -> typing.Any:
        pass

    def addShortestPath(
        self,
        source: typing.Any,
        target: typing.Any,
        weightedPath: WeightedPath[typing.Any, typing.Any, typing.Any],
    ) -> None:
        pass

    def addShortestDistance(
        self, source: typing.Any, target: typing.Any, distance: typing.Any
    ) -> None:
        pass

    def __init__(self, weightOperations: OrderedMonoid[typing.Any]) -> None:
        pass

    # Class Methods End
