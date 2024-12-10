from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class MutableGraph(ABC):

    # Class Fields Begin
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

    # Class Methods End
