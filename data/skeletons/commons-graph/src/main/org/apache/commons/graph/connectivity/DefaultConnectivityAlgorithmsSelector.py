from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.ConnectedComponentHandler import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultConnectivityAlgorithmsSelector:

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __includedVertices: typing.Iterable[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def applyingMinimumSpanningTreeAlgorithm(
        self,
    ) -> typing.Collection[typing.List[typing.Any]]:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        includedVertices: typing.Iterable[typing.Any],
    ) -> None:
        pass

    # Class Methods End
