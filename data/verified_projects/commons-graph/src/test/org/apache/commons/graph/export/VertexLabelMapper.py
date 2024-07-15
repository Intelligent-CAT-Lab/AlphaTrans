import pytest

from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.Mapper import *
import unittest


class VertexLabelMapper(Mapper):

    __serialVersionUID: int = 20120728

    def map(self, input: BaseLabeledVertex) -> str:
        return input.getLabel()
