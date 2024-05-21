from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.DefaultHeadVertexConnector import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultGrapher(GraphConnector):

    # Class Fields Begin
    __graph: MutableGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def addVertex(self, node: typing.Any) -> typing.Any:
        pass

    def addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:
        pass

    def __init__(self, graph: MutableGraph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
