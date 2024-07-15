from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *

# from src.test.org.apache.commons.fileupload.disk.DiskFileItem_ESTest_scaffolding import *
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DiskFileItem_ESTest(unittest.TestCase):

    def test20(self) -> None:

        mockFile0 = MockFile("", "")
        diskFileItem0 = DiskFileItem("", "", True, "UTF8", 299, mockFile0)
        diskFileItem0.getCharSet()
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("", diskFileItem0.getFieldName())

    def test19(self) -> None:

        uRI0 = MockURI.aFileURI
        mockFile0 = MockFile(uRI0)
        diskFileItem0 = DiskFileItem("", "", False, "", 0, mockFile0)
        string0 = diskFileItem0.getName()
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("", string0)
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual("", diskFileItem0.getFieldName())
        self.assertFalse(diskFileItem0.isFormField())

    def test18(self) -> None:

        mockFile0 = MockFile("+")
        diskFileItem0 = DiskFileItem("+", "+", True, "+", 1638, mockFile0)
        string0 = diskFileItem0.getFieldName()
        self.assertEqual("+", string0)
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("+", diskFileItem0.getContentType())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test17(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem("ja_jp.eucjp", "", False, None, 0, mockFile0)
        diskFileItem0.getHeaders()
        self.assertFalse(diskFileItem0.isFormField())
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("ja_jp.eucjp", diskFileItem0.getFieldName())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test16(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem("ja_jp.eucjp", "", False, None, 0, mockFile0)
        boolean0 = diskFileItem0.isFormField()
        self.assertFalse(boolean0)
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("ja_jp.eucjp", diskFileItem0.getFieldName())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test15(self) -> None:

        mockFile0 = MockFile("+")
        diskFileItem0 = DiskFileItem("+", "+", True, "+", 1638, mockFile0)
        diskFileItem0.setFormField(True)
        self.assertEqual("+", diskFileItem0.getContentType())
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual("+", diskFileItem0.getFieldName())

    def test14(self) -> None:

        mockFile0 = MockFile("", "")
        diskFileItem0 = DiskFileItem("", "", True, "UTF8", 299, mockFile0)
        diskFileItem0.setFieldName("")
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("", diskFileItem0.getFieldName())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test13(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem("ja_jp.eucjp", "", False, None, 0, mockFile0)
        string0 = diskFileItem0.getDefaultCharset()
        self.assertFalse(diskFileItem0.isFormField())
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("ISO-8859-1", string0)
        self.assertEqual("ja_jp.eucjp", diskFileItem0.getFieldName())

    def test12(self) -> None:

        diskFileItem0 = DiskFileItem(
            "cuM11<R>i KBP,1COv",
            "cuM11<R>i KBP,1COv",
            True,
            "cuM11<R>i KBP,1COv",
            100000000,
            None,
        )
        file0 = diskFileItem0._getTempFile()
        self.assertEqual(
            "upload_00000000_0100_4000_8200_000003000000_00000000.tmp", file0.name
        )
        self.assertIsNotNone(file0)

    def test11(self) -> None:

        mockFile0 = MockFile("upload_%s_%s.tmp")
        diskFileItem0 = DiskFileItem("", "upload_%s_%s.tmp", False, "", 2952, mockFile0)
        string0 = diskFileItem0.getContentType()
        self.assertFalse(diskFileItem0.isFormField())
        self.assertEqual("upload_%s_%s.tmp", string0)
        self.assertEqual("", diskFileItem0.getFieldName())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test10(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem("ja_jp.eucjp", "", False, None, 0, mockFile0)
        string0 = diskFileItem0.getContentType()
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual("", string0)
        self.assertEqual("ja_jp.eucjp", diskFileItem0.getFieldName())
        self.assertIsNotNone(string0)
        self.assertFalse(diskFileItem0.isFormField())

    def test09(self) -> None:

        mockFile0 = MockFile("u8d0!/R", "%zr8")
        diskFileItem0 = DiskFileItem(None, None, False, '"m', 3475, mockFile0)
        string0 = diskFileItem0.getContentType()
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertFalse(diskFileItem0.isFormField())
        self.assertIsNone(string0)

    def test08(self) -> None:

        uRI0 = MockURI.aFileURI
        mockFile0 = MockFile(uRI0)
        diskFileItem0 = DiskFileItem("", "", False, "", 0, mockFile0)
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

        diskFileItem0.setDefaultCharset("")
        diskFileItem0.getDefaultCharset()
        self.assertEqual("", diskFileItem0.getDefaultCharset())

    def test07(self) -> None:

        mockFile0 = MockFile("v$IJC)d$uJvO2$9aUX!!", "v$IJC)d$uJvO2$9aUX!!")
        diskFileItem0 = DiskFileItem("", "", True, "", 0, mockFile0)
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

        diskFileItem0.setDefaultCharset(None)
        string0 = diskFileItem0.getDefaultCharset()
        self.assertEqual("", diskFileItem0.getFieldName())
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertIsNone(string0)

    def test06(self) -> None:

        mockFile0 = MockFile("upload_%s_%s.tmp")
        diskFileItem0 = DiskFileItem("", "upload_%s_%s.tmp", False, "", 2952, mockFile0)
        string0 = diskFileItem0.getFieldName()
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual("", string0)
        self.assertEqual("upload_%s_%s.tmp", diskFileItem0.getContentType())
        self.assertFalse(diskFileItem0.isFormField())

    def test05(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem(
            None,
            "",
            True,
            "org.apache.commons.fileupload.disk.DiskFileItem",
            0,
            mockFile0,
        )
        string0 = diskFileItem0.getFieldName()
        self.assertIsNone(string0)
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertTrue(diskFileItem0.isFormField())

    def test04(self) -> None:

        mockFile0 = MockFile("&ST2Spw")
        diskFileItem0 = DiskFileItem("ISO-8859-1", "", False, "", 0, mockFile0)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        diskFileItem0.setHeaders(fileItemHeadersImpl0)
        diskFileItem0.getHeaders()
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertEqual("ISO-8859-1", diskFileItem0.getFieldName())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertFalse(diskFileItem0.isFormField())

    def test03(self) -> None:

        file0 = MockFile.createTempFile(
            "cr(7Y_)3xc]", "org.apache.commons.fileupload.disk.DiskFileItem"
        )
        diskFileItem0 = DiskFileItem('q>|"I', "qW5", False, "cr(7Y_)3xc]", -2033, file0)
        string0 = diskFileItem0.getName()
        self.assertEqual("qW5", diskFileItem0.getContentType())
        self.assertFalse(diskFileItem0.isFormField())
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
        self.assertEqual('q>|"I', diskFileItem0.getFieldName())
        self.assertEqual("cr(7Y_)3xc]", string0)

    def test02(self) -> None:

        mockFile0 = MockFile(
            "org.apache.commons.fileupload.util.FileItemHeadersImpl", "=/r+>pCha:h]}7f"
        )
        diskFileItem0 = DiskFileItem(
            None, "=/r+>pCha:h]}7f", True, None, -1458, mockFile0
        )
        string0 = diskFileItem0.getName()
        self.assertTrue(diskFileItem0.isFormField())
        self.assertEqual("=/r+>pCha:h]}7f", diskFileItem0.getContentType())
        self.assertIsNone(string0)
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())

    def test01(self) -> None:

        mockFile0 = MockFile("", "")
        diskFileItem0 = DiskFileItem("", "", True, "UTF8", 299, mockFile0)
        file0 = diskFileItem0._getTempFile()
        file1 = MockFile.createTempFile("UTF8", "", file0)
        #  // Unstable assertion: self.assertEqual("/upload_00000000_0100_4000_8200_000003000000_00000053.tmp", file1.parent)

        file2 = diskFileItem0._getTempFile()
        #  // Unstable assertion: self.assertEqual("/upload_00000000_0100_4000_8200_000003000000_00000053.tmp", str(file2))

    def test00(self) -> None:

        mockFile0 = MockFile("")
        diskFileItem0 = DiskFileItem(
            None,
            "",
            True,
            "org.apache.commons.fileupload.disk.DiskFileItem",
            0,
            mockFile0,
        )
        boolean0 = diskFileItem0.isFormField()
        self.assertEqual("", diskFileItem0.getContentType())
        self.assertTrue(boolean0)
        self.assertEqual("ISO-8859-1", diskFileItem0.getDefaultCharset())
