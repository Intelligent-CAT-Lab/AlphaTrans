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

        assert pBytesRead >= 0 and pBytesRead <= self.__expectedContentLength
        assert pContentLength == -1 or pContentLength == self.__expectedContentLength
        assert pItems >= 0 and pItems <= self.__expectedItems
        assert self.__bytesRead is None or pBytesRead >= self.__bytesRead
        self.__bytesRead = pBytesRead
        assert self.__items is None or pItems >= self.__items
        self.__items = pItems

    def checkFinished(self) -> None:

        assert self.__bytesRead == self.__expectedContentLength
        assert self.__items == self.__expectedItems

    def __init__(self, pContentLength: int, pItems: int) -> None:

        self.__expectedContentLength = pContentLength
        self.__expectedItems = pItems

    # Class Methods End


class ProgressListenerTest(unittest.TestCase):

    pass
