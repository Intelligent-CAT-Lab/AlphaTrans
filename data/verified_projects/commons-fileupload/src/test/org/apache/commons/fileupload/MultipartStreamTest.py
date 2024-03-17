# Imports Begin
import unittest
from io import BytesIO
from src.main.org.apache.commons.fileupload.MultipartStream import MultipartStream, ProgressNotifier

# Imports End


class MultipartStreamTest(unittest.TestCase):

    # Class Fields Begin
    __BOUNDARY_TEXT: str = "myboundary"
    # Class Fields End

    # Class Methods Begin
    def test_ThreeParamConstructor(self) -> None:

        try:
            strData = "foobar"
            contents = strData.encode()
            input = BytesIO(contents)
            boundary = self.__BOUNDARY_TEXT.encode()
            iBufSize = len(boundary) + len(MultipartStream._BOUNDARY_PREFIX) + 1
            ms = MultipartStream(
                input,
                boundary,
                iBufSize,
                ProgressNotifier(None, len(contents))
            )
            self.assertIsNotNone(ms)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_SmallBuffer(self) -> None:

        with self.assertRaises(ValueError):
            strData = "foobar"
            contents = strData.encode()
            input = BytesIO(contents)
            boundary = self.__BOUNDARY_TEXT.encode()
            iBufSize = 1
            _ = MultipartStream(
                input,
                boundary,
                iBufSize,
                ProgressNotifier(None, len(contents))
            )

    def test_TwoParamConstructor(self) -> None:

        try:
            strData = "foobar"
            contents = strData.encode()
            input = BytesIO(contents)
            boundary = self.__BOUNDARY_TEXT.encode()
            ms = MultipartStream.MultipartStream2(
                input,
                boundary,
                ProgressNotifier(None, len(contents))
            )
            self.assertIsNotNone(ms)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
