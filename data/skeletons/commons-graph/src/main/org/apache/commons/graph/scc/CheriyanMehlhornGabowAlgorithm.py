from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class CheriyanMehlhornGabowAlgorithm(SccAlgorithm):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    __marked: typing.Set[typing.Any] = None
    __preorder: typing.Dict[typing.Any, int] = None
    __sscId: typing.Dict[typing.Any, int] = None
    __s: typing.List[typing.Any] = None
    __p: typing.List[typing.Any] = None
    __preorderCounter: int = None
    __sscCounter: int = None
    # Class Fields End

    # Class Methods Begin
    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    def __dfs(self, vertex: typing.Any) -> None:
        pass

    # Class Methods End
