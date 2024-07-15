import pytest

from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.Mapper import *
import unittest

class EdgeWeightMapper(Mapper):

    __serialVersionUID: int = 20120728

    def map(self, input: BaseLabeledWeightedEdge[float]) -> float:
        return input.getWeight()
