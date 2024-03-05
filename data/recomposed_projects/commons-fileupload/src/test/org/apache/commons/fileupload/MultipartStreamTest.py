# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.MultipartStream import *
import unittest
import io

# Imports End


class MultipartStreamTest(unittest.TestCase):

    # Class Fields Begin
    __BOUNDARY_TEXT: str = "myboundary"
    # Class Fields End

    # Class Methods Begin
    def testTwoParamConstructor(self) -> None:

        str_data = "foobar"
        contents = str_data.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        ms = MultipartStream.MultipartStream2(
            input, boundary, MultipartStream.ProgressNotifier(None, contents.length)
        )
        assert ms is not None

    def testSmallBuffer(self) -> None:

        strData = "foobar"
        contents = strData.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        iBufSize = 1
        MultipartStream(
            input,
            boundary,
            iBufSize,
            MultipartStream.ProgressNotifier(None, contents.length),
        )

    def testThreeParamConstructor(self) -> None:

        str_data = "foobar"
        contents = str_data.encode()
        input = io.BytesIO(contents)
        boundary = self.__BOUNDARY_TEXT.encode()
        i_buf_size = len(boundary) + MultipartStream.BOUNDARY_PREFIX.length + 1
        ms = MultipartStream(
            input,
            boundary,
            i_buf_size,
            MultipartStream.ProgressNotifier(None, contents.length),
        )
        assert ms is not None

    # Class Methods End
