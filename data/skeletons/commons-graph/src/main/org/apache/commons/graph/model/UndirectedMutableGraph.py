from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
import typing
from typing import *
import io

# Imports End


class UndirectedMutableGraph(UndirectedGraph, BaseMutableGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def _decorateRemoveVertex(self, v: typing.Any) -> None:
        pass

    def _decorateRemoveEdge(self, e: typing.Any) -> None:
        pass

    def _decorateAddVertex(self, v: typing.Any) -> None:
        pass

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def getDegree(self, v: typing.Any) -> int:
        pass

    # Class Methods End
