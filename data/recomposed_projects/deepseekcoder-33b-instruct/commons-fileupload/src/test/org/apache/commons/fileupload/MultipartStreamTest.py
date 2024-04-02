# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.MultipartStream import *
import unittest
from io import BytesIO

# Imports End


class MultipartStreamTest(unittest.TestCase):

    # Class Fields Begin
    __BOUNDARY_TEXT: str = "myboundary"
    # Class Fields End

    # Class Methods Begin
    def testTwoParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        ms = MultipartStream.MultipartStream2(input, boundary, lambda x: None)
        self.assertTrue(ms is not None)

    def testSmallBuffer(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = 1
        self.assertTrue(
            MultipartStream(
                input, boundary, iBufSize, ProgressNotifier(None, len(contents))
            )
        )

    def testThreeParamConstructor(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = len(boundary) + len(MultipartStream.BOUNDARY_PREFIX) + 1
        ms = MultipartStream(
            input, boundary, iBufSize, ProgressNotifier(None, len(contents))
        )
        self.assertTrue(ms is not None)

    # Class Methods End
