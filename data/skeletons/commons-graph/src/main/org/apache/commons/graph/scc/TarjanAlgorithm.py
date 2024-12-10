from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.scc.TarjanVertexMetaInfo import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class TarjanAlgorithm(SccAlgorithm):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    @staticmethod
    def __strongConnect(
        graph: DirectedGraph[typing.Any, typing.Any],
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
        s: typing.List[typing.Any],
        stronglyConnectedComponent: typing.Set[typing.Any],
        index: int,
    ) -> None:
        pass

    @staticmethod
    def __getMetaInfo(
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
    ) -> TarjanVertexMetaInfo:
        pass

    # Class Methods End
