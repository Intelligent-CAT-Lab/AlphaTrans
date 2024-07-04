from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.BaseProxyHandler import *

# from src.test.org.apache.commons.pool2.proxy.BaseProxyHandler_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class BaseProxyHandler_ESTest(unittest.TestCase):

    def test9(self) -> None:

        baseProxyHandler0 = BaseProxyHandler[object](None, None)
        string0 = baseProxyHandler0.__str__()
        self.assertEqual(
            "org.apache.commons.pool2.proxy.BaseProxyHandler [pooledObject=null, usageTracking=null]",
            string0,
        )

    def test8(self) -> None:

        baseProxyHandler0 = BaseProxyHandler[object](None, None)
        object0 = baseProxyHandler0.getPooledObject()
        self.assertIsNone(object0)

    def test7(self) -> None:

        baseProxyHandler0 = BaseProxyHandler[object](None, None)
        object0 = baseProxyHandler0.disableProxy()
        self.assertIsNone(object0)

    def test6(self) -> None:

        object0 = object()
        baseProxyHandler0 = BaseProxyHandler(object0, None)

        try:
            baseProxyHandler0.doInvoke(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)

    def test5(self) -> None:

        usageTracking0 = mock(UsageTracking, ViolatedAssumptionAnswer())
        doReturn(None).when(usageTracking0).toString()
        baseProxyHandler0 = BaseProxyHandler(usageTracking0, usageTracking0)
        try:
            baseProxyHandler0.doInvoke(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)

    def test4(self) -> None:

        baseProxyHandler0 = BaseProxyHandler(None, None)

        try:
            baseProxyHandler0.doInvoke(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # This object may no longer be used as it has been returned to the Object Pool.
            self.verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)

    def test3(self) -> None:

        baseProxyHandler0 = BaseProxyHandler[object](None, None)

        try:
            baseProxyHandler0.validateProxiedObject()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e)

    def test2(self) -> None:

        # Create an instance of Object
        object0 = object()

        # Create a mock of UsageTracking
        usageTracking0 = mock(UsageTracking, ViolatedAssumptionAnswer)

        # Create an instance of BaseProxyHandler
        baseProxyHandler0 = BaseProxyHandler(object0, usageTracking0)

        # Call the disableProxy method
        object1 = baseProxyHandler0.disableProxy()

        # Assert that object0 and object1 are the same
        self.assertIs(object0, object1)

    def test1(self) -> None:

        integer0 = Integer(0)
        baseProxyHandler0 = BaseProxyHandler(integer0, None)
        usageTracking0 = mock(UsageTracking)
        baseProxyHandler1 = BaseProxyHandler(baseProxyHandler0, usageTracking0)
        object0 = baseProxyHandler1.getPooledObject()
        self.assertIsNotNone(object0)

    def test0(self) -> None:

        integer0 = Integer(0)
        usageTracking0 = mock(UsageTracking, ViolatedAssumptionAnswer())
        baseProxyHandler0 = BaseProxyHandler(integer0, usageTracking0)
        baseProxyHandler0.validateProxiedObject()
