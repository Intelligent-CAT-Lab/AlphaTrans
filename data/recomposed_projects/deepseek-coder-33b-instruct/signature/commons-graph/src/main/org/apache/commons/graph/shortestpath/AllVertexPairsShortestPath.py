from __future__ import annotations
import re
import os
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class AllVertexPairsShortestPath:

    __weightOperations: OrderedMonoid[typing.Any] = None

    __shortestDistances: typing.Dict[VertexPair[typing.Any], typing.Any] = {}

    __paths: typing.Dict[
        VertexPair[typing.Any], WeightedPath[typing.Any, typing.Any, typing.Any]
    ] = {}

    def toString(self) -> str:
        return str(self.__shortestDistances)

    def findShortestPath(
        self, source: typing.Any, target: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:

        source = Assertions.checkNotNull(
            source, "Impossible to add a shortest path from a null source"
        )
        target = Assertions.checkNotNull(
            target, "Impossible to add a shortest path to a null target"
        )

        path = self.__paths.get(VertexPair(source, target))

        if path is None:
            raise PathNotFoundException(
                "Path from '%s' to '%s' doesn't exist" % (source, target)
            )

        return path

    def hasShortestDistance(self, source: typing.Any, target: typing.Any) -> bool:

        source = Assertions.checkNotNull(
            source, "Impossible to add a shortest path from a null source"
        )
        target = Assertions.checkNotNull(
            target, "Impossible to add a shortest path to a null target"
        )

        if source == target:
            return True

        return (source, target) in self.__shortestDistances

    def getShortestDistance(self, source: typing.Any, target: typing.Any) -> typing.Any:

        source = Assertions.checkNotNull(
            source, "Impossible to add a shortest path from a null source"
        )
        target = Assertions.checkNotNull(
            target, "Impossible to add a shortest path to a null target"
        )

        if source == target:
            return self.__weightOperations.identity()

        return self.__shortestDistances.get(VertexPair(source, target))

    def addShortestPath(
        self,
        source: typing.Any,
        target: typing.Any,
        weightedPath: WeightedPath[typing.Any, typing.Any, typing.Any],
    ) -> None:

        source = Assertions.checkNotNull(
            source, "Impossible to add a shortest path from a null source"
        )
        target = Assertions.checkNotNull(
            target, "Impossible to add a shortest path to a null target"
        )
        weightedPath = Assertions.checkNotNull(
            weightedPath, "Impossible to add a null weightedPath path to a null target"
        )

        self.__paths[VertexPair(source, target)] = weightedPath

    def addShortestDistance(
        self, source: typing.Any, target: typing.Any, distance: typing.Any
    ) -> None:

        source = Assertions.checkNotNull(
            source, "Impossible to add a shortest path from a null source"
        )
        target = Assertions.checkNotNull(
            target, "Impossible to add a shortest path to a null target"
        )
        distance = Assertions.checkNotNull(
            distance, "Impossible to add a shortest distance with a null distance"
        )

        self.__shortestDistances[VertexPair(source, target)] = distance

    def __init__(self, weightOperations: OrderedMonoid[typing.Any]) -> None:
        self.__weightOperations = weightOperations
