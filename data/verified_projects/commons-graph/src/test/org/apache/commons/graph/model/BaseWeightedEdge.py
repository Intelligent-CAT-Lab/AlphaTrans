import pytest

# Imports Begin
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import BaseLabeledWeightedEdge
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *

# Imports End

W = typing.TypeVar('W')

class BaseWeightedEdge(Mapper, typing.Generic[W]):

    # Class Fields Begin
    __serialVersionUID: int = -2024378704087762740
    # Class Fields End

    # Class Methods Begin
    def map(self, edge: BaseLabeledWeightedEdge[W]) -> W:
        return edge.getWeight()

    # Class Methods End
