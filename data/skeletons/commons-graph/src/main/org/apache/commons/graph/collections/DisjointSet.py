from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.collections.DisjointSetNode import *
import typing
from typing import *
import io

# Imports End


class DisjointSet:

    # Class Fields Begin
    __disjointSets: typing.Dict[typing.Any, DisjointSetNode[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def union(self, e1: typing.Any, e2: typing.Any) -> None:
        pass

    def find1(self, e: typing.Any) -> typing.Any:
        pass

    def __getNode(self, e: typing.Any) -> DisjointSetNode[typing.Any]:
        pass

    def __find0(self, node: DisjointSetNode[typing.Any]) -> DisjointSetNode[typing.Any]:
        pass

    # Class Methods End
