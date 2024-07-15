from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class SpanningTreeAlgorithmSelector(ABC):

    def applyingPrimAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        # Your implementation here
        pass

    def applyingKruskalAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        # Your implementation here
        pass

    def applyingBoruvkaAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        # Your implementation here
        pass
