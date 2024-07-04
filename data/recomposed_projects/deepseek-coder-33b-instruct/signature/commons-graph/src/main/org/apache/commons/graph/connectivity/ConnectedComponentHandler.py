from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class ConnectedComponentHandler:

    __untouchedVertices: typing.List[typing.Any] = None

    __touchedVertices: typing.List[typing.Any] = []

    def onCompleted(self) -> typing.List[typing.Any]:
        return self.__touchedVertices

    def finishVertex(self, vertex: typing.Any) -> VisitState:

        if vertex in self.__untouchedVertices:
            self.__untouchedVertices.remove(vertex)

        self.__touchedVertices.append(vertex)

        return VisitState.CONTINUE

    def __init__(self, untouchedVertices: typing.List[typing.Any]) -> None:
        self.__untouchedVertices = untouchedVertices
