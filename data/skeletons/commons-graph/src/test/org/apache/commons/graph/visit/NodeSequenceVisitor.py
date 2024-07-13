from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
import typing
from typing import *
import io

# Imports End


class NodeSequenceVisitor:

    # Class Fields Begin
    __vertices: typing.List[BaseLabeledVertex] = None
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> typing.List[BaseLabeledVertex]:
        pass

    def discoverVertex(self, vertex: BaseLabeledVertex) -> VisitState:
        pass

    # Class Methods End
