from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class SpanningTreeSourceSelector(ABC):

    def fromSource(
        self, source: typing.Any
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        return SpanningTreeAlgorithmSelector(source)

    def fromArbitrarySource(
        self,
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        return SpanningTreeAlgorithmSelector()

    def applyingReverseDeleteAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        return ReverseDeleteSpanningTreeAlgorithmSelector().select(weightOperations)
