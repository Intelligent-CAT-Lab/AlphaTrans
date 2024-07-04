from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *


class ConnectivityBuilder(ABC):

    def includingVertices(
        self, vertices: typing.List[typing.Any]
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        pass

    def includingAllVertices(
        self,
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:

        # Your implementation here
        pass
