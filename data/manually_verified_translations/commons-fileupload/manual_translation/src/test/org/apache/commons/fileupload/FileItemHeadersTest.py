from __future__ import annotations
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *


class PeekableIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.peeked is not None:
            next_item = self.peeked
            self.peeked = None
            return next_item
        return next(self.iterator)
    
    def hasNext(self):
        if self.peeked is None:
            try:
                self.peeked = next(self.iterator)
            except StopIteration:
                return False
        return True


class FileItemHeadersTest(unittest.TestCase):

    def testFileItemHeaders(self) -> None:

        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")

        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = PeekableIterator(aMutableFileItemHeaders.getHeaderNames())
        self.assertEqual("content-disposition", next(headerNameEnumeration))
        self.assertEqual("content-type", next(headerNameEnumeration))
        self.assertEqual("testheader", next(headerNameEnumeration))
        self.assertFalse(headerNameEnumeration.hasNext())

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = PeekableIterator(aMutableFileItemHeaders.getHeaders("Content-Type"))
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())

        headerValueEnumeration = PeekableIterator(aMutableFileItemHeaders.getHeaders("content-type"))
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())

        headerValueEnumeration = PeekableIterator(aMutableFileItemHeaders.getHeaders("TestHeader"))
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(next(headerValueEnumeration), "headerValue4")
        self.assertFalse(headerValueEnumeration.hasNext())

        headerValueEnumeration = PeekableIterator(aMutableFileItemHeaders.getHeaders("DummyHeader"))
        self.assertFalse(headerValueEnumeration.hasNext())
