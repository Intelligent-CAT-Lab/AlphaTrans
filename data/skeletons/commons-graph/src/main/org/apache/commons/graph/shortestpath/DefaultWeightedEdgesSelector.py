from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.DefaultPathSourceSelector import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
import pathlib

# Imports End


class DefaultWeightedEdgesSelector(PathWeightedEdgesBuilder):

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> PathSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
