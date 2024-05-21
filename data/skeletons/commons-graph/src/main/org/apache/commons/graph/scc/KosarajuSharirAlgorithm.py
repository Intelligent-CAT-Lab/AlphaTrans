from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import os
import typing
from typing import *
import io

# Imports End


class KosarajuSharirAlgorithm(SccAlgorithm):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def perform1(self, source: typing.Any) -> typing.Set[typing.Any]:
        pass

    def perform0(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    def __searchRecursive(
        self,
        g: DirectedGraph[typing.Any, typing.Any],
        source: typing.Any,
        coll: typing.Collection[typing.Any],
        visited: typing.Set[typing.Any],
        forward: bool,
    ) -> None:
        pass

    def __getExpandedVertexList(
        self, source: typing.Any, visitedVertices: typing.Set[typing.Any]
    ) -> typing.List[typing.Any]:
        pass

    # Class Methods End
