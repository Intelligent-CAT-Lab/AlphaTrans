from __future__ import annotations
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.shortestpath.DefaultPathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultWeightedEdgesSelector(PathWeightedEdgesBuilder):

    __graph: Graph[typing.Any, typing.Any] = None

    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> PathSourceSelector[typing.Any, typing.Any, typing.Any]:

        # Calling the checkNotNull method from Assertions class
        weightedEdges = Assertions.checkNotNull(
            weightedEdges, "Function to calculate edges weight can not be null."
        )

        return DefaultPathSourceSelector(self.__graph, weightedEdges)

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:

        self.__graph = graph
