from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *


class DirectedMutableGraph(DirectedGraph, BaseMutableGraph):

    __outbound: typing.Dict[typing.Any, typing.Set[typing.Any]] = {}

    __inbound: typing.Dict[typing.Any, typing.Set[typing.Any]] = {}

    __serialVersionUID: int = 630111985439492792

    def _decorateRemoveVertex(self, v: typing.Any) -> None:

        if v in self.__inbound:
            del self.__inbound[v]

        if v in self.__outbound:
            del self.__outbound[v]

    def _decorateRemoveEdge(self, e: typing.Any) -> None:

        vertices = self.getVertices1(e)
        self.__inbound[vertices.getTail()].remove(vertices.getHead())
        self.__outbound[vertices.getHead()].remove(vertices.getTail())

    def _decorateAddVertex(self, v: typing.Any) -> None:
        self.__inbound[v] = set()
        self.__outbound[v] = set()

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        if tail in self.__inbound:
            self.__inbound[tail].add(head)
        else:
            self.__inbound[tail] = {head}

        if head in self.__outbound:
            self.__outbound[head].add(tail)
        else:
            self.__outbound[head] = {tail}

    def getOutDegree(self, v: typing.Any) -> int:
        return len(self.__outbound.get(v, set()))

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.__outbound.get(v)

    def getInDegree(self, v: typing.Any) -> int:
        return len(self.__inbound.get(v, set()))

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.__inbound.get(v)

    def getDegree(self, v: typing.Any) -> int:
        return self.getInDegree(v) + self.getOutDegree(v)
