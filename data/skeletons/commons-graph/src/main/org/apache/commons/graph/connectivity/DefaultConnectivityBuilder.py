from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class DefaultConnectivityBuilder(ConnectivityBuilder):

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def includingVertices(
        self, vertices: typing.List[typing.Any]
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        pass

    def includingAllVertices(
        self,
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
