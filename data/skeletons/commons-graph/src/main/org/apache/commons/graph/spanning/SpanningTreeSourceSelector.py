from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.SpanningTree import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SpanningTreeSourceSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def fromSource(
        self, source: typing.Any
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def fromArbitrarySource(
        self,
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingReverseDeleteAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
