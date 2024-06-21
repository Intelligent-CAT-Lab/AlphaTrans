from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class DirectedGraph(ABC):

    def getOutDegree(self, v: typing.Any) -> int:

        # The actual implementation of this method depends on the specific graph data structure used.
        # Here is a placeholder implementation.
        return 0

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        pass

    def getInDegree(self, v: typing.Any) -> int:

        # The actual implementation of this method depends on the specific graph data structure used.
        # Here is a placeholder implementation.
        # You need to replace it with the actual implementation.

        return 0

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        # The actual implementation of this method depends on the specific implementation of the DirectedGraph class.
        # Here is a placeholder implementation that returns an empty iterable.
        return iter(())
