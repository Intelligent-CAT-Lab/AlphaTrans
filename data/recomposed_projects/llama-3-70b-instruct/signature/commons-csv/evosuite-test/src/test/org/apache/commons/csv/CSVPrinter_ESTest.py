from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *

# from src.test.org.apache.commons.csv.CSVPrinter_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CSVPrinter_ESTest(unittest.TestCase):

    def test41(self) -> None:

        cSVFormat_Builder0 = CSVFormat.Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVPrinter0 = cSVFormat0.printer()
        appendable0 = cSVPrinter0.getOut()
        self.assertIsNotNone(appendable0)

    def test40(self) -> None:

        cSVFormat0 = CSVFormat.RFC4180
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.close()

    def test39(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringWriter0 = io.StringIO(new_line="")
        stringBuffer0 = stringWriter0.getvalue()
        cSVPrinter0 = cSVFormat0.print0(stringBuffer0)
        cSVPrinter0.close1(False)

    def test38(self) -> None:

        charArray0 = ["\0", "\0"]
        charBuffer0 = io.StringIO("".join(charArray0))
        cSVFormat0 = CSVFormat.TDF
        cSVPrinter0 = CSVPrinter(charBuffer0, cSVFormat0)
        cSVPrinter0.flush()

    def test37(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        character0 = ")"
        cSVFormat_Builder0.setCommentMarker1(character0)
        objectArray0 = [None] * 5
        objectArray0[0] = cSVFormat_Builder0
        cSVFormat_Builder1 = cSVFormat_Builder0.setHeaderComments0(objectArray0)
        cSVFormat0 = cSVFormat_Builder1.build()
        cSVPrinter0 = cSVFormat0.printer()
        self.assertIsNotNone(cSVPrinter0)

    def test36(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        character0 = "%"
        cSVFormat_Builder0.setCommentMarker1(character0)
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVPrinter0 = cSVFormat0.printer()
        object0 = object()
        cSVPrinter0.print(object0)
        cSVPrinter0.printComment("RFC4180")

    def test35(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker0("a")
        cSVFormat0 = cSVFormat_Builder1.build()
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.printComment("T\n")

    def test34(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder0.setCommentMarker0("d")
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.printComment("\r`")

    def test33(self) -> None:
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder0.setCommentMarker0("Z")
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.printComment("\r\n")

    def test32(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        stringWriter0 = io.StringIO(new_line="\r\n")
        stringBuffer0 = stringWriter0.getvalue()
        cSVPrinter0 = cSVFormat0.print0(stringBuffer0)
        priorityQueue0 = PriorityQueue()
        objectArray0 = [None] * 8
        objectArray0[4] = priorityQueue0
        cSVPrinter0.printRecords1(objectArray0)
        self.assertEqual("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n", stringBuffer0)
        self.assertEqual("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n", stringWriter0.getvalue())

    def test31(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_TSV
        pipedOutputStream0 = io.BytesIO()
        outputStreamWriter0 = io.TextIOWrapper(pipedOutputStream0)
        cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0)
        cSVPrinter0.println()

    def test30(self) -> None:

        csv_format = CSVFormat.INFORMIX_UNLOAD
        piped_output_stream = io.BytesIO()
        output_stream_writer = io.TextIOWrapper(piped_output_stream)
        csv_printer = csv_format.print0(output_stream_writer)
        object_array = [None] * 7
        csv_printer.printRecord1(object_array)
        self.assertEqual(7, len(object_array))

    def test29(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder0.setAutoFlush(True)
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.close1(False)

    def test28(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        cSVPrinter0 = cSVFormat0.printer()
        cSVPrinter0.flush()

    def test27(self) -> None:

        csv_format0 = CSVFormat.RFC4180
        csv_printer0 = csv_format0.printer()
        csv_printer0.printComment("")

    def test26(self) -> None:

        csv_format = CSVFormat.TDF
        csv_printer = csv_format.printer()
        csv_printer.printComment(None)

    def test25(self) -> None:

        stringWriter0 = io.StringIO()
        cSVFormat0 = CSVFormat.EXCEL
        cSVPrinter0 = CSVPrinter(stringWriter0, cSVFormat0)
        linkOptionArray0 = [LinkOption.NOFOLLOW_LINKS] * 6
        list0 = list(linkOptionArray0)
        cSVPrinter0.printRecord0(list0)
        self.assertEqual(6, len(list0))

    def test23(self) -> None:

        csv_format = CSVFormat.EXCEL
        csv_format_builder = CSVFormat.Builder.create0()
        character = "u"
        csv_format_builder = csv_format_builder.setCommentMarker1(character)
        object_array = [None] * 17
        object_array[13] = csv_format
        csv_format_builder.setHeaderComments0(object_array)
        csv_format = csv_format_builder.build()
        piped_writer = io.PipedWriter()
        csv_printer = None
        try:
            csv_printer = CSVPrinter(piped_writer, csv_format)
            self.fail("Expecting exception: IOException")

        except Exception as e:
            # Pipe not connected
            self.verifyException("java.io.PipedWriter", e)

    def test22(self) -> None:

        csv_format = CSVFormat.MONGODB_TSV
        csv_printer = None

        try:
            csv_printer = CSVPrinter(None, csv_format)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "Appendable is not set")

    def test21(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        character = "a"
        csv_format_builder = CSVFormat.Builder.create0()
        csv_format_builder = csv_format_builder.setCommentMarker1(character)
        object_array = [None, csv_format]
        csv_format_builder = csv_format_builder.setHeaderComments0(object_array)
        csv_format = csv_format_builder.build()
        char_array = ["\0"] * 7
        char_buffer = CharBuffer(char_array)
        csv_printer = None
        try:
            csv_printer = CSVPrinter(char_buffer, csv_format)
            self.fail("Expecting exception: BufferOverflowException")

        except BufferOverflowException as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("java.nio.Buffer", e)

    def test20(self) -> None:

        csv_format = CSVFormat.MYSQL
        mock_file_writer = MockFileWriter("format")
        csv_printer = csv_format.print0(mock_file_writer)
        csv_printer.close1(True)
        try:
            csv_printer.close()
            self.fail("Expecting exception: IOException")

        except IOError:
            pass

    def test19(self) -> None:

        csv_format = CSVFormat.MONGODB_TSV
        piped_output_stream = io.BytesIO()
        output_stream_writer = io.TextIOWrapper(piped_output_stream)
        csv_printer = csv_format.print0(output_stream_writer)
        output_stream_writer.write("1")
        try:
            csv_printer.close0()
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedOutputStream", e)

    def test17(self) -> None:

        csv_format = CSVFormat.INFORMIX_UNLOAD_CSV
        piped_output_stream = io.BytesIO()
        output_stream_writer = io.TextIOWrapper(piped_output_stream)
        csv_printer = csv_format.print0(output_stream_writer)
        csv_printer.close0()
        try:
            csv_printer.flush()
            self.fail("Expecting exception: IOException")

        except io.UnsupportedOperation as e:
            pass

    def test16(self) -> None:

        csv_format0 = CSVFormat.INFORMIX_UNLOAD_CSV
        piped_output_stream0 = io.BytesIO()
        output_stream_writer0 = io.TextIOWrapper(piped_output_stream0)
        csv_printer0 = csv_format0.print0(output_stream_writer0)
        output_stream_writer0.close()
        piped_input_stream0 = io.BytesIO(b"\0" * 101)
        try:
            csv_printer0.print(piped_input_stream0)
            self.fail("Expecting exception: IOException")

        except IOError:
            pass

    def test15(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        character0 = "b"
        cSVFormat_Builder0.setCommentMarker1(character0)
        cSVFormat0 = cSVFormat_Builder0.build()
        pipedWriter0 = io.StringIO()
        cSVPrinter0 = cSVFormat0.print0(pipedWriter0)
        try:
            cSVPrinter0.printComment(",Zt[8] x5W'eE3}")
            self.fail("Expecting exception: IOException")

        except Exception as e:
            # Pipe not connected
            self.verifyException("java.io.PipedWriter", e)

    def test14(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker0("]")
        cSVFormat0 = cSVFormat_Builder1.build()
        charArray0 = ["\0"] * 6
        charBuffer0 = CharBuffer.wrap(charArray0)
        cSVPrinter0 = cSVFormat0.print0(charBuffer0)
        # Undeclared exception in Java code
        try:
            cSVPrinter0.printComment("format")
            self.fail("Expecting exception: BufferOverflowException")

        except BufferOverflowException as e:
            #
            # no message in exception (getMessage() returned null)
            #
            self.verifyException("java.nio.Buffer", e)

    def test13(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        pipedReader0 = io.PipedReader()
        cSVParser0 = cSVFormat0.parse(pipedReader0)
        cSVPrinter0 = cSVFormat0.printer()

        try:
            cSVPrinter0.printRecord0(cSVParser0)
            self.fail("Expecting exception: UncheckedIOException")

        except UnicodeError as e:
            self.verifyException(
                "org.apache.commons.csv.CSVParser$CSVRecordIterator", e
            )

    def test12(self) -> None:

        csv_format = CSVFormat.RFC4180
        csv_printer = csv_format.printer()

        try:
            csv_printer.printRecord0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.CSVPrinter", e)

    def test11(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD
        pipedOutputStream0 = io.BytesIO()
        outputStreamWriter0 = io.TextIOWrapper(pipedOutputStream0)
        cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0)
        cSVPrinter0.close1(False)
        objectArray0 = [None] * 7
        try:
            cSVPrinter0.printRecord1(objectArray0)
            self.fail("Expecting exception: IOException")

        except IOError:
            pass

    def test10(self) -> None:

        cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV
        cSVPrinter0 = cSVFormat0.printer()

        try:
            cSVPrinter0.printRecord1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("java.util.Objects", e)

    def test09(self) -> None:

        cSVFormat0 = CSVFormat.ORACLE
        objectArray0 = [None] * 4
        charBuffer0 = io.StringIO()
        cSVPrinter0 = CSVPrinter(charBuffer0, cSVFormat0)

        with pytest.raises(BufferError):
            cSVPrinter0.printRecord1(objectArray0)
            self.fail("Expecting exception: BufferOverflowException")

        verifyException("java.nio.CharBuffer", BufferError)

    def test08(self) -> None:

        csv_format0 = CSVFormat.ORACLE
        csv_printer0 = csv_format0.printer()
        input_stream_array0 = [None] * 2
        byte_array0 = bytearray(5)
        byte_array_input_stream0 = io.BytesIO(byte_array0[44:54])
        sequence_input_stream0 = io.SequenceIO(
            byte_array_input_stream0, byte_array_input_stream0
        )
        input_stream_array0[0] = sequence_input_stream0
        stream0 = iter(input_stream_array0)
        stream1 = sorted(stream0)

        with pytest.raises(TypeError) as e:
            csv_printer0.printRecord2(stream1)

        assert str(e.value) == "object of type 'SequenceIO' has no len()"

    def test07(self) -> None:

        cSVFormat0 = CSVFormat.TDF
        cSVPrinter0 = cSVFormat0.printer()

        try:
            cSVPrinter0.printRecord2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.CSVPrinter", e)

    def test06(self) -> None:

        csv_format0 = CSVFormat.DEFAULT
        csv_printer0 = csv_format0.printer()

        try:
            csv_printer0.printRecords0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.csv.CSVPrinter", e)

    def test05(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        pipedWriter0 = io.StringIO()
        cSVPrinter0 = cSVFormat0.print0(pipedWriter0)
        objectArray0 = [None] * 8
        try:
            cSVPrinter0.printRecords1(objectArray0)
            self.fail("Expecting exception: IOException")

        except IOError as e:
            # Pipe not connected
            self.verifyException("java.io.PipedWriter", e)

    def test04(self) -> None:

        csv_format = CSVFormat.DEFAULT
        csv_printer = csv_format.printer()

        try:
            csv_printer.printRecords1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("java.util.Objects", e)

    def test03(self) -> None:

        csv_format = CSVFormat.EXCEL
        object_array = [None] * 17
        char_array = [None] * 3
        char_buffer = CharBuffer(char_array)
        csv_printer = csv_format.print0(char_buffer)

        try:
            csv_printer.printRecords1(object_array)
            self.fail("Expecting exception: BufferOverflowException")

        except BufferOverflowException as e:
            verifyException("java.nio.CharBuffer", e)

    def test02(self) -> None:

        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        charArray0 = ["\0"] * 7
        charBuffer0 = CharBuffer(charArray0)
        charBuffer1 = CharBuffer(charBuffer0, 0, 0)
        cSVPrinter0 = CSVPrinter(charBuffer1, cSVFormat0)
        objectArray0 = [None] * 1

        try:
            cSVPrinter0.printRecords1(objectArray0)
            self.fail("Expecting exception: ReadOnlyBufferException")

        except ReadOnlyBufferException as e:
            self.verifyException("java.nio.CharBuffer", e)

    def test01(self) -> None:

        charArray0 = [""] * 2
        charBuffer0 = io.StringIO("".join(charArray0))
        charBuffer0.write("N")
        cSVFormat0 = CSVFormat.TDF
        cSVPrinter0 = CSVPrinter(charBuffer0, cSVFormat0)

        with self.assertRaises(BufferError) as context:
            cSVPrinter0.println()

        self.assertTrue("BufferOverflowException" in str(context.exception))

    def test00(self) -> None:

        csv_format0 = CSVFormat.ORACLE
        csv_printer0 = csv_format0.printer()
        input_stream_array0 = [None, None]
        stream0 = iter(input_stream_array0)
        csv_printer0.printRecord2(stream0)
