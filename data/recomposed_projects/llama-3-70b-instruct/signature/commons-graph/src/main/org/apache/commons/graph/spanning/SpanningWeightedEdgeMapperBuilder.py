from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *


class SpanningWeightedEdgeMapperBuilder(ABC):

    def whereEdgesHaveWeights(
        self, weightedEdges: Mapper[typing.Any, typing.Any]
    ) -> SpanningTreeSourceSelector[typing.Any, typing.Any, typing.Any]:
        return SpanningTreeSourceSelector(weightedEdges)
