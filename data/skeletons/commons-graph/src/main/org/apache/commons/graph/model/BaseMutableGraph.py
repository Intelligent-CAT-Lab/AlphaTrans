from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.model.BaseGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class BaseMutableGraph(MutableGraph, BaseGraph, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def removeVertex(self, v: typing.Any) -> None:
        pass

    def removeEdge(self, e: typing.Any) -> None:
        pass

    def _internalRemoveEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def _internalAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def addVertex(self, v: typing.Any) -> None:
        pass

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:
        pass

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

    # Class Methods End
