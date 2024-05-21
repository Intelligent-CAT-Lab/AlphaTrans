from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class PathSourceSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def from_(
        self, source: typing.Any
    ) -> TargetSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingFloydWarshall(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
