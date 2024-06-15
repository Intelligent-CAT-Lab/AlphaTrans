import pytest

# Imports Begin
import unittest
from typing import *
from src.main.org.apache.commons.fileupload.ProgressListener import ProgressListener

# Imports End


class ProgressListenerTest(unittest.TestCase):

    class ProgressListenerImpl(ProgressListener):
        def __init__(self, pContentLength, pItems) -> None:
            self._expectedContentLength = pContentLength
            self._expectedItems = pItems
            self._bytesRead = None
            self._items = None

        def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
            unittest.TestCase().assertTrue(0 <= pBytesRead <= self._expectedContentLength)
            unittest.TestCase().assertTrue(pContentLength == -1 or pContentLength == self._expectedContentLength)
            unittest.TestCase().assertTrue(0 <= pItems <= self._expectedItems)

            unittest.TestCase().assertTrue(self._bytesRead is None or pBytesRead >= self._bytesRead)
            self._bytesRead = pBytesRead
            unittest.TestCase().assertTrue(self._items is None or pItems >= self._items)
            self._items = pItems

        def check_finished(self) -> None:
            unittest.TestCase().assertEqual(self._expectedContentLength, self._bytesRead)
            unittest.TestCase().assertEqual(self._expectedItems, self._items)
    
