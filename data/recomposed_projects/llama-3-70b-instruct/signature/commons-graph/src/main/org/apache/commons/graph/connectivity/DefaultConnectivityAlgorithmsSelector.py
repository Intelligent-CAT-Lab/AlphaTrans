from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.connectivity.ConnectedComponentHandler import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *


class DefaultConnectivityAlgorithmsSelector:

    __includedVertices: typing.Iterable[typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def applyingMinimumSpanningTreeAlgorithm(
        self,
    ) -> typing.Collection[typing.List[typing.Any]]:

        pass  # LLM could not translate this method

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        includedVertices: typing.Iterable[typing.Any],
    ) -> None:
        self.__graph = graph
        self.__includedVertices = includedVertices
