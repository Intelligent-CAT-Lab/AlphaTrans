from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class ShortestPathAlgorithmSelector(ABC):

    def applyingDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        return DijkstraShortestPathAlgorithm(weightOperations).apply(self)

    def applyingBidirectionalDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        return BidirectionalDijkstraShortestPathAlgorithm(weightOperations).apply(self)

    def applyingAStar(
        self, weightOperations: typing.Any
    ) -> HeuristicBuilder[typing.Any, typing.Any, typing.Any]:
        return HeuristicBuilder(weightOperations)
