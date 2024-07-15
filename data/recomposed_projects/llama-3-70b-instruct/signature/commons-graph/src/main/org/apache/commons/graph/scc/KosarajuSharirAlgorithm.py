from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class KosarajuSharirAlgorithm(SccAlgorithm):

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform1(self, source: typing.Any) -> typing.Set[typing.Any]:

        pass  # LLM could not translate this method

    def perform0(self) -> typing.Set[typing.Set[typing.Any]]:
        visitedVertices: typing.Set[typing.Any] = set()
        expandedVertexList: typing.List[typing.Any] = self.__getExpandedVertexList(
            None, visitedVertices
        )
        reverted: DirectedGraph[typing.Any, typing.Any] = RevertedGraph(self.__graph)

        sccs: typing.Set[typing.Set[typing.Any]] = set()

        stack: typing.Set[typing.Any] = set()
        for i in range(len(expandedVertexList) - 1, -1, -1):
            stack.add(expandedVertexList[i])

        while len(stack) > 0:
            v: typing.Any = stack.pop()
            sccSet: typing.Set[typing.Any] = set()
            self.__searchRecursive(reverted, v, sccSet, visitedVertices, False)

            stack.difference_update(sccSet)
            sccs.add(sccSet)

        return sccs

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        return self.perform0()

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph

    def __searchRecursive(
        self,
        g: DirectedGraph[typing.Any, typing.Any],
        source: typing.Any,
        coll: typing.Collection[typing.Any],
        visited: typing.Set[typing.Any],
        forward: bool,
    ) -> None:

        pass  # LLM could not translate this method

    def __getExpandedVertexList(
        self, source: typing.Any, visitedVertices: typing.Set[typing.Any]
    ) -> typing.List[typing.Any]:
        size = 13 if source is not None else self.__graph.getOrder()
        vertices = set()
        if source is not None:
            vertices.add(source)
        else:
            for vertex in self.__graph.getVertices0():
                vertices.add(vertex)
        expandedVertexList = []
        idx = 0
        while len(vertices) > 0:
            v = vertices.pop()
            self.__searchRecursive(
                self.__graph, v, expandedVertexList, visitedVertices, True
            )
            vertices.difference_update(expandedVertexList[idx:])
            idx = len(expandedVertexList)
        return expandedVertexList
