from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class PathWeightedEdgesBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> PathSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
