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
from src.main.org.apache.commons.fileupload.FileItem import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.FileUpload import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *

# from src.test.org.apache.commons.fileupload.FileUploadBase_ESTest_scaffolding import *
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.RequestContext import *
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class FileUploadBase_ESTest(unittest.TestCase):

    def test50(self) -> None:

        pass  # LLM could not translate this method

    def test49(self) -> None:

        pass  # LLM could not translate this method

    def test48(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(0, fileItemFactory0)
        hashMap0 = {}

        with self.assertRaises(RuntimeError):
            fileUpload0.createItem(hashMap0, False)

        try:
            verifyException("org.apache.commons.fileupload.FileUploadBase", e)
        except Exception as e:
            self.fail("Expecting exception: RuntimeError")

    def test47(self) -> None:

        pass  # LLM could not translate this method

    def test46(self) -> None:

        pass  # LLM could not translate this method

    def test45(self) -> None:

        pass  # LLM could not translate this method

    def test44(self) -> None:

        pass  # LLM could not translate this method

    def test43(self) -> None:

        pass  # LLM could not translate this method

    def test42(self) -> None:

        pass  # LLM could not translate this method

    def test41(self) -> None:

        pass  # LLM could not translate this method

    def test40(self) -> None:

        fileUploadBase_SizeLimitExceededException0 = SizeLimitExceededException(
            "BJ||BA-)4]mQ+K5w", 1442, 0
        )
        fileUploadBase_InvalidContentTypeException0 = InvalidContentTypeException(
            None, fileUploadBase_SizeLimitExceededException0
        )

    def test39(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "Content-type", -1, 0
        )
        string0 = fileUploadBase_FileSizeLimitExceededException0.getFileName()
        self.assertIsNone(string0)

    def test38(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "))%~uYXw", 2538, -2824
        )
        fileUploadBase_FileSizeLimitExceededException0.setFileName("-")
        self.assertEqual(
            "-", fileUploadBase_FileSizeLimitExceededException0.getFileName()
        )

    def test37(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "Content-disposition", 0, 0
        )
        fileUploadBase_FileSizeLimitExceededException0.setFieldName("Content-length")
        self.assertIsNone(fileUploadBase_FileSizeLimitExceededException0.getFileName())

    def test36(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "org.apache.commons.fileupload.FileUploadBase$IOFileUploadException",
            -1449,
            -1449,
        )
        string0 = fileUploadBase_FileSizeLimitExceededException0.getFieldName()
        self.assertIsNone(string0)

    def test35(self) -> None:

        mock_io_exception = IOError()
        file_upload_base_io_file_upload_exception = IOFileUploadException(
            "", mock_io_exception
        )
        throwable = file_upload_base_io_file_upload_exception.getCause()
        self.assertIs(throwable, mock_io_exception)

    def test34(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "org.apache.commons.fileupload.FileUploadBase$IOFileUploadException",
            -1449,
            -1449,
        )
        long0 = fileUploadBase_FileSizeLimitExceededException0.getPermittedSize()
        self.assertEqual(-1449, long0)

    def test33(self) -> None:

        fileUploadBase_FileSizeLimitExceededException0 = FileSizeLimitExceededException(
            "", 2091, -1184
        )
        long0 = fileUploadBase_FileSizeLimitExceededException0.getActualSize()
        self.assertEqual(2091, long0)

    def test32(self) -> None:
        fileUploadBase_FileUploadIOException0 = FileUploadIOException(None)
        throwable0 = fileUploadBase_FileUploadIOException0.getCause()
        self.assertIsNone(throwable0)

    def test31(self) -> None:

        class MockRequestContext(RequestContext):
            def getContentType(self) -> str:
                return "Invalid RFC 2047 encoded-word: "

        requestContext0 = MockRequestContext()
        boolean0 = FileUploadBase.isMultipartContent(requestContext0)
        self.assertFalse(boolean0)

    def test30(self) -> None:

        # Create a mock object for RequestContext
        requestContext0 = unittest.mock.Mock(spec=RequestContext)

        # Set the return value of getContentType method to None
        requestContext0.getContentType.return_value = None

        # Call the method under test
        boolean0 = FileUploadBase.isMultipartContent(requestContext0)

        # Assert that the result is False
        self.assertFalse(boolean0)

    def test29(self) -> None:

        class MockRequestContext(RequestContext):
            def getContentType(self) -> str:
                return "multipart/ce^nz.b.ce"

        requestContext0 = MockRequestContext()
        boolean0 = FileUploadBase.isMultipartContent(requestContext0)
        self.assertTrue(boolean0)

    def test28(self) -> None:

        fileUpload0 = FileUploadBase((-492), None)
        fileUpload0.getBoundary("Content-disposition")
        self.assertEqual((-1), fileUpload0.getFileSizeMax())
        self.assertEqual((-1), fileUpload0.getFileCountMax())
        self.assertEqual((-1), fileUpload0.getSizeMax())

    def test27(self) -> None:

        fileUpload0 = FileUpload(-1459597726, None)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("Content-disposition", "Content-disposition")
        string0 = fileUpload0._getFileName1(fileItemHeadersImpl0)
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertIsNone(string0)

    def test26(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(-1459597726, fileItemFactory0)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("Content-disposition", "form-data")
        string0 = fileUpload0._getFileName1(fileItemHeadersImpl0)
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getSizeMax())

    def test25(self) -> None:

        fileUpload0 = FileUpload(41, None)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("Content-disposition", "attachment")
        string0 = fileUpload0._getFileName1(fileItemHeadersImpl0)
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getFileCountMax())

    def test24(self) -> None:

        fileUpload0 = FileUpload(-1459597726, None)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("Content-disposition", "multipart/form-data")
        string0 = fileUpload0._getFieldName0(fileItemHeadersImpl0)
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())

    def test23(self) -> None:

        fileUpload0 = FileUpload(1843, None)
        fileItemHeadersImpl0 = FileItemHeadersImpl()
        fileItemHeadersImpl0.addHeader("Content-disposition", "form-dataform-data")
        string0 = fileUpload0._getFieldName0(fileItemHeadersImpl0)
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())

    def test22(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(1617, fileItemFactory0)

        try:
            fileUpload0.parseHeaders(" \r\n")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            FileUploadBase.verifyException(
                "org.apache.commons.fileupload.FileUploadBase", e
            )

    def test21(self) -> None:

        fileUpload0 = FileUpload(-209235087, None)
        try:
            fileUpload0.parseHeaders("\r")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test20(self) -> None:

        fileUpload0 = FileUpload(-1472806860, None)
        try:
            fileUpload0.parseHeaders(" \rY")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test19(self) -> None:

        fileUpload0 = FileUpload(23, None)
        try:
            fileUpload0._getFieldName0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test18(self) -> None:

        fileUpload0 = FileUpload(2147483645, None)
        try:
            fileUpload0.getFieldName2(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test17(self) -> None:

        fileUpload0 = FileUpload(-492, None)
        try:
            fileUpload0._getFileName0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test16(self) -> None:

        fileUpload0 = FileUpload(0, None)
        try:
            fileUpload0._getFileName1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test15(self) -> None:

        fileUpload0 = FileUpload(-333288148, None)
        try:
            fileUpload0.getHeader(None, "multipart/")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test14(self) -> None:

        fileUpload0 = FileUpload(-492, None)
        try:
            fileUpload0.getParsedHeaders("#)u)U")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test13(self) -> None:

        fileUpload0 = FileUpload(2147483645, None)
        try:
            fileUpload0.getParsedHeaders(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test12(self) -> None:
        try:
            FileUploadBase.isMultipartContent(None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test11(self) -> None:

        fileUpload0 = FileUpload(-492, None)
        try:
            fileUpload0.parseHeaders(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.fileupload.FileUploadBase", e)

    def test10(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(0, fileItemFactory0)
        fileItemFactory1 = unittest.mock.Mock(spec=FileItemFactory)
        fileItemFactory1.createItem.return_value = None
        fileUpload0.setFileItemFactory(fileItemFactory1)
        hashMap0 = {}
        fileUpload0.createItem(hashMap0, False)
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())

    def test09(self) -> None:
        fileUpload0 = FileUpload(-454, None)
        hashMap0 = {}
        string0 = fileUpload0._getFieldName2(hashMap0)
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getFileSizeMax())

    def test08(self) -> None:
        fileUpload0 = FileUpload(561, None)
        fileUpload0.setFileCountMax(561)
        long0 = fileUpload0.getFileCountMax()
        self.assertEqual(561, long0)

    def test07(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(1, fileItemFactory0)
        fileUpload0.getFileItemFactory()
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())

    def test06(self) -> None:
        fileUpload0 = FileUpload(2485, None)
        fileUpload0.getFileItemFactory()
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())

    def test05(self) -> None:
        fileUpload0 = FileUpload(1843, None)
        hashMap0 = {}
        string0 = fileUpload0._getFileName0(hashMap0)
        self.assertIsNone(string0)
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())

    def test04(self) -> None:

        pass  # LLM could not translate this method

    def test03(self) -> None:

        fileItemFactory0 = unittest.mock.Mock(spec=FileItemFactory)
        fileUpload0 = FileUpload(0, fileItemFactory0)
        hashMap0 = {}
        fileUpload0.getHeader(hashMap0, "")
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
        self.assertEqual(-1, fileUpload0.getSizeMax())

    def test02(self) -> None:
        fileUpload0 = FileUpload(1843, None)
        fileUpload0.setSizeMax(1843)
        long0 = fileUpload0.getSizeMax()
        self.assertEqual(1843, long0)

    def test01(self) -> None:

        pass  # LLM could not translate this method

    def test00(self) -> None:
        fileUpload0 = FileUpload(561, None)
        fileUpload0.setFileItemFactory(None)
        self.assertEqual(-1, fileUpload0.getSizeMax())
        self.assertEqual(-1, fileUpload0.getFileCountMax())
        self.assertEqual(-1, fileUpload0.getFileSizeMax())
