from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.graph.Mapper import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *


class VertexLabelMapper(Mapper):

    __serialVersionUID: int = 20120728

    def map(self, input: BaseLabeledVertex) -> str:
        return input.getLabel()
