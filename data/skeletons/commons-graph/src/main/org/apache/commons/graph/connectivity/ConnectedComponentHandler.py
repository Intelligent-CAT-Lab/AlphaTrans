from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class ConnectedComponentHandler:

    # Class Fields Begin
    __touchedVertices: typing.List[typing.Any] = None
    __untouchedVertices: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> typing.List[typing.Any]:
        pass

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def __init__(self, untouchedVertices: typing.List[typing.Any]) -> None:
        pass

    # Class Methods End
