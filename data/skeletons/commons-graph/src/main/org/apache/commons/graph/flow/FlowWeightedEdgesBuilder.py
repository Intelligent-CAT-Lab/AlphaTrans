from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class FlowWeightedEdgesBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> FromHeadBuilder[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
