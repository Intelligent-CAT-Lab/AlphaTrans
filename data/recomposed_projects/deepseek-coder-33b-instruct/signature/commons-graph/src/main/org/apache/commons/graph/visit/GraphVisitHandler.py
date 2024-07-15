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
        pass

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def finishGraph(self, graph: typing.Any) -> None:

        # Your code here
        pass

    def finishEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:

        # Your implementation here
        pass

    def discoverVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def discoverGraph(self, graph: typing.Any) -> None:

        # Your implementation here
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        pass
