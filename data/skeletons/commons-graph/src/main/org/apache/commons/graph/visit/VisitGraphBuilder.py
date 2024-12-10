from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class VisitGraphBuilder(BaseGraphVisitHandler):

    # Class Fields Begin
    __visitGraph: BaseMutableGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> Graph[typing.Any, typing.Any]:
        pass

    def discoverGraph(self, graph: typing.Any) -> None:
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        pass

    # Class Methods End
