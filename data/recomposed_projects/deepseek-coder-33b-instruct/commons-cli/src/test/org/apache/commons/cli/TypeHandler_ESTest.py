from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.cli.TypeHandler import *

# from src.main.org.apache.commons.cli.TypeHandler_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.testdata.EvoSuiteFile import *
# from src.main.org.evosuite.runtime.testdata.FileSystemHandling import *


class TypeHandler_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test27(self) -> None:
        class0 = TypeHandler.createClass("org.apache.commons.cli.Option$1")
        self.assertEqual(str(class0), "<class 'org.apache.commons.cli.Option$1'>")

    @pytest.mark.test
    def test26(self) -> None:
        with pytest.raises(NullPointerException):
            TypeHandler.openFile(None)

    @pytest.mark.test
    def test25(self) -> None:

        # Undeclared exception
        try:
            TypeHandler.createFiles("org.apache.commons.cli.PatternOptionBuilder")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            # Not yet implemented
            verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test24(self) -> None:

        try:
            TypeHandler.createValue1(None, None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unable to handle the class: null
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test23(self) -> None:
        typeHandler0 = TypeHandler()

    @pytest.mark.test
    def test22(self) -> None:
        try:
            TypeHandler.createURL("Unable to parse the URL: ")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            #
            # Unable to parse the URL: Unable to parse the URL:
            #
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test21(self) -> None:

        # Undeclared exception
        try:
            TypeHandler.createDate("xKBaRqX+")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            # Not yet implemented
            verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test20(self) -> None:

        class0 = object
        object0 = TypeHandler.createValue0("org.apache.commons.cli.Options", class0)
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test19(self) -> None:
        number0 = TypeHandler.createNumber("9")
        self.assertEqual(9, number0)

    @pytest.mark.test
    def test18(self) -> None:
        try:
            TypeHandler.createNumber("org.apache.commons.cli.PatternOptionBulder")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # For input string: "org.apache.commons.cli.PatternOptionBulder"
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test17(self) -> None:

        object0 = TypeHandler.createObject(
            "org.apache.commons.cli.PatternOptionBuilder"
        )
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test16(self) -> None:

        class0 = int
        try:
            TypeHandler.createValue0("h/!/%Y2", class0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unable to handle the class: class java.lang.Integer
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test15(self) -> None:
        try:
            TypeHandler.createClass(None)
            self.fail("Expecting exception: NullPointerException")
        except TypeError:
            pass

    @pytest.mark.test
    def test14(self) -> None:
        try:
            TypeHandler.createClass("xKBaRqX+")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            # Unable to find the class: xKBaRqX+
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test13(self) -> None:

        try:
            TypeHandler.createFile(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertIsInstance(e, TypeError)
            self.assertEqual(str(e), "argument of type 'NoneType' is not iterable")

    @pytest.mark.test
    def test12(self) -> None:
        try:
            TypeHandler.createNumber(None)
            self.fail("Expecting exception: NullPointerException")
        except TypeError as e:
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test11(self) -> None:

        try:
            TypeHandler.createObject(None)
            self.fail("Expecting exception: NullPointerException")
        except NullPointerException:
            pass

    @pytest.mark.test
    def test10(self) -> None:

        try:
            TypeHandler.createObject("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Unable to find the class:
            #
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test09(self) -> None:

        class0 = object

        try:
            TypeHandler.createValue0(None, class0)
            self.fail("Expecting exception: NullPointerException")

        except TypeError as e:
            pass

    @pytest.mark.test
    def test08(self) -> None:

        try:
            TypeHandler.createValue1("", "")
            self.fail("Expecting exception: ClassCastException")

        except ClassCastException as e:
            verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test07(self) -> None:
        try:
            TypeHandler.openFile("; Unable to create an instance of: ")
            self.fail("Expecting exception: Exception")
        except Exception as e:
            #
            # Unable to find file: ; Unable to create an instance of:
            #
            self.verifyException("org.apache.commons.cli.TypeHandler", e)

    @pytest.mark.test
    def test06(self) -> None:
        class0 = TypeHandler.createClass("org.apache.commons.cli.PatternOptionBuilder")
        self.assertFalse(class0.isSynthetic())

    @pytest.mark.test
    def test05(self) -> None:

        # Create an EvoSuiteFile object
        evoSuiteFile0 = EvoSuiteFile("/!/%Y2")

        # Append a string to the file
        FileSystemHandling.appendStringToFile(evoSuiteFile0, " ")

        # Create a file
        file0 = TypeHandler.createFile("/!/%Y2")

        # Assert that the file name is as expected
        self.assertEqual("!/%Y2", file0.name)

    @pytest.mark.test
    def test04(self) -> None:

        file0 = TypeHandler.createFile("")
        self.assertFalse(file0.is_file())

    @pytest.mark.test
    def test03(self) -> None:

        file0 = TypeHandler.createFile(".>scalamj}4c,")
        self.assertEqual(0, file0.stat().st_blocks * 512)

    @pytest.mark.test
    def test02(self) -> None:

        class0 = object
        object0 = TypeHandler.createValue1("org.apache.commons.cli.Options", class0)
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test01(self) -> None:

        # Create an instance of EvoSuiteFile
        evoSuiteFile0 = EvoSuiteFile("; Unable to create an instance of: ")

        # Create a byte array
        byteArray0 = bytearray(7)

        # Call the static method appendDataToFile from FileSystemHandling
        FileSystemHandling.appendDataToFile(evoSuiteFile0, byteArray0)

        # Call the static method openFile from TypeHandler
        fileInputStream0 = TypeHandler.openFile("; Unable to create an instance of: ")

        # Check if the file size is 7
        self.assertEqual(7, fileInputStream0.read().__sizeof__())

    @pytest.mark.test
    def test00(self) -> None:

        try:
            TypeHandler.createObject("org.apache.commons.cli.ParseException")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # java.lang.InstantiationException; Unable to create an instance of: org.apache.commons.cli.ParseException
            self.verifyException("org.apache.commons.cli.TypeHandler", e)
