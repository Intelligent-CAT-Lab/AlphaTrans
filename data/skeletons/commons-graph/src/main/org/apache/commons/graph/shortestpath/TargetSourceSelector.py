from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class TargetSourceSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def to(
        self, target: typing.Any
    ) -> ShortestPathAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingBelmannFord(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
