from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedMutableGraph import *

# from src.test.org.apache.commons.graph.SynchronizedMutableGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class SynchronizedMutableGraph_ESTest(unittest.TestCase):

    def test4(self) -> None:

        # Create a mock object for MutableGraph
        mutableGraph0 = unittest.mock.Mock(spec=MutableGraph)

        # Create an instance of SynchronizedMutableGraph using the mock object
        synchronizedMutableGraph0 = SynchronizedMutableGraph(mutableGraph0)

        # Create an Integer object
        integer0 = Integer(-1)

        # Call the removeVertex method on the SynchronizedMutableGraph instance
        synchronizedMutableGraph0.removeVertex(integer0)

        # Assert that the order of the SynchronizedMutableGraph instance is 0
        self.assertEqual(0, synchronizedMutableGraph0.getOrder())

    def test1(self) -> None:

        synchronizedMutableGraph0 = SynchronizedMutableGraph[int, int](None)
        integer0 = 3805

        with pytest.raises(RuntimeError):
            synchronizedMutableGraph0.removeEdge(integer0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.SynchronizedMutableGraph", RuntimeError
        )
