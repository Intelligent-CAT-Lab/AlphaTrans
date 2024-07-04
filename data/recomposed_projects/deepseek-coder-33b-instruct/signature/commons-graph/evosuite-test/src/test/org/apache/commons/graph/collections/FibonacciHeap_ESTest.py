from __future__ import annotations
import time
import re
import mock
import collections
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.collections.FibonacciHeap import *
from src.main.org.apache.commons.graph.collections.FibonacciHeapNode import *

# from src.test.org.apache.commons.graph.collections.FibonacciHeap_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class FibonacciHeap_ESTest(unittest.TestCase):

    def test45(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        list0 = [
            "",
            "",
            "org.apache.commons.graph.utils.Assertions",
            "",
            "",
            "",
            "",
            "",
        ]

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.removeAll(list0)
            self.fail("Expecting exception: NotImplementedError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", NotImplementedError
        )

    def test44(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        fibonacciHeap0.offer("%^<[9a`RG/[|wVh1M")
        list0 = [
            "]nm[.`[1I ` 2FB+",
            "%^<[9a`RG/[|wVh1M",
            "%^<[9a`RG/[|wVh1M",
            "org.apache.commons.graph.collections.FibonacciHeapNode",
            "%^<[9a`RG/[|wVh1M",
            "%^<[9a`RG/[|wVh1M",
            "%^<[9a`RG/[|wVh1M",
            "org.apache.commons.graph.collections.FibonacciHeapNode",
        ]
        fibonacciHeap0.addAll(list0)
        fibonacciHeap0.poll()
        fibonacciHeap0.remove()
        self.assertFalse(fibonacciHeap0.isEmpty())

    def test43(self) -> None:

        fibonacciHeap0 = FibonacciHeap[FibonacciHeap[object]](None)
        objectArray0 = [None] * 0

        try:
            fibonacciHeap0.toArray(objectArray0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.apache.commons.graph.collections.FibonacciHeap", e)

    def test42(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        int0 = fibonacciHeap0.potential()
        self.assertEqual(0, int0)
        self.assertEqual(0, fibonacciHeap0.size())

    def test41(self) -> None:

        fibonacciHeap0 = FibonacciHeap[str](None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.remove(None)
            self.fail("Expecting exception: NotImplementedError")

    def test40(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.addAll(fibonacciHeap0)
            self.fail("Expecting exception: NotImplementedError")

    def test39(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        int0 = fibonacciHeap0.size()
        self.assertEqual(0, fibonacciHeap0.potential())
        self.assertEqual(0, int0)

    def test38(self) -> None:

        fibonacciHeap0 = FibonacciHeap[str](None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.toArray()
            self.fail("Expecting exception: NotImplementedError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", NotImplementedError
        )

    def test37(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.remove()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", RuntimeError
        )

    def test36(self) -> None:

        fibonacciHeap0 = FibonacciHeap.FibonacciHeap1()

        comparator0 = unittest.mock.Mock(spec=Comparator)
        comparator0.compare.return_value = 0

        fibonacciHeap1 = FibonacciHeap(comparator0)
        fibonacciHeap1.offer(fibonacciHeap0)
        boolean0 = fibonacciHeap1.add(fibonacciHeap0)

        self.assertEqual(2, fibonacciHeap1.size())
        self.assertTrue(boolean0)

    def test35(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.clear()
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertEqual(0, fibonacciHeap0.potential())

    def test34(self) -> None:

        fibonacciHeap0 = FibonacciHeap[FibonacciHeapNode[str]](None)
        linkedList0 = LinkedList[object]()

        try:
            fibonacciHeap0.retainAll(linkedList0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.apache.commons.graph.collections.FibonacciHeap", e)

    def test33(self) -> None:

        list0 = [
            "",
            "FibonacciHeap=[",
            "FibonacciHeap=[",
            "",
            "",
            "",
            "U`'?k+",
            "org.apache.commons.graph.utils.Assertions",
        ]
        fibonacciHeap0 = FibonacciHeap[object](None)
        fibonacciHeap0.addAll(list0)
        fibonacciHeap0.poll()
        fibonacciHeap0.toString()
        self.assertTrue(
            fibonacciHeap0.contains("org.apache.commons.graph.utils.Assertions")
        )

    def test32(self) -> None:

        list0 = [
            "",
            "FibonacciHeap=[",
            "FibonacciHeap=[",
            "",
            "",
            "",
            "U`'?k+",
            "org.apache.commons.graph.utils.Assertions",
        ]
        fibonacciHeap0 = FibonacciHeap[FibonacciHeapNode[str]](None)
        boolean0 = fibonacciHeap0.containsAll(list0)
        self.assertEqual(0, fibonacciHeap0.potential())
        self.assertFalse(boolean0)
        self.assertEqual(0, fibonacciHeap0.size())

    def test31(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        boolean0 = fibonacciHeap0.contains(None)
        self.assertEqual(0, fibonacciHeap0.potential())
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertFalse(boolean0)

    def test30(self) -> None:

        list0 = [
            "",
            "FibonacciHeap=[",
            "FibonacciHeap=[",
            "",
            "",
            "",
            "U`'?k+",
            "org.apache.commons.graph.utils.Assertions",
        ]
        fibonacciHeap0 = FibonacciHeap[object](None)
        fibonacciHeap0.addAll(list0)
        boolean0 = fibonacciHeap0.contains("U`'?k+")
        self.assertFalse(fibonacciHeap0.isEmpty())
        self.assertTrue(boolean0)

    def test29(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        boolean0 = fibonacciHeap0.containsAll(None)
        self.assertEqual(0, fibonacciHeap0.potential())
        self.assertFalse(boolean0)
        self.assertEqual(0, fibonacciHeap0.size())

    def test28(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        list0 = [
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
            "U`'?k+",
        ]
        fibonacciHeap0.addAll(list0)
        boolean0 = fibonacciHeap0.containsAll(list0)
        self.assertFalse(fibonacciHeap0.isEmpty())
        self.assertTrue(boolean0)

    def test27(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        list0 = ["", "", ", ", "UX'V`.x|", "UX'V`.x|", "", "", "-?"]
        for item in list0:
            fibonacciHeap0.add(item)
        fibonacciHeap0.element()
        self.assertEqual(8, fibonacciHeap0.size())

    def test26(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.element()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", RuntimeError
        )

    def test25(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.peek()
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertEqual(0, fibonacciHeap0.potential())

    def test24(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.poll()
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertEqual(0, fibonacciHeap0.potential())

    def test23(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.add(fibonacciHeap0)
        fibonacciHeap0.remove0()
        self.assertEqual(0, fibonacciHeap0.size())

    def test22(self) -> None:

        list0 = [
            "",
            "FibonacciHeap=[",
            "FibonacciHeap=[",
            "",
            "",
            "",
            "U`'?k+",
            "org.apache.commons.graph.utils.Assertions",
        ]
        fibonacciHeap0 = FibonacciHeap[object](None)
        fibonacciHeap0.addAll(list0)
        fibonacciHeap0.toString()
        self.assertEqual(8, fibonacciHeap0.size())

    def test21(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        string0 = str(fibonacciHeap0)
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertEqual(0, fibonacciHeap0.potential())
        self.assertEqual("FibonacciHeap=[]", string0)

    def test20(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        fibonacciHeapNodeArray0 = [FibonacciHeapNode[object]()] * 0

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.toArray1(fibonacciHeapNodeArray0)
            self.fail("Expecting exception: NotImplementedError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", NotImplementedError
        )

    def test19(self) -> None:

        fibonacciHeap0 = FibonacciHeap[FibonacciHeap[str]](None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.iterator()
            self.fail("Expecting exception: NotImplementedError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", NotImplementedError
        )

    def test18(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.toArray0()
            self.fail("Expecting exception: NotImplementedError")

        self.verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", NotImplementedError
        )

    def test17(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap0.remove1(None)

    def test16(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        boolean0 = fibonacciHeap0.contains(fibonacciHeap0)
        self.assertEqual(0, fibonacciHeap0.size())
        self.assertFalse(boolean0)
        self.assertEqual(0, fibonacciHeap0.potential())

    def test14(self) -> None:

        fibonacciHeap0 = FibonacciHeap[int]()
        linkedList0 = LinkedList[int]()
        integer0 = Integer(0)
        linkedList0.add(integer0)
        fibonacciHeap0.addAll(linkedList0)
        fibonacciHeap0.isEmpty()
        self.assertEqual(1, fibonacciHeap0.size())

    def test13(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.add(fibonacciHeap0)
        fibonacciHeap0.peek()
        self.assertEqual(1, fibonacciHeap0.size())

    def test12(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        list0 = [", ", "", "", "V<^gw/;,dyMJyC", "", "", "`1u/", "V<^gw/;,dyMJyC"]
        fibonacciHeap0.addAll(list0)
        fibonacciHeap0.remove()
        fibonacciHeap0.poll()
        self.assertFalse(fibonacciHeap0.isEmpty())

    def test11(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.add(fibonacciHeap0)
        fibonacciHeap0.poll()
        self.assertEqual(0, fibonacciHeap0.size())

    def test10(self) -> None:

        fibonacciHeap0 = FibonacciHeap[str](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.remove0()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", RuntimeError
        )

    def test09(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)
        stream0 = fibonacciHeap0.parallelStream()
        fibonacciHeap0.add(fibonacciHeap0)

        with self.assertRaises(TypeError):
            fibonacciHeap0.add(stream0)

        verifyException("org.apache.commons.graph.collections.FibonacciHeap", TypeError)

    def test08(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.add(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test07(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.add(fibonacciHeap0)
        list0 = ['{H#U6C}>dyurkgZEL&"']

        with pytest.raises(TypeError):
            fibonacciHeap0.addAll(list0)

    def test06(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object]((Comparator[object])(None))
        linkedList0 = LinkedList[object]()
        linkedList0.add((object)(None))

        try:
            fibonacciHeap0.addAll(linkedList0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test05(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.addAll(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.collections.FibonacciHeap", RuntimeError
        )

    def test04(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap1 = FibonacciHeap(None)

        with pytest.raises(NotImplementedError):
            fibonacciHeap1.containsAll(fibonacciHeap0)

    def test03(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        fibonacciHeap0.add(fibonacciHeap0)

        with pytest.raises(TypeError):
            fibonacciHeap0.offer(
                "FibonacciHeap=[org.apache.commons.graph.collections.FibonacciHeap@0000000001, ]"
            )

    def test02(self) -> None:

        fibonacciHeap0 = FibonacciHeap[object](None)

        with pytest.raises(RuntimeError):
            fibonacciHeap0.offer(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test01(self) -> None:

        fibonacciHeap0 = FibonacciHeap(None)
        list0 = [
            "",
            "",
            "org.apache.commons.graph.utils.Assertions",
            "",
            "",
            "",
            "",
            "",
        ]
        fibonacciHeap0.addAll(list0)
        fibonacciHeap0.poll()
        int0 = fibonacciHeap0.potential()
        self.assertEqual(7, fibonacciHeap0.size())
        self.assertEqual(8, int0)

    def test00(self) -> None:

        # Create a FibonacciHeap instance using the static method FibonacciHeap1
        fibonacciHeap0 = FibonacciHeap.FibonacciHeap1()

        # Create a mock comparator
        comparator0 = unittest.mock.Mock(spec=Comparator)

        # Create a FibonacciHeap instance with the mock comparator
        fibonacciHeap1 = FibonacciHeap(comparator0)

        # Offer fibonacciHeap0 to fibonacciHeap1
        fibonacciHeap1.offer(fibonacciHeap0)

        # Get the size of fibonacciHeap1
        int0 = fibonacciHeap1.size()

        # Assert that the size is 1
        self.assertEqual(1, int0)
