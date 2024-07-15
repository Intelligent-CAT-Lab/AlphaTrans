from __future__ import annotations
import time
import copy
import re
import mock
import tempfile
import os
import typing
from typing import *
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.IOUtils import *

# from src.test.org.apache.commons.csv.IOUtils_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class IOUtils_ESTest(unittest.TestCase):

    def test18(self) -> None:

        mockThrowable0 = MockThrowable()
        try:
            IOUtils.rethrow(mockThrowable0)
            self.fail("Expecting exception: Throwable")

        except Exception as e:
            pass

    def test17(self) -> None:

        reader0 = io.StringIO("")
        writer0 = io.StringIO()
        mockPrintWriter0 = io.TextIOWrapper(writer0)
        long0 = IOUtils.copyLarge0(reader0, mockPrintWriter0)
        self.assertEqual(0, long0)

    def test16(self) -> None:

        reader0 = io.StringIO("")
        writer0 = io.StringIO()
        mockPrintWriter0 = writer0
        long0 = IOUtils.copy0(reader0, mockPrintWriter0)
        self.assertEqual(0, long0)

    def test15(self) -> None:

        reader0 = io.StringIO("")
        writer0 = io.StringIO()
        charBuffer0 = [""] * IOUtils.DEFAULT_BUFFER_SIZE
        IOUtils.copy1(reader0, writer0, charBuffer0)

    def test14(self) -> None:

        byteArrayOutputStream0 = io.BytesIO()
        mockPrintWriter0 = io.TextIOWrapper(byteArrayOutputStream0)
        charArray0 = [""] * 4
        stringReader0 = io.StringIO("D*<> ZJ`^fqfzve")
        long0 = IOUtils.copyLarge1(stringReader0, mockPrintWriter0, charArray0)
        self.assertEqual(15, long0)

    def test13(self) -> None:

        piped_reader0 = io.PipedReader()
        try:
            IOUtils.copy0(piped_reader0, None)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test12(self) -> None:

        stringReader0 = io.StringIO('EHX4ktF3 o"y<I36#')
        try:
            IOUtils.copy0(stringReader0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test11(self) -> None:

        pipedReader0 = io.PipedReader(1)
        mockFileOutputStream0 = io.StringIO()
        mockPrintStream0 = mockFileOutputStream0
        charBuffer0 = ["\0"] * 1
        try:
            IOUtils.copy1(pipedReader0, mockPrintStream0, charBuffer0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.assertEqual(str(e), "java.io.PipedReader")

    def test10(self) -> None:

        reader0 = io.StringIO("")
        try:
            IOUtils.copy1(reader0, [], [])
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test09(self) -> None:

        pipedReader0 = io.PipedReader()
        stringWriter0 = io.StringIO()
        try:
            IOUtils.copyLarge0(pipedReader0, stringWriter0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test08(self) -> None:

        writer0 = io.StringIO()
        try:
            IOUtils.copyLarge0(None, writer0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, TypeError)
            self.assertEqual(str(e), "argument 1 must be str, not NoneType")

    def test07(self) -> None:

        pipedReader0 = io.PipedReader()
        pipedWriter0 = io.PipedWriter()
        charArray0 = [" "]
        try:
            IOUtils.copyLarge1(pipedReader0, pipedWriter0, charArray0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedReader", e)

    def test06(self) -> None:

        reader0 = io.StringIO()
        writer0 = io.StringIO()

        try:
            IOUtils.copyLarge1(reader0, writer0, None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test05(self) -> None:

        reader0 = io.StringIO("")
        byteArrayOutputStream0 = io.BytesIO()
        mockPrintWriter0 = io.TextIOWrapper(byteArrayOutputStream0, line_buffering=True)
        charArray0 = []
        IOUtils.copyLarge1(reader0, mockPrintWriter0, charArray0)

    def test04(self) -> None:

        with pytest.raises(RuntimeError):
            IOUtils.rethrow(None)

    def test03(self) -> None:

        stringReader0 = io.StringIO('EHX4ktF3 o"yI36')
        file0 = tempfile.NamedTemporaryFile()
        mockPrintStream0 = file0
        long0 = IOUtils.copy0(stringReader0, mockPrintStream0)
        self.assertEqual(19, file0.tell())
        self.assertEqual(19, long0)

    def test02(self) -> None:

        reader0 = io.StringIO("")
        charArray0 = ["\0"] * 3
        charBuffer0 = charArray0[1:2]
        long0 = IOUtils.copy1(reader0, charBuffer0, charBuffer0)
        self.assertEqual(0, long0)

    def test01(self) -> None:

        dataOutputStream0 = io.BytesIO()
        mockPrintWriter0 = io.TextIOWrapper(dataOutputStream0, line_buffering=True)
        stringReader0 = io.StringIO("&s[(A7A")
        long0 = IOUtils.copyLarge0(stringReader0, mockPrintWriter0)
        self.assertEqual(7, long0)

    def test00(self) -> None:

        reader0 = io.StringIO()
        writer0 = io.StringIO()
        charArray0 = [" "] * 9
        long0 = IOUtils.copyLarge1(reader0, writer0, charArray0)
        self.assertEqual(0, long0)
