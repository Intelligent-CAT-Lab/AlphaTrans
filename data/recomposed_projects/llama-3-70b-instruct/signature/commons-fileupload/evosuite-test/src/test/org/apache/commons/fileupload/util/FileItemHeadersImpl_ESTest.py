from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *

# from src.test.org.apache.commons.fileupload.util.FileItemHeadersImpl_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FileItemHeadersImpl_ESTest(unittest.TestCase):

    def test9(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        iterator0 = fileItemHeadersImpl0.getHeaderNames()
        assert iterator0 is not None

    def test8(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("ytU(", "ytU(")
        string0 = fileItemHeadersImpl0.getHeader("ytU(")
        self.assertIsNotNone(string0)
        self.assertEqual("ytU(", string0)

    def test7(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        string0 = fileItemHeadersImpl0.getHeader("cLk0cv4BCDd4'V1g>")
        self.assertIsNone(string0)

    def test6(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("", "cLk0cv4BCDd4'V1g>")
        iterator0 = fileItemHeadersImpl0.getHeaders("")
        assert iterator0 is not None

    def test5(self) -> None:
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        iterator0 = fileItemHeadersImpl0.getHeaders("cLk0cv4BCDd4'V1g>")
        assert iterator0 is not None

    def test4(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("", "")
        fileItemHeadersImpl0.addHeader("", "")

    def test3(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        try:
            fileItemHeadersImpl0.addHeader(None, None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test2(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        try:
            fileItemHeadersImpl0.getHeader(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.fileupload.util.FileItemHeadersImpl", e
            )

    def test1(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()

        with pytest.raises(RuntimeError):
            fileItemHeadersImpl0.getHeaders(None)

    def test0(self) -> None:

        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("", "")
        string0 = fileItemHeadersImpl0.getHeader("")
        self.assertEqual("", string0)
