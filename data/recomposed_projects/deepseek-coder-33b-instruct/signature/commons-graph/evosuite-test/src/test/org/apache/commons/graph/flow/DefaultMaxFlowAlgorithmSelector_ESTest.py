from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector import *

# from src.test.org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.LongWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultMaxFlowAlgorithmSelector_ESTest(unittest.TestCase):

    def test13(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            None,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        try:
            default_max_flow_algorithm_selector0.applying_edmonds_karp(
                long_weight_base_operations0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Vertex org.apache.commons.graph.weight.primitive.LongWeightBaseOperations@2 does not exist in the Graph
            self.verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test12(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        directed_mutable_graph0.add_vertex(long_weight_base_operations0)
        long0 = Long(0)
        directed_mutable_graph0.add_edge(
            long_weight_base_operations0, long0, long_weight_base_operations0
        )
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            None,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        try:
            default_max_flow_algorithm_selector0.applying_edmonds_karp(
                long_weight_base_operations0
            )
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verify_exception(
                "org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector$MapperWrapper",
                e,
            )

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        long_weight_base_operations1 = LongWeightBaseOperations()
        directed_mutable_graph0.add_vertex(long_weight_base_operations0)
        directed_mutable_graph0.add_vertex(long_weight_base_operations1)
        long0 = Long(1102)
        directed_mutable_graph0.add_edge(
            long_weight_base_operations0, long0, long_weight_base_operations1
        )
        mapper0 = Mock(Mapper)
        mapper0.map.return_value = None
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            mapper0,
            long_weight_base_operations1,
            long_weight_base_operations1,
        )
        default_max_flow_algorithm_selector0.applying_ford_fulkerson(
            long_weight_base_operations0
        )

    def test10(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        longWeightBaseOperations0 = LongWeightBaseOperations()
        directedMutableGraph0.addVertex(longWeightBaseOperations0)
        defaultMaxFlowAlgorithmSelector0 = DefaultMaxFlowAlgorithmSelector(
            directedMutableGraph0,
            None,
            longWeightBaseOperations0,
            longWeightBaseOperations0,
        )
        defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp(longWeightBaseOperations0)

    def test09(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0, None, None, None
        )

        try:
            default_max_flow_algorithm_selector0.applying_edmonds_karp(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test08(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        directed_mutable_graph0.add_vertex(long_weight_base_operations0)
        long0 = Long(3014)
        directed_mutable_graph0.add_edge(
            long_weight_base_operations0, long0, long_weight_base_operations0
        )
        directed_mutable_graph0.remove_vertex(long_weight_base_operations0)
        mapper0 = Mapper()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            mapper0,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        with pytest.raises(RuntimeError):
            default_max_flow_algorithm_selector0.applying_edmonds_karp(
                long_weight_base_operations0
            )

    def test07(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            None,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        try:
            default_max_flow_algorithm_selector0.applying_ford_fulkerson(
                long_weight_base_operations0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Vertex org.apache.commons.graph.weight.primitive.LongWeightBaseOperations@2 does not exist in the Graph
            self.verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test06(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0, None, None, None
        )

        try:
            default_max_flow_algorithm_selector0.applying_ford_fulkerson(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verify_exception("org.apache.commons.graph.utils.Assertions", e)

    def test05(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        directed_mutable_graph0.add_vertex(long_weight_base_operations0)
        long0 = Long(0)
        directed_mutable_graph0.add_edge(
            long_weight_base_operations0, long0, long_weight_base_operations0
        )
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            None,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        try:
            default_max_flow_algorithm_selector0.applying_ford_fulkerson(
                long_weight_base_operations0
            )
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verify_exception(
                "org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector$MapperWrapper",
                e,
            )

    def test04(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        long_weight_base_operations0 = LongWeightBaseOperations()
        directed_mutable_graph0.add_vertex(long_weight_base_operations0)
        long0 = Long(3014)
        directed_mutable_graph0.add_edge(
            long_weight_base_operations0, long0, long_weight_base_operations0
        )
        directed_mutable_graph0.remove_vertex(long_weight_base_operations0)
        mapper0 = Mapper()
        default_max_flow_algorithm_selector0 = DefaultMaxFlowAlgorithmSelector(
            directed_mutable_graph0,
            mapper0,
            long_weight_base_operations0,
            long_weight_base_operations0,
        )

        with pytest.raises(RuntimeError):
            default_max_flow_algorithm_selector0.applying_ford_fulkerson(
                long_weight_base_operations0
            )

    def test03(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.side_effect = ViolatedAssumptionAnswer()

        longWeightBaseOperations0 = LongWeightBaseOperations()

        directedMutableGraph0 = DirectedMutableGraph()
        long0 = Long(0)
        directedMutableGraph0.addVertex(long0)
        long1 = Long.getLong(None)

        defaultMaxFlowAlgorithmSelector0 = DefaultMaxFlowAlgorithmSelector(
            directedMutableGraph0, mapper0, long0, long1
        )

        orderedMonoid0 = Mock(spec=OrderedMonoid)
        orderedMonoid0.side_effect = ViolatedAssumptionAnswer()
        orderedMonoid0.identity.return_value = longWeightBaseOperations0

        orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp(
            orderedMonoid0
        )

        self.assertIs(longWeightBaseOperations0, orderedMonoid1)

    def test02(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.return_value = ViolatedAssumptionAnswer()

        directedMutableGraph0 = DirectedMutableGraph()
        long0 = Long(0)
        directedMutableGraph0.addVertex(long0)
        long1 = Long.getLong(None)

        defaultMaxFlowAlgorithmSelector0 = DefaultMaxFlowAlgorithmSelector(
            directedMutableGraph0, mapper0, long0, long1
        )

        orderedMonoid0 = Mock(spec=OrderedMonoid)
        orderedMonoid0.identity.return_value = None

        orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp(
            orderedMonoid0
        )

        self.assertIsNone(orderedMonoid1)

    def test01(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.side_effect = ViolatedAssumptionAnswer()

        longWeightBaseOperations0 = LongWeightBaseOperations()

        directedMutableGraph0 = DirectedMutableGraph()
        long0 = Long(0)
        directedMutableGraph0.addVertex(long0)
        long1 = Long.getLong(None)

        defaultMaxFlowAlgorithmSelector0 = DefaultMaxFlowAlgorithmSelector(
            directedMutableGraph0, mapper0, long0, long1
        )

        orderedMonoid0 = Mock(spec=OrderedMonoid)
        orderedMonoid0.side_effect = ViolatedAssumptionAnswer()
        orderedMonoid0.identity.return_value = longWeightBaseOperations0

        orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson(
            orderedMonoid0
        )

        self.assertIs(longWeightBaseOperations0, orderedMonoid1)

    def test00(self) -> None:

        mapper0 = Mock(spec=Mapper)
        mapper0.return_value = ViolatedAssumptionAnswer()

        directedMutableGraph0 = DirectedMutableGraph()
        long0 = Long(0)
        directedMutableGraph0.addVertex(long0)
        long1 = Long.getLong(None)

        defaultMaxFlowAlgorithmSelector0 = DefaultMaxFlowAlgorithmSelector(
            directedMutableGraph0, mapper0, long0, long1
        )

        orderedMonoid0 = Mock(spec=OrderedMonoid)
        orderedMonoid0.identity.return_value = None

        orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson(
            orderedMonoid0
        )

        self.assertIsNone(orderedMonoid1)
