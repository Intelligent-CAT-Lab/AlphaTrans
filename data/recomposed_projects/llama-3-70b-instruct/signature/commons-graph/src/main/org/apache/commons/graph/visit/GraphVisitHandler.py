from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class GraphVisitHandler(ABC):

    def onCompleted(self) -> typing.Any:
        return None

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        return VisitState.FINISHED

    def finishGraph(self, graph: typing.Any) -> None:
        pass

    def finishEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        return VisitState.FINISH

    def discoverVertex(self, vertex: typing.Any) -> VisitState:
        return VisitState.CONTINUE

    def discoverGraph(self, graph: typing.Any) -> None:
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        return VisitState.CONTINUE
