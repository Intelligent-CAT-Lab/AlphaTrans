from __future__ import annotations
import time
import re
import mock
import os
import datetime
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfo import *

# from src.test.org.apache.commons.pool2.impl.DefaultPooledObjectInfo_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultPooledObjectInfo_ESTest(unittest.TestCase):

    def test28(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getLastBorrowTimeFormatted()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test27(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)
        string0 = defaultPooledObjectInfo0.toString()
        self.assertEqual("DefaultPooledObjectInfo [pooledObject=None]", string0)

    def test26(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getLastReturnTime()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test25(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getPooledObjectToString()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'AttributeError'>")
            self.assertEqual(str(e), "'NoneType' object has no attribute 'getObject'")

    def test24(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getBorrowedCount()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test23(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getCreateTime()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test22(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        pooledObject0.getLastBorrowInstant.return_value = datetime.datetime(
            2014, 2, 14, 20, 21, 21
        )

        # Creating DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Calling the method to be tested
        string0 = defaultPooledObjectInfo0.getLastBorrowTimeFormatted()

        # Asserting the result
        self.assertEqual("2014-02-14 20:21:21 +0000", string0)

    def test21(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getLastReturnTimeFormatted()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test20(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)
        try:
            defaultPooledObjectInfo0.getLastBorrowTrace()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e)

    def test19(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getCreateTimeFormatted()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test18(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getPooledObjectType()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test17(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        pooledObject0.getLastBorrowInstant.return_value = MockInstant.now()

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)
        long0 = defaultPooledObjectInfo0.getLastBorrowTime()

        self.assertEqual(1392409281320, long0)

    def test16(self) -> None:

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(None)

        try:
            defaultPooledObjectInfo0.getLastBorrowTime()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e
            )

    def test15(self) -> None:

        # Create a mock object of PooledObject
        pooledObject0 = unittest.mock.Mock(spec=PooledObject)

        # Set the return value of getBorrowedCount method to -1
        pooledObject0.getBorrowedCount.return_value = -1

        # Create an instance of DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Call the getBorrowedCount method
        long0 = defaultPooledObjectInfo0.getBorrowedCount()

        # Assert that the return value is -1
        self.assertEqual(-1, long0)

    def test14(self) -> None:

        # Create a mock object of PooledObject
        pooledObject0 = unittest.mock.Mock(spec=PooledObject)

        # Set the return value of getBorrowedCount method
        pooledObject0.getBorrowedCount.return_value = 2922

        # Create an instance of DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Call the getBorrowedCount method
        long0 = defaultPooledObjectInfo0.getBorrowedCount()

        # Assert that the return value is as expected
        self.assertEqual(2922, long0)

    def test13(self) -> None:

        # Create a mock object of PooledObject
        pooledObject0 = unittest.mock.Mock(spec=PooledObject)

        # Set the return value of getBorrowedCount method to 0
        pooledObject0.getBorrowedCount.return_value = 0

        # Create an instance of DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Call the getBorrowedCount method
        long0 = defaultPooledObjectInfo0.getBorrowedCount()

        # Assert that the return value is 0
        self.assertEqual(0, long0)

    def test12(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        pooledObject0.getCreateInstant.return_value = MockInstant.ofEpochMilli(-1192)

        # Creating DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Getting the create time
        long0 = defaultPooledObjectInfo0.getCreateTime()

        # Asserting the create time
        self.assertEqual(-1192, long0)

    def test11(self) -> None:

        instant0 = MockInstant.ofEpochSecond(0)
        duration0 = Duration.ofMinutes(-1)
        instant1 = MockInstant.minus(instant0, duration0)

        pooledObject0 = mock(PooledObject, new=ViolatedAssumptionAnswer)
        when(pooledObject0).getCreateInstant().thenReturn(instant1)

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)
        long0 = defaultPooledObjectInfo0.getCreateTime()

        self.assertEqual(60000, long0)

    def test10(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        pooledObject0.getCreateInstant.return_value = Instant.ofEpochSecond(0)

        # Creating DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Getting the create time
        long0 = defaultPooledObjectInfo0.getCreateTime()

        # Asserting the create time
        self.assertEqual(0, long0)

    def test09(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        type(pooledObject0).getCreateInstant = Mock(return_value=1)

        # Creating the DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Getting the formatted create time
        string0 = defaultPooledObjectInfo0.getCreateTimeFormatted()

        # Asserting the result
        self.assertEqual("1970-01-01 00:00:01 +0000", string0)

    def test08(self) -> None:

        pass  # LLM could not translate this method

    def test07(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        instant0 = Mock(spec=Instant)
        instant0.toEpochMilli.return_value = 0
        pooledObject0.getLastBorrowInstant.return_value = instant0

        defaultPooledObjectInfo0 = DefaultPooledObjectObjectInfo(pooledObject0)
        long0 = defaultPooledObjectInfo0.getLastBorrowTime()

        self.assertEqual(0, long0)

    def test06(self) -> None:

        pooledObject0 = unittest.mock.Mock(spec=PooledObject)
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)
        string0 = defaultPooledObjectInfo0.getLastBorrowTrace()
        self.assertEqual("", string0)

    def test05(self) -> None:

        instant0 = MockInstant.ofEpochSecond(0)
        instant1 = MockInstant.plusSeconds(instant0, -802)
        pooledObject0 = Mock(PooledObject)
        pooledObject0.getLastReturnInstant.return_value = instant1
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)
        long0 = defaultPooledObjectInfo0.getLastReturnTime()
        self.assertEqual(-802000, long0)

    def test04(self) -> None:

        # Mocking the instant
        instant0 = MockInstant.ofEpochMilli(730)

        # Mocking the PooledObject
        pooledObject0 = Mock(PooledObject)
        pooledObject0.getLastReturnInstant.return_value = instant0

        # Creating the DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Getting the last return time
        long0 = defaultPooledObjectInfo0.getLastReturnTime()

        # Asserting the result
        self.assertEqual(730, long0)

    def test03(self) -> None:

        # Mocking the PooledObject
        pooledObject0 = Mock(spec=PooledObject)
        instant0 = Mock(spec=Instant)
        instant0.toEpochMilli.return_value = 0
        pooledObject0.getLastReturnInstant.return_value = instant0

        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)
        long0 = defaultPooledObjectInfo0.getLastReturnTime()

        self.assertEqual(0, long0)

    def test02(self) -> None:

        # Mocking the PooledObject and its methods
        pooledObject0 = unittest.mock.Mock(spec=PooledObject)
        pooledObject0.getLastReturnInstant.return_value = datetime.datetime.now()

        # Creating an instance of DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectObjectInfo(pooledObject0)

        # Calling the method to be tested
        string0 = defaultPooledObjectInfo0.getLastReturnTimeFormatted()

        # Asserting the result
        self.assertEqual("2014-02-14 20:21:21 +0000", string0)

    def test01(self) -> None:

        # Create a new object
        object0 = object()

        # Create a mock of PooledObject
        pooledObject0 = mock(PooledObject, ViolatedAssumptionAnswer())

        # Set the return value of getObject() method to object0
        doReturn(object0).when(pooledObject0).getObject()

        # Create a DefaultPooledObjectInfo object
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Call the getPooledObjectToString() method
        string0 = defaultPooledObjectInfo0.getPooledObjectToString()

        # Assert that string0 is not None
        assert string0 is not None

    def test00(self) -> None:

        # Create a mock object of PooledObject
        pooledObject0 = mock(PooledObject)

        # Set the return value of getObject method to a new Object
        doReturn(object()).when(pooledObject0).getObject()

        # Create an instance of DefaultPooledObjectInfo
        defaultPooledObjectInfo0 = DefaultPooledObjectInfo(pooledObject0)

        # Call the getPooledObjectType method
        string0 = defaultPooledObjectInfo0.getPooledObjectType()

        # Assert that the returned string is "java.lang.Object"
        self.assertEqual("java.lang.Object", string0)
