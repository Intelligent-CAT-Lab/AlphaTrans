from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.SynchronizedGraph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class SynchronizedMutableGraph(MutableGraph, SynchronizedGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    __mutableGraph: MutableGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def removeVertex(self, v: typing.Any) -> None:
        pass

    def removeEdge(self, e: typing.Any) -> None:
        pass

    def addVertex(self, v: typing.Any) -> None:
        pass

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:
        pass

    def __init__(self, g: MutableGraph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
