from __future__ import annotations
import re
import os
import typing
from typing import *
import enum
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *


class FileItemHeadersTest(unittest.TestCase):

    def testFileItemHeaders(self) -> None:
        a_mutable_file_item_headers = FileItemHeadersImpl()
        a_mutable_file_item_headers.add_header(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        a_mutable_file_item_headers.add_header("Content-Type", "text/plain")

        a_mutable_file_item_headers.add_header("TestHeader", "headerValue1")
        a_mutable_file_item_headers.add_header("TestHeader", "headerValue2")
        a_mutable_file_item_headers.add_header("TestHeader", "headerValue3")
        a_mutable_file_item_headers.add_header("testheader", "headerValue4")

        header_name_enumeration = a_mutable_file_item_headers.get_header_names()
        self.assertEqual("content-disposition", next(header_name_enumeration))
        self.assertEqual("content-type", next(header_name_enumeration))
        self.assertEqual("testheader", next(header_name_enumeration))
        self.assertFalse(next(header_name_enumeration))

        self.assertEqual(
            a_mutable_file_item_headers.get_header("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            a_mutable_file_item_headers.get_header("Content-Type"), "text/plain"
        )
        self.assertEqual(
            a_mutable_file_item_headers.get_header("content-type"), "text/plain"
        )
        self.assertEqual(
            a_mutable_file_item_headers.get_header("TestHeader"), "headerValue1"
        )
        self.assertIsNone(a_mutable_file_item_headers.get_header("DummyHeader"))

        header_value_enumeration: typing.Iterator[str]

        header_value_enumeration = a_mutable_file_item_headers.get_headers(
            "Content-Type"
        )
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "text/plain")
        self.assertFalse(next(header_value_enumeration))

        header_value_enumeration = a_mutable_file_item_headers.get_headers(
            "content-type"
        )
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "text/plain")
        self.assertFalse(next(header_value_enumeration))

        header_value_enumeration = a_mutable_file_item_headers.get_headers("TestHeader")
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "headerValue1")
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "headerValue2")
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "headerValue3")
        self.assertTrue(next(header_value_enumeration))
        self.assertEqual(next(header_value_enumeration), "headerValue4")
        self.assertFalse(next(header_value_enumeration))

        header_value_enumeration = a_mutable_file_item_headers.get_headers(
            "DummyHeader"
        )
        self.assertFalse(next(header_value_enumeration))
