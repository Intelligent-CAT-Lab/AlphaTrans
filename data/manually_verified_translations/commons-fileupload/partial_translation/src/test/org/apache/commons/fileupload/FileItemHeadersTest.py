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

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual("content-disposition", next(headerNameEnumeration))
        self.assertEqual("content-type", next(headerNameEnumeration))
        self.assertEqual("testheader", next(headerNameEnumeration))
        self.assertFalse(next(headerNameEnumeration, None) is not None)

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

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(next(headerValueEnumeration, None) is not None)

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(next(headerValueEnumeration, None) is not None)

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(next(headerValueEnumeration, None) is not None)
        self.assertEqual(next(headerValueEnumeration), "headerValue4")
        self.assertFalse(next(headerValueEnumeration, None) is not None)

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader")
        self.assertFalse(next(headerValueEnumeration, None) is not None)
