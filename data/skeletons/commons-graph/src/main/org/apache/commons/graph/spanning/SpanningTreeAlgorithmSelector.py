from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.SpanningTree import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SpanningTreeAlgorithmSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingPrimAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingKruskalAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingBoruvkaAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
