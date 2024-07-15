from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *


class VisitAlgorithmsSelector(ABC):

    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:

        # Your implementation here
        pass

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:

        # Your implementation here
        pass

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:

        # Your implementation here
        pass

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:

        # Your implementation here
        pass
