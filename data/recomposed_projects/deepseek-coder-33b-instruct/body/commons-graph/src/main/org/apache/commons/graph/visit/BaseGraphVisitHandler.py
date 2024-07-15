from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class BaseGraphVisitHandler(GraphVisitHandler):

    def onCompleted(self) -> typing.Any:
        return None

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        return VisitState.CONTINUE

    def finishGraph(self, graph: typing.Any) -> None:
        pass

    def finishEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        return VisitState.CONTINUE

    def discoverVertex(self, vertex: typing.Any) -> VisitState:
        return VisitState.CONTINUE

    def discoverGraph(self, graph: typing.Any) -> None:
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        return VisitState.CONTINUE
