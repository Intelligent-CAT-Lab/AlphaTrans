from __future__ import annotations
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

        pass

    def fromArbitrarySource(
        self,
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:

        pass

    def applyingReverseDeleteAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        # Your code here
        pass
