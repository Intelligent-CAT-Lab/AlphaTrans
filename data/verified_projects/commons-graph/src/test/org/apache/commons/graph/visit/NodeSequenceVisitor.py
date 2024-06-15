import pytest

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
import typing
from typing import *

# Imports End

class NodeSequenceVisitor(BaseGraphVisitHandler):
    def __init__(self):
        self.__vertices = []

    def discoverVertex(self, vertex: BaseLabeledVertex) -> VisitState:
        self.__vertices.append(vertex)
        return VisitState.CONTINUE

    def onCompleted(self) -> typing.List[BaseLabeledVertex]:
        return list(self.__vertices)
