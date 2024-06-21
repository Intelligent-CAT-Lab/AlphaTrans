from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *


class CheriyanMehlhornGabowAlgorithm(SccAlgorithm):

    __sscCounter: int = 0

    __preorderCounter: int = 0

    __p: List[Any] = []

    __s: List[Any] = []

    __sscId: typing.Dict[typing.Any, int] = {}

    __preorder: typing.Dict[typing.Any, int] = {}

    __marked: typing.Set[typing.Any] = set()
    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:

        for vertex in self._graph.getVertices0():
            if vertex not in self._marked:
                self.__dfs(vertex)

        indexed_scc_components = [set() for _ in range(self.__sscCounter)]

        for w in self._graph.getVertices0():
            component = indexed_scc_components[self.__sscId[w]]
            component.add(w)

        scc = set(indexed_scc_components)
        return scc

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:

        self.__graph = graph
        self.__p = []
        self.__s = []

    def __dfs(self, vertex: typing.Any) -> None:

        self.__marked.add(vertex)
        self.__preorder[vertex] = self.__preorderCounter
        self.__preorderCounter += 1
        self.__s.append(vertex)
        self.__p.append(vertex)
        for w in self.__graph.getConnectedVertices(vertex):
            if w not in self.__marked:
                self.__dfs(w)
            elif self.__sscId.get(w) is None:
                while self.__preorder[self.__p[-1]] > self.__preorder[w]:
                    self.__p.pop()

        if self.__p[-1] == vertex:
            self.__p.pop()
            w = None
            while True:
                w = self.__s.pop()
                self.__sscId[w] = self.__sscCounter
                if vertex == w:
                    break
            self.__sscCounter += 1
