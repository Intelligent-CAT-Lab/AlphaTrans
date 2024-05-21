from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.DefaultToTailBuilder import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultFromHeadBuilder(FromHeadBuilder):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def from_(
        self, head: typing.Any
    ) -> ToTailBuilder[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
