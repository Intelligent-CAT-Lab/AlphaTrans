# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.Mapper import *
import unittest
import typing
from typing import *

# Imports End


class BaseWeightedEdge(unittest.TestCase):

    # Class Fields Begin
    __serialVersionUID: int = -2024378704087762740
    # Class Fields End

    # Class Methods Begin
    def map(self, edge: BaseLabeledWeightedEdge[typing.Any]) -> typing.Any:

        return edge.getWeight()

    # Class Methods End
