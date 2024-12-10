from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractGraphConnection(GraphConnection, ABC):

    # Class Fields Begin
    __connector: GraphConnector[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def connect1(self, connector: GraphConnector[typing.Any, typing.Any]) -> None:
        pass

    def connect(self, connector: GraphConnector[typing.Any, typing.Any]) -> None:
        pass

    def _addVertex(self, node: typing.Any) -> typing.Any:
        pass

    def _addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:
        pass

    def connect0(self) -> None:
        pass

    # Class Methods End
