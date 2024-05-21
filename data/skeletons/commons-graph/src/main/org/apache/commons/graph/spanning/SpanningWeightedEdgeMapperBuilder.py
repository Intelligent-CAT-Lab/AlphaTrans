from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SpanningWeightedEdgeMapperBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def whereEdgesHaveWeights(
        self, weightedEdges: Mapper[typing.Any, typing.Any]
    ) -> SpanningTreeSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
