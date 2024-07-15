from __future__ import annotations
import re
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.MultipartStream import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class MultipartStreamTest(unittest.TestCase):

    __BOUNDARY_TEXT: str = "myboundary"

    def testTwoParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        ms = MultipartStream.MultipartStream2(
            input, boundary, ProgressNotifier(None, len(contents))
        )
        assert ms is not None

    def testSmallBuffer(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = 1

        with pytest.raises(ValueError):
            MultipartStream(
                input, boundary, iBufSize, ProgressNotifier(None, len(contents))
            )

    def testThreeParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = len(boundary) + len(MultipartStream._BOUNDARY_PREFIX) + 1
        pNotifier = ProgressNotifier(None, len(contents))
        ms = MultipartStream(input, boundary, iBufSize, pNotifier)
        self.assertIsNotNone(ms)
