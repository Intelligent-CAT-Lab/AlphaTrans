from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class AbstractGraphConnection(GraphConnection, ABC):

    __connector: GraphConnector[typing.Any, typing.Any] = None

    def connect1(self, connector: GraphConnector[typing.Any, typing.Any]) -> None:
        checkState(self.__connector == None, "Re-entry not allowed!")
        self.__connector = connector

        try:
            self.connect0()
        finally:
            self.__connector = None

    def connect(self, connector: GraphConnector[typing.Any, typing.Any]) -> None:
        self.connect1(connector)

    def _addVertex(self, node: typing.Any) -> typing.Any:
        return self.__connector.addVertex(node)

    def _addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:
        return self.__connector.addEdge(arc)

    def connect0(self) -> None:
        pass
