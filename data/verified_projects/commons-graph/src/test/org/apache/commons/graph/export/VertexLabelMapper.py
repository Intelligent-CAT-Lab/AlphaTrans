# Imports Begin
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.Mapper import *
import unittest
# Imports End

class VertexLabelMapper(Mapper):

    # Class Fields Begin
    __serialVersionUID: int = 20120728
    # Class Fields End

    # Class Methods Begin
    def map(self, input: BaseLabeledVertex) -> str:
        return input.getLabel()

    # Class Methods End


