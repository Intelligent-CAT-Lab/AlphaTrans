# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
import unittest
import typing
from typing import *

# Imports End


class ProgressListenerImpl(unittest.TestCase, ProgressListener):

    # Class Fields Begin
    __expectedContentLength: int = None
    __expectedItems: int = None
    __bytesRead: int = None
    __items: int = None
    # Class Fields End

    # Class Methods Begin
    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:

        self.assertTrue(
            pBytesRead >= 0 and pBytesRead <= self.__expectedContentLength,
            "pBytesRead is not in the expected range",
        )
        self.assertTrue(
            pContentLength == -1 or pContentLength == self.__expectedContentLength,
            "pContentLength is not in the expected range",
        )
        self.assertTrue(
            pItems >= 0 and pItems <= self.__expectedItems,
            "pItems is not in the expected range",
        )
        self.assertTrue(
            self.__bytesRead is None or pBytesRead >= self.__bytesRead,
            "pBytesRead is less than the previous value",
        )
        self.__bytesRead = pBytesRead
        self.assertTrue(
            self.__items is None or pItems >= self.__items,
            "pItems is less than the previous value",
        )
        self.__items = pItems

    def checkFinished(self) -> None:

        self.assertTrue(
            self.__expectedContentLength == self.__bytesRead,
            "Expected content length does not match bytes read",
        )
        self.assertTrue(
            self.__expectedItems == self.__items,
            "Expected items does not match actual items",
        )

    def __init__(self, pContentLength: int, pItems: int) -> None:

        self.__expectedContentLength = pContentLength
        self.__expectedItems = pItems

    # Class Methods End


class ProgressListenerTest(unittest.TestCase):

    pass
