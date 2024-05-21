from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ConnectivityBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def includingVertices(
        self, vertices: typing.List[typing.Any]
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        pass

    def includingAllVertices(
        self,
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        pass

    # Class Methods End
