from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class DirectedGraph(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getOutDegree(self, v: typing.Any) -> int:
        pass

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getInDegree(self, v: typing.Any) -> int:
        pass

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    # Class Methods End
