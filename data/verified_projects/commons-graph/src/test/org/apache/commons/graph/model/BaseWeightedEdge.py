import pytest

from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import BaseLabeledWeightedEdge
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *


W = typing.TypeVar('W')


class BaseWeightedEdge(Mapper, typing.Generic[W]):

    __serialVersionUID: int = -2024378704087762740

    def map(self, edge: BaseLabeledWeightedEdge[W]) -> W:
        return edge.getWeight()
