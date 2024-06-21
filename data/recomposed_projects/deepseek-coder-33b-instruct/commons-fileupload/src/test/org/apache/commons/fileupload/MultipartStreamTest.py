from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.fileupload.MultipartStream import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class MultipartStreamTest(unittest.TestCase):

    __BOUNDARY_TEXT: str = "myboundary"

    @pytest.mark.test
    def testTwoParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        ms = MultipartStream.MultipartStream2(
            input, boundary, ProgressNotifier(None, len(contents))
        )
        assert ms is not None

    @pytest.mark.test
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

    @pytest.mark.test
    def testThreeParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = len(boundary) + len(MultipartStream._BOUNDARY_PREFIX) + 1
        ms = MultipartStream(
            input, boundary, iBufSize, ProgressNotifier(None, len(contents))
        )
        assert ms is not None
