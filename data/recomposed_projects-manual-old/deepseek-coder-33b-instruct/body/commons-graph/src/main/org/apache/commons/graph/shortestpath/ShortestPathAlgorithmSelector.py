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

        # Your implementation here
        pass

    def applyingBidirectionalDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:

        # Your implementation here
        pass

    def applyingAStar(
        self, weightOperations: typing.Any
    ) -> HeuristicBuilder[typing.Any, typing.Any, typing.Any]:
        pass
