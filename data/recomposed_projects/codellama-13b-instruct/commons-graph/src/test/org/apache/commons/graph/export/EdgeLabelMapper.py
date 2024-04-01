# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.Mapper import *
import unittest
# Imports End

class EdgeLabelMapper(unittest.TestCase, Mapper<BaseLabeledWeightedEdge<Double>,String>):

    # Class Fields Begin
    __serialVersionUID: int = 20120728
    # Class Fields End

    # Class Methods Begin
    def map(self, input: BaseLabeledWeightedEdge[float]) -> str:

            return input.getLabel()

    # Class Methods End


