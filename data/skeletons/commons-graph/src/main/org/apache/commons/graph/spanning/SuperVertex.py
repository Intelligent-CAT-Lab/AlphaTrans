from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class SuperVertex:

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __vertices: typing.Set[typing.Any] = None
    __orderedEdges: typing.Set[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def merge(self, other: SuperVertex) -> None:
        pass

    def iterator(self) -> typing.Iterator[typing.Any]:
        pass

    def getMinimumWeightEdge(self) -> typing.Any:
        pass

    def __init__(
        self,
        source: typing.Any,
        graph: Graph[typing.Any, typing.Any],
        weightComparator: WeightedEdgesComparator[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
