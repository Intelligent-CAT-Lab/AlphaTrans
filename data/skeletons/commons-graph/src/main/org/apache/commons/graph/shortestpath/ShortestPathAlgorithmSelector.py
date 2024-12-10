from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.WeightedPath import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class ShortestPathAlgorithmSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingBidirectionalDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingAStar(
        self, weightOperations: typing.Any
    ) -> HeuristicBuilder[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
