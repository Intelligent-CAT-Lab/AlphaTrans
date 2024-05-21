from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.SynchronizedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class SynchronizedDirectedGraph(DirectedGraph, SynchronizedGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    __directedGraph: DirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getOutDegree(self, v: typing.Any) -> int:
        pass

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getInDegree(self, v: typing.Any) -> int:
        pass

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def __init__(self, g: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
