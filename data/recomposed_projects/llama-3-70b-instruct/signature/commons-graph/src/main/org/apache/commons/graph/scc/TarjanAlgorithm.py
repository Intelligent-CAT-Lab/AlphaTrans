from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.scc.TarjanVertexMetaInfo import *


class TarjanAlgorithm(SccAlgorithm):

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo] = {}
        s: typing.List[typing.Any] = []
        stronglyConnectedComponents: typing.Set[typing.Set[typing.Any]] = set()
        index: int = 0

        for vertex in self.__graph.getVertices0():
            vertexMetaInfo: TarjanVertexMetaInfo = self.__getMetaInfo(
                vertex, verticesMetaInfo
            )
            stronglyConnectedComponent: typing.Set[typing.Any] = set()

            if vertexMetaInfo.hasUndefinedIndex():
                self.__strongConnect(
                    self.__graph,
                    vertex,
                    verticesMetaInfo,
                    s,
                    stronglyConnectedComponent,
                    index,
                )
                stronglyConnectedComponents.add(stronglyConnectedComponent)

        return stronglyConnectedComponents

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph

    @staticmethod
    def __strongConnect(
        graph: DirectedGraph[typing.Any, typing.Any],
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
        s: typing.List[typing.Any],
        stronglyConnectedComponent: typing.Set[typing.Any],
        index: int,
    ) -> None:
        vertexMetaInfo = TarjanAlgorithm.__getMetaInfo(vertex, verticesMetaInfo)
        vertexMetaInfo.setIndex(index)
        vertexMetaInfo.setLowLink(index)
        index += 1
        s.append(vertex)

        for adjacent in graph.getOutbound(vertex):
            adjacentMetaInfo = TarjanAlgorithm.__getMetaInfo(adjacent, verticesMetaInfo)
            if adjacentMetaInfo.hasUndefinedIndex():
                TarjanAlgorithm.__strongConnect(
                    graph,
                    adjacent,
                    verticesMetaInfo,
                    s,
                    stronglyConnectedComponent,
                    index,
                )
                vertexMetaInfo.setLowLink(
                    min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getLowLink())
                )
            elif adjacent in s:
                vertexMetaInfo.setLowLink(
                    min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getIndex())
                )

        if vertexMetaInfo.getLowLink() == vertexMetaInfo.getIndex():
            v = None
            while True:
                v = s.pop()
                stronglyConnectedComponent.add(v)
                if vertex == v:
                    break

    @staticmethod
    def __getMetaInfo(
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
    ) -> TarjanVertexMetaInfo:
        vertexMetaInfo = verticesMetaInfo.get(vertex)
        if vertexMetaInfo is None:
            vertexMetaInfo = TarjanVertexMetaInfo()
            verticesMetaInfo[vertex] = vertexMetaInfo
        return vertexMetaInfo
