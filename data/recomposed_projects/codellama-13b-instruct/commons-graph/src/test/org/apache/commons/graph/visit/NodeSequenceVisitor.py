# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
import unittest
import typing
from typing import *

# Imports End


class NodeSequenceVisitor(unittest.TestCase):

    # Class Fields Begin
    __vertices: List[BaseLabeledVertex] = []
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> typing.List[BaseLabeledVertex]:

        return list(self.__vertices)

    def discoverVertex(self, vertex: BaseLabeledVertex) -> VisitState:

        self.__vertices.add(vertex)
        return VisitState.CONTINUE

    # Class Methods End
