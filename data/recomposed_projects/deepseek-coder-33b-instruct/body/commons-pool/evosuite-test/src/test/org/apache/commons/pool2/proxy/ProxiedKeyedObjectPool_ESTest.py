from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.proxy.JdkProxySource import *
from src.main.org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool import *

# from src.test.org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class ProxiedKeyedObjectPool_ESTest(unittest.TestCase):

    def test30(self) -> None:

        classArray0 = [None] * 0
        jdkProxySource0 = JdkProxySource(None, classArray0)
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(None, jdkProxySource0)
        integer0 = Integer(2)
        try:
            proxiedKeyedObjectPool0.invalidateObject0(integer0, integer0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # not a proxy instance
            self.verifyException("java.lang.reflect.Proxy", e)

    def test29(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)

        # Set the return value for getNumIdle0 method
        when(keyedObjectPool0).getNumIdle0().thenReturn(-1)

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the getNumIdle0 method
        int0 = proxiedKeyedObjectPool0.getNumIdle0()

        # Assert that the return value is -1
        self.assertEqual(-1, int0)

    def test28(self) -> None:

        integer0 = Integer(0)
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer())
        doReturn(1774).when(keyedObjectPool0).getNumIdle1(anyInt())
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        int0 = proxiedKeyedObjectPool0.getNumIdle1(integer0)
        self.assertEqual(1774, int0)

    def test27(self) -> None:

        integer0 = Integer(0)
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer())
        keyedObjectPool0.getNumActive1.return_value = -1200
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        int0 = proxiedKeyedObjectPool0.getNumActive1(integer0)
        self.assertEqual(-1200, int0)

    def test26(self) -> None:

        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        proxiedKeyedObjectPool0.clear0()

    def test25(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)
        string0 = str(proxiedKeyedObjectPool0)
        self.assertEqual(
            "ProxiedKeyedObjectPool [pool=None, proxySource=None]", string0
        )

    def test24(self) -> None:

        integer0 = Integer(0)
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        proxiedKeyedObjectPool0.clear1(integer0)

    def test23(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)

        # Set the return value for getNumActive0 method
        when(keyedObjectPool0).getNumActive0().thenReturn(-1760)

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the getNumActive0 method
        int0 = proxiedKeyedObjectPool0.getNumActive0()

        # Assert the result
        self.assertEqual(-1760, int0)

    def test22(self) -> None:

        integer0 = Integer(0)
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        proxiedKeyedObjectPool0.addObject(integer0)

    def test21(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)

        try:
            proxiedKeyedObjectPool0.close()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test20(self) -> None:

        integer0 = Integer(0)
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer())
        doReturn(None).when(keyedObjectPool0).borrowObject(any_int())
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        try:
            proxiedKeyedObjectPool0.borrowObject(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test19(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)
        try:
            proxiedKeyedObjectPool0.addObject(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test18(self) -> None:

        pass  # LLM could not translate this method

    def test17(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)
        try:
            proxiedKeyedObjectPool0.clear0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test16(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)
        try:
            proxiedKeyedObjectPool0.clear1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test15(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)

        try:
            proxiedKeyedObjectPool0.getNumActive0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test14(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)

        try:
            proxiedKeyedObjectPool0.getNumActive1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test13(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)

        try:
            proxiedKeyedObjectPool0.getNumIdle0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test12(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)

        try:
            proxiedKeyedObjectPool0.getNumIdle1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test11(self) -> None:

        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool[int, int](None, None)
        try:
            proxiedKeyedObjectPool0.returnObject(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e)

    def test10(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = unittest.mock.Mock(spec=KeyedObjectPool)

        # Set the return value for getNumActive0 method
        keyedObjectPool0.getNumActive0.return_value = 739

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the getNumActive0 method
        int0 = proxiedKeyedObjectPool0.getNumActive0()

        # Assert that the return value is as expected
        self.assertEqual(739, int0)

    def test09(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = unittest.mock.Mock(spec=KeyedObjectPool)

        # Set the return value for getNumActive0 method
        keyedObjectPool0.getNumActive0.return_value = 0

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the getNumActive0 method
        int0 = proxiedKeyedObjectPool0.getNumActive0()

        # Assert that the return value is 0
        self.assertEqual(0, int0)

    def test08(self) -> None:

        integer0 = 4151
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer())
        doReturn(4151).when(keyedObjectPool0).getNumActive1(anyInt())
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        int0 = proxiedKeyedObjectPool0.getNumActive1(integer0)
        self.assertEqual(4151, int0)

    def test07(self) -> None:

        pass  # LLM could not translate this method

    def test06(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)

        # Set up the behavior of the mock object
        when(keyedObjectPool0).getNumIdle0().thenReturn(2295)

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the method to be tested
        int0 = proxiedKeyedObjectPool0.getNumIdle0()

        # Assert the result
        self.assertEqual(2295, int0)

    def test05(self) -> None:

        pass  # LLM could not translate this method

    def test04(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)

        # Set up the behavior of the mock object
        when(keyedObjectPool0).getNumIdle1(anyInt()).thenReturn(-1)

        # Create an instance of ProxiedKeyedObjectPool
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Create an instance of Integer
        integer0 = Integer(2163)

        # Call the method to be tested
        int0 = proxiedKeyedObjectPool0.getNumIdle1(integer0)

        # Assert the result
        self.assertEqual(-1, int0)

    def test03(self) -> None:

        pass  # LLM could not translate this method

    def test02(self) -> None:

        # Create a mock object for KeyedObjectPool
        keyedObjectPool0 = mock(KeyedObjectPool, ViolatedAssumptionAnswer)

        # Create a ProxiedKeyedObjectPool object
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)

        # Call the close method on the proxiedKeyedObjectPool0 object
        proxiedKeyedObjectPool0.close()

    def test01(self) -> None:

        keyedObjectPool0 = unittest.mock.Mock(spec=KeyedObjectPool)
        proxiedKeyedObjectPool0 = ProxiedKeyedObjectPool(keyedObjectPool0, None)
        integer0 = -1
        integer1 = -295
        try:
            proxiedKeyedObjectPool0.invalidateObject0(integer0, integer1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e
            )

    def test00(self) -> None:

        pass  # LLM could not translate this method
