from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *


class DefaultVisitSourceSelector(VisitSourceSelector):

    __graph: typing.Any = None

    def from_(
        self, source: typing.Any
    ) -> VisitAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        source = Assertions.checkNotNull(
            source, "Impossible to visit input graph %s with null source", self.__graph
        )
        Assertions.checkState(
            self.__graph.containsVertex(source),
            "Vertex %s does not exist in the Graph",
            source,
        )
        return DefaultVisitAlgorithmsSelector(self.__graph, source)

    def __init__(self, graph: typing.Any) -> None:
        self.__graph = graph
