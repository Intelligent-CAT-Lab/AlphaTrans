from __future__ import annotations
import time
import inspect
import re
import os
import numbers
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.cli.TypeHandler import *

# from src.test.org.apache.commons.cli.TypeHandler_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.testdata.EvoSuiteFile import *
# from src.main.org.evosuite.runtime.testdata.FileSystemHandling import *


class TypeHandler_ESTest(unittest.TestCase):

    def test25(self) -> None:
        class0 = TypeHandler.createClass("[S")
        self.assertFalse(inspect.isinterface(class0))

    def test24(self) -> None:
        try:
            TypeHandler.openFile("")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Unable to find file:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test23(self) -> None:

        # Undeclared exception handling in Python is done using try/except blocks
        try:
            TypeHandler.createFiles("org.apache.commons.cli.PatternOptionBuilder")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            # Not yet implemented
            verifyException("org.apache.commons.cli.TypeHandler", e)

    def test22(self) -> None:

        try:
            TypeHandler.createValue1(None, None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unable to handle the class: null
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test21(self) -> None:

        object0 = TypeHandler.createObject("org.apache.commons.cli.TypeHandler")
        self.assertIsNotNone(object0)

    def test20(self) -> None:
        try:
            TypeHandler.createURL("]qlF%Fe^,Qb;")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Unable to parse the URL: ]qlF%Fe^,Qb;
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test19(self) -> None:

        # Undeclared exception in Java code
        try:
            TypeHandler.createDate("}*o")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            # Not yet implemented
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test18(self) -> None:
        number0 = TypeHandler.createNumber("5")
        self.assertEqual(5, number0)

    def test17(self) -> None:
        try:
            TypeHandler.createNumber("org.apache.commons.cli.Options")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test16(self) -> None:

        class0 = Object
        object0 = TypeHandler.createValue0("org.apache.commons.cli.TypeHandler", class0)
        self.assertIsNotNone(object0)

    def test15(self) -> None:
        typeHandler0 = TypeHandler()

    def test14(self) -> None:

        class0 = int
        try:
            TypeHandler.createValue0("; Unable to create an instance of: ", class0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Unable to handle the class: class java.lang.Integer
            #
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test13(self) -> None:
        with pytest.raises(RuntimeError):
            TypeHandler.createClass(None)

    def test12(self) -> None:
        try:
            TypeHandler.createClass("gNx")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Unable to find the class: gNx
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test11(self) -> None:

        with self.assertRaises(RuntimeError):
            TypeHandler.createFile(None)

        try:
            TypeHandler.createFile(None)
        except RuntimeError as e:
            self.verifyException("java.io.File", e)

    def test10(self) -> None:
        try:
            TypeHandler.createNumber(None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test09(self) -> None:

        try:
            TypeHandler.createObject(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test08(self) -> None:

        try:
            TypeHandler.createObject("@;~YkT#_pRf")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    def test07(self) -> None:

        class0 = Object

        try:
            TypeHandler.createValue0(None, class0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test06(self) -> None:

        try:
            TypeHandler.createValue1(",y&2", ",y&2")
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            verifyException("org.apache.commons.cli.TypeHandler", e)

    def test05(self) -> None:
        with pytest.raises(TypeError) as e:
            TypeHandler.openFile(None)
        assert str(e.value) == "Expecting exception: RuntimeError"

    def test04(self) -> None:
        class0 = TypeHandler.createClass("org.apache.commons.cli.PatternOptionBuilder")
        self.assertFalse(not class0)

    def test03(self) -> None:

        file0 = TypeHandler.createFile("")
        self.assertTrue(file0.exists())

    def test02(self) -> None:
        file0 = TypeHandler.createFile("/p.")
        self.assertTrue(file0.is_absolute())

    def test01(self) -> None:

        evoSuiteFile0 = EvoSuiteFile(".KsSb`k_VX_1N1jSin")
        byteArray0 = bytearray(3)
        FileSystemHandling.appendDataToFile(evoSuiteFile0, byteArray0)
        file0 = TypeHandler.createFile(".KsSb`k_VX_1N1jSin")
        self.assertEqual(0, file0.stat().st_size)

    def test00(self) -> None:

        try:
            TypeHandler.createObject("org.apache.commons.cli.Option")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)
