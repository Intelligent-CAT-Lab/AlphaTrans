from __future__ import annotations
import time
import re
import mock
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.FileUploadException import *

# from src.test.org.apache.commons.fileupload.FileUploadException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FileUploadException_ESTest(unittest.TestCase):

    def test8(self) -> None:
        fileUploadException0 = FileUploadException.FileUploadException0()
        throwable0 = fileUploadException0.getCause()
        self.assertIsNone(throwable0)

    def test7(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException1("Caused by:")
        assert fileUploadException0 is not None

    def test6(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()
        mockPrintStream0 = io.StringIO()
        fileUploadException0.printStackTrace0(mockPrintStream0)

    def test5(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()
        fileUploadException1 = FileUploadException("Caused by:", fileUploadException0)
        mockFile0 = io.StringIO()
        fileUploadException1.printStackTrace0(mockFile0)
        # Unstable assertion: self.assertEqual(438, len(mockFile0.getvalue()))

    def test4(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()
        mockFile0 = MockFile('~g$9"Ph>8(OL')
        mockPrintStream0 = MockPrintStream(mockFile0)
        mockPrintWriter0 = MockPrintWriter(mockPrintStream0)
        fileUploadException0.printStackTrace1(mockPrintWriter0)

    def test3(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()
        file0 = io.StringIO("Caused by:")
        mockPrintWriter0 = file0
        fileUploadException1 = FileUploadException("i[O", fileUploadException0)
        fileUploadException1.printStackTrace1(mockPrintWriter0)
        self.assertFalse(fileUploadException1 == fileUploadException0)

    def test2(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()

        try:
            fileUploadException0.printStackTrace0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsNotNone(str(e))

    def test1(self) -> None:

        fileUploadException0 = FileUploadException.FileUploadException0()
        # Undeclared exception
        try:
            fileUploadException0.printStackTrace1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.evosuite.runtime.mock.java.lang.MockThrowable", e)

    def test0(self) -> None:
        fileUploadException0 = FileUploadException.FileUploadException0()
        fileUploadException1 = FileUploadException("Caused by:", fileUploadException0)
        throwable0 = fileUploadException1.getCause()
        self.assertIsNot(fileUploadException1, throwable0)
