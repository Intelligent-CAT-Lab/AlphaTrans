from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *


class CheriyanMehlhornGabowAlgorithm(SccAlgorithm):

    __sscCounter: int = 0
    __preorderCounter: int = 0
    __p: typing.List[typing.Any] = []
    __s: typing.List[typing.Any] = []
    __sscId: typing.Dict[typing.Any, int] = {}

    __preorder: typing.Dict[typing.Any, int] = {}

    __marked: typing.Set[typing.Any] = set()
    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        for vertex in self.__graph.getVertices0():
            if vertex not in self.__marked:
                self.__dfs(vertex)

        indexedSccComponents = []
        for i in range(self.__sscCounter):
            indexedSccComponents.append(set())

        for w in self.__graph.getVertices0():
            component = indexedSccComponents[self.__sscId.get(w)]
            component.add(w)

        scc = set()
        scc.update(indexedSccComponents)
        return scc

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__p = []
        self.__s = []
        self.__graph = graph

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
