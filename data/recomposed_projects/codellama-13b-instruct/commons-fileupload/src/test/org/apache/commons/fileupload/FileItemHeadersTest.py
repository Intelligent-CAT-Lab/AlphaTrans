# Imports Begin
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *
import unittest
import os
import typing
from typing import *

# Imports End


class FileItemHeadersTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
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
        self.assertEqual("content-disposition", headerNameEnumeration.next())
        self.assertEqual("content-type", headerNameEnumeration.next())
        self.assertEqual("testheader", headerNameEnumeration.next())
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
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "headerValue1")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "headerValue2")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "headerValue3")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEqual(headerValueEnumeration.next(), "headerValue4")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader")
        self.assertFalse(headerValueEnumeration.hasNext())

    # Class Methods End
