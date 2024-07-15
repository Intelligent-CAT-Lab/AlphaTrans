from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class DirectedGraph(ABC):

    def getOutDegree(self, v: typing.Any) -> int:
        return self.getOutEdges(v).size()

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.getOutbound(v)

    def getInDegree(self, v: typing.Any) -> int:
        return self.getEdges(v).size()

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return (
            self.getEdges(v)
            .stream()
            .map(lambda e: e.getSource())
            .collect(Collectors.toList())
        )
