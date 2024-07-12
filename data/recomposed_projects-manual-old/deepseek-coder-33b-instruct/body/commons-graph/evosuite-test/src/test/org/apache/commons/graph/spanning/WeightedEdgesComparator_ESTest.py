from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *

# from src.test.org.apache.commons.graph.spanning.WeightedEdgesComparator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class WeightedEdgesComparator_ESTest(unittest.TestCase):

    def test3(self) -> None:

        toDoubleFunction0 = mock(ToDoubleFunction, ViolatedAssumptionAnswer())
        toDoubleFunction0.applyAsDouble = Mock(
            side_effect=[-555.198663509436, -555.198663509436]
        )
        comparator0 = Comparator.comparingDouble(toDoubleFunction0)
        integer0 = Integer(1)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(side_effect=[integer0, None])
        weightedEdgesComparator0 = WeightedEdgesComparator(comparator0, mapper0)
        int0 = weightedEdgesComparator0.compare(integer0, None)
        self.assertEqual(-1, int0)

    def test2(self) -> None:

        function0 = lambda x: x
        comparator0 = Comparator(function0)
        mapper0 = mock(Mapper)
        mapper0.map.side_effect = [None, None]
        weightedEdgesComparator0 = WeightedEdgesComparator(comparator0, mapper0)

        with pytest.raises(RuntimeError):
            weightedEdgesComparator0.compare(None, None)
            verifyException("java.util.Comparator", RuntimeError)

    def test1(self) -> None:

        toIntFunction0 = mock(ToIntFunction, ViolatedAssumptionAnswer())
        comparator0 = Comparator.comparingInt(toIntFunction0)
        comparator1 = Comparator.nullsLast(comparator0)
        integer0 = Integer(0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map.side_effect = [integer0, integer0]
        weightedEdgesComparator0 = WeightedEdgesComparator(comparator1, mapper0)
        int0 = weightedEdgesComparator0.compare(None, integer0)
        self.assertEqual(1, int0)

    def test0(self) -> None:

        toDoubleFunction0 = mock(ToDoubleFunction, ViolatedAssumptionAnswer())
        doReturn(0.0, 0.0).when(toDoubleFunction0).applyAsDouble(anyInt())
        comparator0 = Comparator.comparingDouble(toDoubleFunction0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        doReturn(None, None).when(mapper0).map(anyInt())
        weightedEdgesComparator0 = WeightedEdgesComparator(comparator0, mapper0)
        integer0 = Integer(0)
        int0 = weightedEdgesComparator0.compare(integer0, integer0)
        self.assertEqual(0, int0)
