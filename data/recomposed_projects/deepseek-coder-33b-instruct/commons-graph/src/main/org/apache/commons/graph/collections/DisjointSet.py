from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.collections.DisjointSetNode import *


class DisjointSet:

    __disjointSets: typing.Dict[typing.Any, DisjointSetNode[typing.Any]] = {}

    def union(self, e1: typing.Any, e2: typing.Any) -> None:

        e1Root = self.__find0(self.__getNode(e1))
        e2Root = self.__find0(self.__getNode(e2))

        if e1Root == e2Root:
            return

        comparison = e1Root.compareTo(e2Root)
        if comparison < 0:
            e1Root.setParent(e2Root)
        elif comparison > 0:
            e2Root.setParent(e1Root)
        else:
            e2Root.setParent(e1Root)
            e1Root.increaseRank()

    def find1(self, e: typing.Any) -> typing.Any:

        node = self.__find0(self.__getNode(e))

        if node == node.getParent():
            return node.getElement()

        node.setParent(self.__find0(node.getParent()))

        return node.getParent().getElement()

    def __getNode(self, e: typing.Any) -> DisjointSetNode[typing.Any]:

        node = self.__disjointSets.get(e)

        if node is None:
            node = DisjointSetNode(e)
            self.__disjointSets[e] = node

        return node

    def __find0(self, node: DisjointSetNode[typing.Any]) -> DisjointSetNode[typing.Any]:

        if node == node.getParent():
            return node
        else:
            return self.__find0(node.getParent())
