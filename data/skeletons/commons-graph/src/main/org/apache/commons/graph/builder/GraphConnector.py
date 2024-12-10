from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class GraphConnector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def addVertex(self, node: typing.Any) -> typing.Any:
        pass

    def addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:
        pass

    # Class Methods End
