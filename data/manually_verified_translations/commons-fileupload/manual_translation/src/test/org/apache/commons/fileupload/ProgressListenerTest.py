from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class ProgressListenerImpl(ProgressListener):

    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:

        assert pBytesRead >= 0 and pBytesRead <= self.__expectedContentLength
        assert pContentLength == -1 or pContentLength == self.__expectedContentLength
        assert pItems >= 0 and pItems <= self.__expectedItems

        assert self.__bytesRead is None or pBytesRead >= self.__bytesRead
        self.__bytesRead = pBytesRead
        assert self.__items is None or pItems >= self.__items
        self.__items = pItems

    def checkFinished(self) -> None:

        assert self.__expectedContentLength == self.__bytesRead
        assert self.__expectedItems == self.__items

    def __init__(self, pContentLength: int, pItems: int) -> None:
        self.__expectedContentLength = pContentLength
        self.__expectedItems = pItems
        self.__bytesRead = None
        self.__items = None


class ProgressListenerTest:

    pass
