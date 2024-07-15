from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *


class FlowWeightedEdgesBuilder(ABC):

    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> FromHeadBuilder[typing.Any, typing.Any, typing.Any]:
        return FromHeadBuilder(self, weightedEdges)
