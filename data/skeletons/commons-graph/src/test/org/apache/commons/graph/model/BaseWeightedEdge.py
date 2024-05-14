# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.Mapper import *
import typing

# Imports End


class BaseWeightedEdge:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def map(self, edge: BaseLabeledWeightedEdge[typing.Any]) -> typing.Any:
        pass

    # Class Methods End
