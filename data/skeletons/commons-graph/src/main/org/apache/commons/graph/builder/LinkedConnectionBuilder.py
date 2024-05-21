from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class LinkedConnectionBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def withConnections(
        self, graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> typing.Any:
        pass

    # Class Methods End
