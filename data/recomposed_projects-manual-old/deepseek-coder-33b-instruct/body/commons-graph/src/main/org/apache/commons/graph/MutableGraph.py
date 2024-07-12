from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class MutableGraph(ABC):

    def removeVertex(self, v: typing.Any) -> None:

        # Your implementation here
        pass

    def removeEdge(self, e: typing.Any) -> None:

        # Your implementation here
        pass

    def addVertex(self, v: typing.Any) -> None:
        pass

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:
        pass
