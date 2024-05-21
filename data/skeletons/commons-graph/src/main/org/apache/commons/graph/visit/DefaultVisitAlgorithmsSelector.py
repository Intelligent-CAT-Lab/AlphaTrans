from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.VisitGraphBuilder import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultVisitAlgorithmsSelector(VisitAlgorithmsSelector):

    # Class Fields Begin
    __graph: typing.Any = None
    __source: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        pass

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        pass

    def __init__(self, graph: typing.Any, source: typing.Any) -> None:
        pass

    def __applyingSearch(
        self,
        handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any],
        enqueue: bool,
    ) -> typing.Any:
        pass

    # Class Methods End
