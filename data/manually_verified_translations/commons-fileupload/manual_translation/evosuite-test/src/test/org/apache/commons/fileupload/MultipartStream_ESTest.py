from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.MultipartStream import *

# from src.test.org.apache.commons.fileupload.MultipartStream_ESTest_scaffolding import *
from src.main.org.apache.commons.fileupload.ProgressListener import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class MultipartStream_ESTest(unittest.TestCase):

    def test57(self) -> None:

        pass  # LLM could not translate this method

    def test56(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        assert multipartStream_ItemInputStream0.isClosed() == False
        assert multipartStream_ItemInputStream0.available() == 0

    def test55(self) -> None:

        pipedInputStream0 = io.BytesIO()
        byteArray0 = bytearray(19)
        multipartStream0 = MultipartStream.MultipartStream3(
            pipedInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        multipartStream_ItemInputStream0.getBytesRead()
        self.assertEqual(0, multipartStream_ItemInputStream0.available())

    def test54(self) -> None:

        try:
            MultipartStream.MultipartStream0()
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test53(self) -> None:

        byteArray0 = bytearray(1)
        pipedOutputStream0 = io.BytesIO()
        pipedInputStream0 = io.BytesIO(pipedOutputStream0.getvalue())
        dataInputStream0 = io.BufferedReader(pipedInputStream0)
        multipartStream0 = MultipartStream.MultipartStream3(
            dataInputStream0, byteArray0
        )
        string0 = multipartStream0.getHeaderEncoding()
        self.assertIsNone(string0)

    def test52(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream0.setHeaderEncoding("")
        self.assertEqual(10240, MultipartStream.HEADER_PART_SIZE_MAX)

    def test51(self) -> None:

        byteArray0 = bytearray(9)
        multipartStream0 = MultipartStream.MultipartStream3(None, byteArray0)
        byteArray1 = bytearray(4)
        try:
            multipartStream0.setBoundary(byteArray1)
            self.fail("Expecting exception: IOException")

        except IllegalBoundaryException as e:
            # The length of a boundary token cannot be changed
            self.assertEqual(str(e), "The length of a boundary token cannot be changed")

    def test50(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()

        with pytest.raises(ValueError):
            MultipartStream.MultipartStream1(
                multipartStream_ItemInputStream0, byteArray0, -10
            )
            pytest.fail("Expecting exception: ValueError")

    def test49(self) -> None:

        inputStream0 = io.BytesIO(b"")
        byteArray0 = bytearray([1])
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        try:
            multipartStream0.readBoundary()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Stream ended unexpectedly
            #
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test48(self) -> None:

        inputStream0 = io.BytesIO(b"")
        byteArray0 = bytearray([0])
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream0.setBoundary(byteArray0)
        self.assertIsNone(multipartStream0.getHeaderEncoding())

    def test47(self) -> None:

        byteArray0 = bytearray(1)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        byteArray1 = bytearray(5)
        byteArray1[0] = 13
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray1
        )
        self.assertEqual(13, MultipartStream.CR)

    def test46(self) -> None:

        byteArray0 = bytearray(1)
        byteArray0[0] = 13
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        multipartStream0 = MultipartStream.MultipartStream3(
            bufferedInputStream0, byteArray0
        )
        try:
            multipartStream0.readHeaders()
            self.fail("Expecting exception: IOException")

        except FileUploadIOException as e:
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test45(self) -> None:
        byteArray0 = bytearray(1)
        boolean0 = MultipartStream.arrayequals(byteArray0, byteArray0, -2071)
        self.assertTrue(boolean0)

    def test44(self) -> None:
        byteArray0 = [0] * 9
        try:
            MultipartStream.arrayequals(byteArray0, byteArray0, 70)
            self.fail("Expecting exception: IndexError")
        except IndexError as e:
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test43(self) -> None:

        fileDescriptor0 = io.FileIO("test.txt", "r")
        mockFileInputStream0 = io.BufferedReader(fileDescriptor0)
        byteArray0 = bytearray()
        multipartStream0 = MultipartStream.MultipartStream3(
            mockFileInputStream0, byteArray0
        )

        try:
            multipartStream0._findByte(36, -2044)
            self.fail("Expecting exception: IndexError")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of range")

    def test42(self) -> None:

        byteArray0 = bytearray(23)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        multipartStream0 = MultipartStream.MultipartStream3(
            bufferedInputStream0, byteArray0
        )
        multipartStream0.readByte()
        int0 = multipartStream0.findByte(36, 8)
        self.assertEqual(0, byteArrayInputStream0.readable())
        self.assertEqual(-1, int0)

    def test41(self) -> None:

        byteArray0 = bytearray(2)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream(
            byteArrayInputStream0, byteArray0, 25, multipartStream_ProgressNotifier0
        )
        multipartStream_ItemInputStream0 = ItemInputStream()
        int0 = multipartStream_ItemInputStream0.read0()
        self.assertEqual(0, byteArrayInputStream0.readable())
        self.assertEqual(0, int0)

    def test40(self) -> None:

        byteArray0 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.close1(True)
        try:
            multipartStream_ItemInputStream0.read()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test39(self) -> None:

        byteArray0 = bytearray(3)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        try:
            multipartStream_ItemInputStream0.readAllBytes()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Stream ended unexpectedly
            #
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test38(self) -> None:

        byteArray0 = bytearray(2)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1)
        byteArray1 = bytearray(9)
        byteArray1[2] = -1
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream(
            byteArrayInputStream0, byteArray0, 25, multipartStream_ProgressNotifier0
        )
        multipartStream_ItemInputStream0 = ItemInputStream()
        byteArrayInputStream0.read(byteArray0)
        int0 = multipartStream_ItemInputStream0.read()
        self.assertEqual(1, multipartStream_ItemInputStream0.getBytesRead())
        self.assertEqual(255, int0)

    def test37(self) -> None:

        file_descriptor0 = io.FileIO("file_path", "r")
        mock_file_input_stream0 = io.BufferedReader(file_descriptor0)
        byte_array0 = bytearray(3)
        multipart_stream_progress_notifier0 = ProgressNotifier(None, 0)
        multipart_stream0 = MultipartStream.MultipartStream2(
            mock_file_input_stream0, byte_array0, multipart_stream_progress_notifier0
        )
        multipart_stream_item_input_stream0 = multipart_stream0.ItemInputStream()
        multipart_stream_item_input_stream0.read1(byte_array0, 13, 0)
        self.assertEqual(0, multipart_stream_item_input_stream0.available())

    def test36(self) -> None:

        byteArray0 = bytearray(3)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.skip(-1321)

        try:
            multipartStream_ItemInputStream0.read1(byteArray1, 10240, -2532)
            self.fail("Expecting exception: IndexError")

        except IndexError:
            pass

    def test35(self) -> None:

        byteArray0 = bytearray(3)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()

        try:
            multipartStream_ItemInputStream0.read1(byteArray1, 13, 1024)
            self.fail("Expecting exception: IndexError")

        except IndexError:
            pass

    def test34(self) -> None:

        byteArray0 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.close1(True)
        multipartStream_ItemInputStream0.close0()
        self.assertTrue(multipartStream_ItemInputStream0.isClosed())

    def test33(self) -> None:

        byteArray0 = bytearray(23)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        byteArray1 = bytearray(0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray1
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.skip(0)
        try:
            multipartStream_ItemInputStream0.close0()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Stream ended unexpectedly
            #
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test32(self) -> None:

        byteArray0 = bytearray(2)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream(
            byteArrayInputStream0, byteArray0, 25, multipartStream_ProgressNotifier0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.close1(True)
        try:
            multipartStream_ItemInputStream0.skip(0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test31(self) -> None:
        multipartStream_IllegalBoundaryException0 = IllegalBoundaryException(
            "]j`?$`2Z)i(q"
        )

    def test30(self) -> None:
        multipartStream_MalformedStreamException0 = MalformedStreamException(
            "[pyuK61Ga;b5b)id+"
        )

    def test29(self) -> None:

        inputStream0 = io.BytesIO()
        multipartStream_ProgressNotifier0 = ProgressNotifier(None, 0)
        multipartStream0 = None
        try:
            multipartStream0 = MultipartStream(
                inputStream0, None, 1024, multipartStream_ProgressNotifier0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # boundary may not be null
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test28(self) -> None:

        pipedInputStream0 = io.BytesIO()
        byteArray0 = bytearray(2)
        multipartStream0 = None

        try:
            multipartStream0 = MultipartStream(pipedInputStream0, byteArray0, 5, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The buffer size specified for the MultipartStream is too small
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test27(self) -> None:

        byteArray0 = bytearray(3)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream0.readByte()
        byte0 = multipartStream0.readByte()
        self.assertEqual(0, len(byteArrayInputStream0.read()))
        self.assertEqual(0, byte0)

    def test26(self) -> None:

        inputStream0 = io.BytesIO(b"")
        byteArray0 = bytearray([1])
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        try:
            multipartStream0.readByte()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # No more data is available
            self.assertEqual(str(e), "No more data is available")

    def test25(self) -> None:

        byteArray0 = bytearray(1)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, 9)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream(
            byteArrayInputStream0, byteArray0, 59, multipartStream_ProgressNotifier0
        )
        multipartStream0.readByte()
        self.assertEqual(0, len(byteArrayInputStream0.read()))

    def test24(self) -> None:

        byteArray0 = bytearray(1)
        byteArray1 = bytearray(4)
        byteArray1[0] = 45
        boolean0 = MultipartStream.arrayequals(byteArray1, byteArray0, 13)
        self.assertFalse(boolean0)

    def test23(self) -> None:

        pipedInputStream0 = io.BytesIO()
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1815)

        try:
            MultipartStream.MultipartStream2(
                pipedInputStream0, None, multipartStream_ProgressNotifier0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # boundary may not be null
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test22(self) -> None:

        pipedInputStream0 = io.BytesIO()

        try:
            MultipartStream.MultipartStream3(pipedInputStream0, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test21(self) -> None:
        byteArray0 = bytearray(19)
        try:
            MultipartStream.arrayequals(None, byteArray0, 1748)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test20(self) -> None:

        byteArray0 = bytearray(23)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        byteArray1 = bytearray(0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray1
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        multipartStream_ItemInputStream0.skip(-8)

        try:
            multipartStream0.newInputStream()
            self.fail("Expecting exception: IndexError")

        except IndexError as e:
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test19(self) -> None:

        byteArray0 = bytearray(4)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = ItemInputStream()
        multipartStream_ItemInputStream0.skip(-284)

        try:
            multipartStream0.readBoundary()
            self.fail("Expecting exception: IndexError")

        except IndexError as e:
            verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test18(self) -> None:

        byteArray0 = bytearray(3)
        multipartStream0 = MultipartStream.MultipartStream1(None, byteArray0, 468)
        # Undeclared exception in Java code
        try:
            multipartStream0.readByte()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test17(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, 0)
        multipartStream1 = MultipartStream.MultipartStream2(
            multipartStream_ItemInputStream0,
            byteArray0,
            multipartStream_ProgressNotifier0,
        )
        try:
            multipartStream1.readByte()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Stream ended unexpectedly
            self.assertEqual(str(e), "No more data is available")

    def test16(self) -> None:

        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(None, byteArray0)

        try:
            multipartStream0.readHeaders()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test15(self) -> None:

        byteArray0 = bytearray(0)
        multipartStream0 = MultipartStream.MultipartStream3(None, byteArray0)
        int0 = multipartStream0._findSeparator()
        self.assertEqual(-1, int0)

    def test14(self) -> None:

        byteArray0 = bytearray(23)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        byteArray1 = bytearray(0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray1
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        multipartStream_ItemInputStream0.skip(0)
        self.assertEqual(0, len(byteArrayInputStream0.read()))

        multipartStream_ItemInputStream1 = multipartStream0.newInputStream()
        self.assertEqual(19, multipartStream_ItemInputStream1.available())

    def test13(self) -> None:

        byteArray0 = bytearray(23)
        byteArray0[0] = 20
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        multipartStream0 = MultipartStream.MultipartStream3(
            bufferedInputStream0, byteArray0
        )
        byte0 = multipartStream0.readByte()
        self.assertEqual(0, len(byteArrayInputStream0.read()))
        self.assertEqual(20, byte0)

    def test12(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0)
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        int0 = multipartStream_ItemInputStream0.available()
        self.assertEqual(0, int0)

    def test11(self) -> None:
        multipartStream_ProgressNotifier0 = ProgressNotifier(None, 0)
        multipartStream_ProgressNotifier0.noteBytesRead(0)

    def test10(self) -> None:

        byteArray0 = bytearray(4)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        multipartStream0 = MultipartStream(
            bufferedInputStream0, byteArray0, 9, multipartStream_ProgressNotifier0
        )
        self.assertEqual(10240, MultipartStream.HEADER_PART_SIZE_MAX)

    def test09(self) -> None:

        pipedOutputStream0 = io.BytesIO()
        pipedInputStream0 = io.BytesIO()
        byteArray0 = bytearray(1)
        multipartStream0 = MultipartStream.MultipartStream1(
            pipedInputStream0, byteArray0, 490
        )
        byteArray1 = bytearray(6)
        try:
            multipartStream0.setBoundary(byteArray1)
            self.fail("Expecting exception: IOException")

        except IllegalBoundaryException as e:
            # The length of a boundary token cannot be changed
            self.assertEqual(str(e), "The length of a boundary token cannot be changed")

    def test08(self) -> None:

        byteArray0 = bytearray(4)
        byteArray0[0] = 20
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        progressListener0 = unittest.mock.Mock(spec=ProgressListener)
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, 20)
        multipartStream0 = MultipartStream(
            bufferedInputStream0, byteArray0, 20, multipartStream_ProgressNotifier0
        )

        try:
            multipartStream0.readHeaders()
            self.fail("Expecting exception: IOException")

        except FileUploadIOException as e:
            self.verifyException("org.apache.commons.fileupload.MultipartStream", e)

    def test07(self) -> None:
        byteArray0 = bytearray(19)
        boolean0 = MultipartStream.arrayequals(byteArray0, byteArray0, 13)
        self.assertTrue(boolean0)

    def test06(self) -> None:

        fileDescriptor0 = io.FileIO("file.txt", "r")
        mockFileInputStream0 = io.BufferedReader(fileDescriptor0)
        byteArray0 = bytearray()
        multipartStream0 = MultipartStream.MultipartStream3(
            mockFileInputStream0, byteArray0
        )
        int0 = multipartStream0._findByte(0x24, 8)
        self.assertEqual(-1, int0)

    def test05(self) -> None:

        byteArray0 = bytearray(4)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        multipartStream_ItemInputStream0.skip(13)
        int0 = multipartStream0._findByte(-1, 0)
        self.assertEqual(0, byteArrayInputStream0.readable())
        self.assertEqual(-1, int0)

    def test04(self) -> None:

        byteArray0 = bytearray(1)
        byteArray1 = bytearray(8)
        byteArray1[0] = 13
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        try:
            multipartStream_ItemInputStream0.close0()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Stream ended unexpectedly
            #
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test03(self) -> None:

        byteArray0 = bytearray(4)
        byteArray0[0] = 20
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        bufferedInputStream0 = io.BufferedReader(byteArrayInputStream0)
        multipartStream0 = MultipartStream.MultipartStream3(
            bufferedInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.ItemInputStream()
        try:
            multipartStream_ItemInputStream0.read1(byteArray0, 1, 2006)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            #
            # Stream ended unexpectedly
            #
            self.verifyException(
                "org.apache.commons.fileupload.MultipartStream$ItemInputStream", e
            )

    def test02(self) -> None:

        byteArray0 = bytearray(3)
        byteArrayInputStream0 = io.BytesIO(byteArray0)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream0.readByte()
        multipartStream_ItemInputStream0 = ItemInputStream()
        assert byteArrayInputStream0.readable() == False

    def test01(self) -> None:

        byteArray0 = bytearray(3)
        byteArray1 = bytearray(9)
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream.MultipartStream3(
            byteArrayInputStream0, byteArray0
        )
        multipartStream_ItemInputStream0 = multipartStream0.newInputStream()
        multipartStream_ItemInputStream0.skip(13)
        multipartStream0.newInputStream()
        self.assertEqual(0, len(byteArrayInputStream0.read()))

    def test00(self) -> None:

        byteArray0 = bytearray(3)
        progressListener0 = ProgressListener()
        multipartStream_ProgressNotifier0 = ProgressNotifier(progressListener0, -1)
        byteArray1 = bytearray(9)
        byteArray1[0] = 9
        byteArrayInputStream0 = io.BytesIO(byteArray1)
        multipartStream0 = MultipartStream(
            byteArrayInputStream0, byteArray0, 9, multipartStream_ProgressNotifier0
        )
        multipartStream_ItemInputStream0 = ItemInputStream()
        int0 = multipartStream_ItemInputStream0.read()
        self.assertEqual(0, byteArrayInputStream0.readable())
        self.assertEqual(9, int0)
