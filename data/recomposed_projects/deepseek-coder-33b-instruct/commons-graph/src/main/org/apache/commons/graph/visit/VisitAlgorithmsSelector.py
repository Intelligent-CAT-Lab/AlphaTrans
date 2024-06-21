from __future__ import annotations
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

        # Here you need to implement the logic of applying depth first search.
        # Since the Java code does not provide any implementation, I can't provide a direct translation.
        # You need to implement the logic of applying depth first search based on your requirements.

        pass

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:

        # Your implementation here
        pass

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:

        # Implementation of applyingBreadthFirstSearch0 method goes here
        # This is a placeholder and will depend on the specific implementation of the method in the Java code
        pass
