from __future__ import annotations
import time
import re
import mock
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector import *

# from src.test.org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultWeightedEdgesSelector_ESTest(unittest.TestCase):

    def test1(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultWeightedEdgesSelector0 = DefaultWeightedEdgesSelector(
            directedMutableGraph0
        )

        with pytest.raises(RuntimeError):
            defaultWeightedEdgesSelector0.whereEdgesHaveWeights(None)

    def test0(self) -> None:

        integer0 = int(350)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        defaultWeightedEdgesSelector0 = DefaultWeightedEdgesSelector(inMemoryPath0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        pathSourceSelector0 = defaultWeightedEdgesSelector0.whereEdgesHaveWeights(
            mapper0
        )
        assert pathSourceSelector0 is not None
