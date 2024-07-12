from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *


class UndirectedMutableGraph(UndirectedGraph, BaseMutableGraph):

    __serialVersionUID: int = 3067145277295525946

    def _decorateRemoveVertex(self, v: typing.Any) -> None:
        pass

    def _decorateRemoveEdge(self, e: typing.Any) -> None:

        self._internalRemoveEdge(
            self._getVertices1(e).getTail(), e, self._getVertices1(e).getHead()
        )

    def _decorateAddVertex(self, v: typing.Any) -> None:
        pass

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        self._internalAddEdge(tail, e, head)

    def getDegree(self, v: typing.Any) -> int:
        return len(self.getAdjacencyList().get(v))
