from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *


class GraphConnector(ABC):

    def addVertex(self, node: typing.Any) -> typing.Any:
        return node

    def addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:
        pass
