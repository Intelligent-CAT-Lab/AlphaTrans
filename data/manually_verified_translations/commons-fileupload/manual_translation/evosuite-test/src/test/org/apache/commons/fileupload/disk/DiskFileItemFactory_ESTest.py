from __future__ import annotations
import time
import re
import mock
import tempfile
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory import *

# from src.test.org.apache.commons.fileupload.disk.DiskFileItemFactory_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.testdata.EvoSuiteFile import *
# from src.main.org.evosuite.runtime.testdata.FileSystemHandling import *


class DiskFileItemFactory_ESTest(unittest.TestCase):

    def test10(self) -> None:
        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        int0 = diskFileItemFactory0.getSizeThreshold()
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())
        self.assertEqual(10240, int0)

    def test09(self) -> None:
        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        string0 = diskFileItemFactory0.getDefaultCharset()
        self.assertEqual("ISO-8859-1", string0)
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())

    def test08(self) -> None:

        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

        diskFileItemFactory0.setDefaultCharset("")
        diskFileItemFactory0.getDefaultCharset()
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())

    def test07(self) -> None:
        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        diskFileItemFactory0.getRepository()
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

    def test06(self) -> None:

        # Create a temporary file
        file0 = tempfile.NamedTemporaryFile(suffix=".Dl3rCgNOCnjY", prefix="7X")
        file0.close()

        # Create a DiskFileItemFactory instance
        diskFileItemFactory0 = DiskFileItemFactory(2163, pathlib.Path(file0.name))

        # Call the getRepository method
        diskFileItemFactory0.getRepository()

        # Assert the size threshold
        self.assertEqual(2163, diskFileItemFactory0.getSizeThreshold())

        # Assert the default charset
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

    def test05(self) -> None:

        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

        diskFileItemFactory0.setDefaultCharset(None)
        diskFileItemFactory0.getDefaultCharset()
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())

    def test04(self) -> None:

        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        mockFile0 = MockFile(")aqdqM(2WBA4-*??")
        diskFileItemFactory0.setRepository(mockFile0)
        diskFileItemFactory0.getRepository()
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())

    def test03(self) -> None:

        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        mockFile0 = MockFile("zdIj.-=r", "zdIj.-=r")
        MockFile.createTempFile("110(K?GwA9HJ=`", "zdIj.-=r", mockFile0)
        diskFileItemFactory0.setRepository(mockFile0)
        diskFileItemFactory0.getRepository()
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

    def test02(self) -> None:

        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        mockFile0 = MockFile(")aqdqM(2-*??")
        evoSuiteFile0 = EvoSuiteFile(")aqdqM(2-*??")
        FileSystemHandling.appendStringToFile(evoSuiteFile0, ")aqdqM(2-*??")
        diskFileItemFactory0.setRepository(mockFile0)
        diskFileItemFactory0.getRepository()
        self.assertEqual(10240, diskFileItemFactory0.getSizeThreshold())
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())

    def test01(self) -> None:
        diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1()
        diskFileItemFactory0.setSizeThreshold(-4440)
        int0 = diskFileItemFactory0.getSizeThreshold()
        self.assertEqual(-4440, int0)

    def test00(self) -> None:

        # Create a temporary file
        file0 = tempfile.NamedTemporaryFile(
            prefix="org.apache.commons.fileupload.disk.DiskFileItemFactory", suffix=""
        )
        file0.close()

        # Create an instance of DiskFileItemFactory
        diskFileItemFactory0 = DiskFileItemFactory(0, pathlib.Path(file0.name))

        # Get the size threshold
        int0 = diskFileItemFactory0.getSizeThreshold()

        # Assert that the size threshold is 0
        self.assertEqual(0, int0)

        # Assert that the default charset is "ISO-8859-1"
        self.assertEqual("ISO-8859-1", diskFileItemFactory0.getDefaultCharset())
