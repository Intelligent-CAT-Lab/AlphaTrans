from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class NodeSequenceVisitor:

    __vertices: typing.List[BaseLabeledVertex] = []

    def onCompleted(self) -> typing.List[BaseLabeledVertex]:
        return unmodifiableList(self.__vertices)

    def discoverVertex(self, vertex: BaseLabeledVertex) -> VisitState:
        self.__vertices.append(vertex)
        return VisitState.CONTINUE

    def __init__(self) -> None:
        super().__init__()
