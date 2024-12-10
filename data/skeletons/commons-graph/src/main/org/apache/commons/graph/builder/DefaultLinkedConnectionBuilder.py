from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.DefaultGrapher import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultLinkedConnectionBuilder(LinkedConnectionBuilder):

    # Class Fields Begin
    __graph: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def withConnections(
        self, graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    def __init__(self, graph: typing.Any) -> None:
        pass

    # Class Methods End
