from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.Mapper import *
import typing
from typing import *
import io

# Imports End


class BaseWeightedEdge:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def map_(self, edge: BaseLabeledWeightedEdge[typing.Any]) -> typing.Any:
        pass

    # Class Methods End
