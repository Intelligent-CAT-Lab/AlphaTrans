# Imports Begin
import unittest
import typing
from typing import *
from fileupload import ProgressListener

# Imports End


class ProgressListenerTest(unittest.TestCase):

    class ProgressListenerImpl(unittest.TestCase, ProgressListener):
        def __init__(self, pContentLength, pItems) -> None:
            self._expectedContentLength = pContentLength
            self._expectedItems = pItems
            self._bytesRead = None
            self._items = None

        def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
            self.assertTrue(0 <= pBytesRead <= self._expectedContentLength)
            self.assertTrue(pContentLength == -1 or pContentLength == self._expectedContentLength)
            self.assertTrue(0 <= pItems <= self._expectedItems)

            self.assertTrue(self._bytesRead is None or pBytesRead >= self._bytesRead)
            self._bytesRead = pBytesRead
            self.assertTrue(self._items is None or pItems >= self._items)
            self._items = pItems

        def check_finished(self) -> None:
            self.assertEqual(self._expectedContentLength, self._bytesRead)
            self.assertEqual(self._expectedItems, self._items)
    
