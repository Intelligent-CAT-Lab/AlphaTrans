from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class BaseGraphVisitHandler(GraphVisitHandler):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> typing.Any:
        pass

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def finishGraph(self, graph: typing.Any) -> None:
        pass

    def finishEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        pass

    def discoverVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def discoverGraph(self, graph: typing.Any) -> None:
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        pass

    # Class Methods End
