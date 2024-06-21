from __future__ import annotations
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class TargetSourceSelector(ABC):

    def to(
        self, target: typing.Any
    ) -> ShortestPathAlgorithmSelector[typing.Any, typing.Any, typing.Any]:

        pass

    def applyingBelmannFord(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:

        # TODO: Implement the method here
        pass
