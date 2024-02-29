# Imports Begin
import unittest
import typing
from typing import *

# Imports End


class FileItemHeadersTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_FileItemHeaders(self) -> None:

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
        self.assertEquals("content-disposition", headerNameEnumeration.next())
        self.assertEquals("content-type", headerNameEnumeration.next())
        self.assertEquals("testheader", headerNameEnumeration.next())
        self.assertFalse(headerNameEnumeration.hasNext())
        self.assertEquals(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEquals(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEquals(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEquals(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "text/plain")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "headerValue1")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "headerValue2")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "headerValue3")
        self.assertTrue(headerValueEnumeration.hasNext())
        self.assertEquals(headerValueEnumeration.next(), "headerValue4")
        self.assertFalse(headerValueEnumeration.hasNext())
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader")
        self.assertFalse(headerValueEnumeration.hasNext())

    # Class Methods End
