from __future__ import annotations
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

        checkNotNull(
            source,
            "Kosaraju Sharir algorithm cannot be calculated without expressing the source"
            + " vertex",
        )
        checkState(
            self.__graph.containsVertex(source),
            "Vertex %s does not exist in the Graph",
            source,
        )

        visitedVertices = set()
        expandedVertexList = self.__getExpandedVertexList(source, visitedVertices)
        reverted = RevertedGraph(self.__graph)

        v = expandedVertexList.pop()
        sccSet = set()
        self.__searchRecursive(reverted, v, sccSet, visitedVertices, False)
        return sccSet

    def perform0(self) -> typing.Set[typing.Set[typing.Any]]:

        visited_vertices = set()
        expanded_vertex_list = self.__getExpandedVertexList(None, visited_vertices)
        reverted = RevertedGraph(self.__graph)

        sccs = set()

        stack = set(expanded_vertex_list)

        while len(stack) > 0:
            v = next(iter(stack))
            scc_set = set()
            self.__searchRecursive(reverted, v, scc_set, visited_vertices, False)

            stack = stack - scc_set
            sccs.add(scc_set)

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

        stack = []
        stack.append(source)

        while stack:
            v = stack.pop()

            if not (forward ^ (v in visited)):
                coll.add(v)
                continue

            stack.append(v)
            if forward:
                visited.add(v)
            else:
                visited.remove(v)

            for w in g.getOutbound(v):
                if not (forward ^ (w not in visited)):
                    stack.append(w)

    def __getExpandedVertexList(
        self, source: typing.Any, visitedVertices: typing.Set[typing.Any]
    ) -> typing.List[typing.Any]:

        size = len(self.__graph.getVertices0()) if source is None else 13
        vertices = set(self.__graph.getVertices0()) if source is None else {source}

        expandedVertexList = []

        while vertices:
            v = next(iter(vertices))
            self.__searchRecursive(
                self.__graph, v, expandedVertexList, visitedVertices, True
            )
            vertices.difference_update(
                expandedVertexList[len(expandedVertexList) - len(vertices) :]
            )

        return expandedVertexList
