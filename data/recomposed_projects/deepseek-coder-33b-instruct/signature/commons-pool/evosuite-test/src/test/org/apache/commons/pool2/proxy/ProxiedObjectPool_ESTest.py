from __future__ import annotations
import time
import re
import mock
import sys
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.proxy.JdkProxySource import *
from src.main.org.apache.commons.pool2.proxy.ProxiedObjectPool import *

# from src.test.org.apache.commons.pool2.proxy.ProxiedObjectPool_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class ProxiedObjectPool_ESTest(unittest.TestCase):

    def test22(self) -> None:

        pass  # LLM could not translate this method

    def test21(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool(None, None)
        try:
            proxiedObjectPool0.getNumIdle()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test20(self) -> None:

        pass  # LLM could not translate this method

    def test19(self) -> None:

        # Create a mock object for ObjectPool
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())

        # Get the system class loader
        classLoader0 = ClassLoader.getSystemClassLoader()

        # Create an empty array of classes
        classArray0 = Array.newInstance(Class, 0)

        # Create a JdkProxySource
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)

        # Create a ProxiedObjectPool
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)

        # Call the clear method on the ProxiedObjectPool
        proxiedObjectPool0.clear()

    def test18(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool[int](None, None)

        try:
            proxiedObjectPool0.close()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test17(self) -> None:

        pass  # LLM could not translate this method

    def test16(self) -> None:

        classLoader0 = JdkProxySource.getPlatformClassLoader()
        classArray0 = [object] * 1
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())
        objectPool0.getNumActive = Mock(return_value=0)
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)
        int0 = proxiedObjectPool0.getNumActive()
        self.assertEqual(0, int0)

    def test15(self) -> None:

        classLoader0 = JdkProxySource.__classLoader
        classArray0 = [None] * 0
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)
        proxiedObjectPool0.addObject()

    def test14(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool(None, None)
        try:
            proxiedObjectPool0.addObject()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test13(self) -> None:

        objectPool0 = mock(ObjectPool, new=ViolatedAssumptionAnswer())
        objectPool0.borrowObject.return_value = None
        classLoader0 = ClassLoader.getPlatformClassLoader()
        classArray0 = Array.newInstance(Class, 1)
        class0 = Object
        classArray0[0] = class0
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)
        try:
            proxiedObjectPool0.borrowObject()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # java.lang.Object is not an interface
            #
            verifyException("java.lang.reflect.Proxy$ProxyBuilder", e)

    def test12(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool(None, None)
        try:
            proxiedObjectPool0.borrowObject()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test11(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool(None, None)
        try:
            proxiedObjectPool0.clear()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test10(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool(None, None)
        try:
            proxiedObjectPool0.getNumActive()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test09(self) -> None:

        classLoader0 = JdkProxySource.__classLoader
        classArray0 = [None] * 0
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)
        proxiedObjectPool0 = ProxiedObjectPool(None, jdkProxySource0)

        try:
            proxiedObjectPool0.invalidateObject0(jdkProxySource0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # not a proxy instance
            self.verifyException("java.lang.reflect.Proxy", e)

    def test08(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool[object](None, None)
        try:
            proxiedObjectPool0.invalidateObject0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test07(self) -> None:

        classLoader0 = JdkProxySource.__classLoader
        classArray0 = [None] * 0
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)
        proxiedObjectPool0 = ProxiedObjectPool(None, jdkProxySource0)
        object0 = object()
        try:
            proxiedObjectPool0.returnObject(object0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # not a proxy instance
            self.verifyException("java.lang.reflect.Proxy", e)

    def test06(self) -> None:

        proxiedObjectPool0 = ProxiedObjectPool[object](None, None)
        try:
            proxiedObjectPool0.returnObject(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e)

    def test05(self) -> None:

        # Create a mock object of ObjectPool
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())

        # Set the return value of getNumActive method
        when(objectPool0).getNumActive().thenReturn(-3983)

        # Create a ProxiedObjectPool object
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, None)

        # Call the getNumActive method
        int0 = proxiedObjectPool0.getNumActive()

        # Assert the result
        self.assertEqual(-3983, int0)

    def test04(self) -> None:

        # Mock ObjectPool
        objectPool0 = unittest.mock.Mock(spec=ObjectPool)
        objectPool0.getNumActive.return_value = 83

        # Create JdkProxySource
        classLoader0 = ClassLoader.getSystemClassLoader()
        classArray0 = [None] * 0
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)

        # Create ProxiedObjectPool
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)

        # Call getNumActive
        int0 = proxiedObjectPool0.getNumActive()

        # Assert the result
        self.assertEqual(83, int0)

    def test03(self) -> None:

        pass  # LLM could not translate this method

    def test02(self) -> None:

        # Create a mock object of ObjectPool
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())

        # Set the return value of getNumIdle method
        when(objectPool0).getNumIdle().thenReturn(2266)

        # Create a ProxiedObjectPool object
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, None)

        # Call the getNumIdle method
        int0 = proxiedObjectPool0.getNumIdle()

        # Assert the result
        self.assertEqual(2266, int0)

    def test01(self) -> None:

        # Create a mock object of ObjectPool
        objectPool0 = mock(ObjectPool, ViolatedAssumptionAnswer())

        # Set the return value of getNumIdle method to 0
        doReturn(0).when(objectPool0).getNumIdle()

        # Create a ProxiedObjectPool object
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, None)

        # Call the getNumIdle method
        int0 = proxiedObjectPool0.getNumIdle()

        # Assert that the return value is 0
        self.assertEqual(0, int0)

    def test00(self) -> None:

        # Mocking ObjectPool
        objectPool0 = mock(ObjectPool, new_callable=ViolatedAssumptionAnswer)

        # Getting System ClassLoader
        classLoader0 = ClassLoader.getSystemClassLoader()

        # Creating an array of Classes
        classArray0 = Array.newInstance(Class, 1)

        # Creating JdkProxySource
        jdkProxySource0 = JdkProxySource(classLoader0, classArray0)

        # Creating ProxiedObjectPool
        proxiedObjectPool0 = ProxiedObjectPool(objectPool0, jdkProxySource0)

        # Closing ProxiedObjectPool
        proxiedObjectPool0.close()
