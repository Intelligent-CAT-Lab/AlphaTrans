from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DirectedMutableGraph(DirectedGraph, BaseMutableGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    __inbound: typing.Dict[typing.Any, typing.Set[typing.Any]] = None
    __outbound: typing.Dict[typing.Any, typing.Set[typing.Any]] = None
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

    def getOutDegree(self, v: typing.Any) -> int:
        pass

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getInDegree(self, v: typing.Any) -> int:
        pass

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getDegree(self, v: typing.Any) -> int:
        pass

    # Class Methods End
