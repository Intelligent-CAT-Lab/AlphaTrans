from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import numbers
from io import StringIO
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *

# from src.test.org.apache.commons.csv.CSVRecord_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CSVRecord_ESTest(unittest.TestCase):

    def test37(self) -> None:

        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        cSVParser0 = CSVParser.parse4("format", cSVFormat0)
        cSVRecord0 = cSVParser0.nextRecord()
        cSVRecord0.getComment()
        self.assertEqual(1, cSVRecord0.size())
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test36(self) -> None:

        cSVFormat0 = CSVFormat.POSTGRESQL_TEXT
        cSVParser0 = CSVParser.parse4("format", cSVFormat0)
        cSVRecord0 = cSVParser0.nextRecord()
        long0 = cSVRecord0.getCharacterPosition()
        self.assertEqual(0, long0)
        self.assertEqual(1, cSVRecord0.size())
        self.assertEqual(1, cSVRecord0.getRecordNumber())

    def test35(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", csv_format
        )
        string_array = [""] * 4
        csv_record = CSVRecord(csv_parser, string_array, ")", 0, 0)
        csv_record.toMap()
        self.assertEqual(4, csv_record.size())

    def test34(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        cSVParser0 = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        string0 = cSVRecord0.toString()
        self.assertEqual(
            "CSVRecord [comment='null', recordNumber=1, values=[) invalid char between encapsulated token and delimiter]]",
            string0,
        )
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test33(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        cSVParser0 = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()

        try:
            cSVRecord0.get1(102)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException("org.apache.commons.csv.CSVRecord", e)

    def test32(self) -> None:

        stringArray0 = [""] * 5
        cSVRecord0 = CSVRecord(None, stringArray0, "W2T^[eSjIU8K@~kn", -2665, -2665)
        stringArray1 = cSVRecord0.values()
        self.assertEqual(5, len(stringArray1))
        self.assertEqual(-2665, cSVRecord0.getCharacterPosition())
        self.assertEqual(-2665, cSVRecord0.getRecordNumber())

    def test31(self) -> None:

        cSVFormat0 = CSVFormat.RFC4180
        cSVParser0 = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        cSVRecord0.getParser()
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())
        self.assertEqual(1, cSVRecord0.size())

    def test30(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", csv_format
        )
        string_array = [""] * 4
        csv_record = CSVRecord(csv_parser, string_array, ")", 0, 0)
        record_number = csv_record.getRecordNumber()
        self.assertEqual(4, csv_record.size())

    def test29(self) -> None:

        cSVFormat0 = CSVFormat.DEFAULT
        cSVParser0 = CSVParser.parse4(
            "The comment start marker character cannot be a line break", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        int0 = cSVRecord0.size()
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(1, int0)
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test28(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4('"6^', csv_format)
        csv_record = CSVRecord(csv_parser, None, "", 1083, 1083)
        csv_record.getComment()
        self.assertEqual(1083, csv_record.getCharacterPosition())
        self.assertEqual(1083, csv_record.getRecordNumber())

    def test27(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", csv_format
        )
        string_array = [""] * 4
        csv_record = CSVRecord(csv_parser, string_array, ")", 0, 0)

        try:
            csv_record.get2(")1&DZC?O)FpC")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.csv.CSVRecord", e)

    def test26(self) -> None:

        stringArray0 = [None] * 9
        cSVRecord0 = CSVRecord(None, stringArray0, "$VALUES", 0, 0)
        boolean0 = cSVRecord0.isSet1("$VALUES")
        self.assertEqual(9, cSVRecord0.size())
        self.assertFalse(boolean0)

    def test25(self) -> None:

        stringReader0 = io.StringIO("cs,t/kCu")
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVParser0 = CSVParser(stringReader0, cSVFormat0, 1658, 1658)
        cSVRecord0 = cSVParser0.nextRecord()
        boolean0 = cSVRecord0.hasComment()
        self.assertFalse(boolean0)
        self.assertEqual(1658, cSVRecord0.getCharacterPosition())
        self.assertEqual(1658, cSVRecord0.getRecordNumber())
        self.assertEqual(2, cSVRecord0.size())

    def test24(self) -> None:

        stringArray0 = [""] * 13
        cSVRecord0 = CSVRecord(None, stringArray0, "", -460, -460)
        boolean0 = cSVRecord0.hasComment()
        self.assertTrue(boolean0)
        self.assertEqual(-460, cSVRecord0.getRecordNumber())
        self.assertEqual(-460, cSVRecord0.getCharacterPosition())
        self.assertEqual(13, cSVRecord0.size())

    def test23(self) -> None:

        cSVFormat0 = CSVFormat.DEFAULT
        cSVParser0 = CSVParser.parse4(
            "The comment start marker character cannot be a line break", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        boolean0 = cSVRecord0.isConsistent()
        self.assertTrue(boolean0)
        self.assertEqual(1, cSVRecord0.size())
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test22(self) -> None:

        csv_format = CSVFormat.DEFAULT
        csv_parser = CSVParser.parse4("f-", csv_format)
        csv_record = csv_parser.nextRecord()
        boolean0 = csv_record.isSet0(-1265)
        self.assertFalse(boolean0)
        self.assertEqual(1, csv_record.size())
        self.assertEqual(0, csv_record.getCharacterPosition())
        self.assertEqual(1, csv_record.getRecordNumber())

    def test21(self) -> None:

        cSVFormat0 = CSVFormat.DEFAULT
        cSVParser0 = CSVParser.parse4(
            "The comment start marker character cannot be a line break", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        boolean0 = cSVRecord0.isSet0(2)
        self.assertEqual(0, cSVRecord0.getCharacterPosition())
        self.assertFalse(boolean0)
        self.assertEqual(1, cSVRecord0.size())
        self.assertEqual(1, cSVRecord0.getRecordNumber())

    def test20(self) -> None:

        cSVFormat0 = CSVFormat.RFC4180
        cSVParser0 = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        boolean0 = cSVRecord0.isSet0(0)
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())
        self.assertTrue(boolean0)

    def test19(self) -> None:

        csv_record0 = CSVRecord(None, None, "", 0, 0)
        list0 = csv_record0.toList()
        self.assertEqual(len(list0), 0)

    def test18(self) -> None:

        stringArray0 = [None] * 9
        cSVRecord0 = CSVRecord(None, stringArray0, "$VALUES", -448, -448)
        cSVRecord0.stream()
        self.assertEqual(-448, cSVRecord0.getCharacterPosition())
        self.assertEqual(-448, cSVRecord0.getRecordNumber())

    def test17(self) -> None:

        csv_format = CSVFormat.POSTGRESQL_TEXT
        csv_parser = CSVParser.parse4('"6^', csv_format)
        csv_record = CSVRecord(csv_parser, None, "", 0, 0)
        boolean_result = csv_record.isMapped("")
        self.assertFalse(boolean_result)

    def test16(self) -> None:

        stringReader0 = io.StringIO("cs,t/kCu")
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVParser0 = CSVParser(stringReader0, cSVFormat0, 1658, 1658)
        cSVRecord0 = cSVParser0.nextRecord()
        cSVRecord0.putIn(None)
        self.assertEqual(1658, cSVRecord0.getRecordNumber())
        self.assertEqual(1658, cSVRecord0.getCharacterPosition())

    def test15(self) -> None:

        stringArray0 = [""] * 2
        stringArray0[0] = ""
        stringArray0[1] = ""
        path0 = Path.of("", stringArray0)
        charset0 = Charset.defaultCharset()
        cSVFormat0 = CSVFormat.MONGODB_TSV
        cSVParser0 = CSVParser.parse2(path0, charset0, cSVFormat0)
        cSVRecord0 = CSVRecord(cSVParser0, stringArray0, "", (-1), (-1))
        cSVRecord0.get1(0)
        self.assertEqual((-1), cSVRecord0.getRecordNumber())
        self.assertEqual((-1), cSVRecord0.getCharacterPosition())

    def test14(self) -> None:

        csv_format = CSVFormat.MONGODB_CSV
        string_reader = io.StringIO("'(j,S=d65E5LngZpK")
        csv_parser = csv_format.parse(string_reader)
        string_array = ["'(j,S=d65E5LngZpK"]
        csv_record = CSVRecord(csv_parser, string_array, "'(j,S=d65E5LngZpK", 0, 0)
        string = csv_record.get1(0)
        self.assertEqual("'(j,S=d65E5LngZpK", string)

    def test13(self) -> None:

        stringArray0 = [""] * 5
        cSVRecord0 = CSVRecord(None, stringArray0, "W2T^[eSjIU8K@~kn", -2665, -2665)
        long0 = cSVRecord0.getCharacterPosition()
        self.assertEqual(-2665, long0)
        self.assertEqual(-2665, cSVRecord0.getRecordNumber())

    def test12(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        cSVParser0 = CSVParser.parse4("", cSVFormat0)
        stringArray0 = [""] * 2
        cSVRecord0 = CSVRecord(
            cSVParser0,
            stringArray0,
            "Index for header '%s' is %d but CSVRecord only has %d values!"
            % ("", 2027, 2027),
            2027,
            2027,
        )
        long0 = cSVRecord0.getCharacterPosition()
        self.assertEqual(2027, cSVRecord0.getRecordNumber())
        self.assertEqual(2027, long0)

    def test11(self) -> None:

        stringArray0 = [None] * 9
        cSVRecord0 = CSVRecord(None, stringArray0, "$VALUES", -448, -448)
        cSVRecord0.getComment()
        self.assertEqual(-448, cSVRecord0.getRecordNumber())
        self.assertEqual(-448, cSVRecord0.getCharacterPosition())

    def test10(self) -> None:

        csv_format = CSVFormat.MYSQL
        csv_parser = CSVParser.parse4("", csv_format)
        string_array = [""] * 5
        csv_record = CSVRecord(csv_parser, string_array, None, -822, 0)
        csv_record.getParser()
        self.assertEqual(0, csv_record.getCharacterPosition())
        self.assertEqual(-822, csv_record.getRecordNumber())

    def test09(self) -> None:

        stringArray0 = [""] * 4
        cSVRecord0 = CSVRecord(
            None,
            stringArray0,
            "Index for header '%s' is %d but CSVRecord only has %d values",
            2027,
            2027,
        )
        self.assertIsNone(cSVRecord0.getParser())
        self.assertEqual(2027, cSVRecord0.getCharacterPosition())
        self.assertEqual(2027, cSVRecord0.getRecordNumber())

    def test08(self) -> None:

        stringReader0 = io.StringIO("cs,t/kCu")
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVParser0 = CSVParser(stringReader0, cSVFormat0, 1, -2748)
        cSVRecord0 = cSVParser0.nextRecord()
        long0 = cSVRecord0.getRecordNumber()
        self.assertEqual(1, cSVRecord0.getCharacterPosition())
        self.assertEqual(-2748, long0)

    def test07(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        cSVParser0 = CSVParser.parse4(
            ") invalid char between encapsulated token and delimiter", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        long0 = cSVRecord0.getRecordNumber()
        self.assertEqual(1, long0)
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test06(self) -> None:

        cSVFormat0 = CSVFormat.MYSQL
        cSVParser0 = CSVParser.parse4("", cSVFormat0)
        stringArray0 = [""] * 2
        cSVRecord0 = CSVRecord(
            cSVParser0,
            stringArray0,
            "Index for header '%s' is %d but CSVRecord only has %d values!"
            % ("", 2027, 2027),
            2027,
            2027,
        )
        cSVRecord0.iterator()
        self.assertEqual(2027, cSVRecord0.getCharacterPosition())
        self.assertEqual(2027, cSVRecord0.getRecordNumber())

    def test05(self) -> None:

        cSVFormat0 = CSVFormat.MONGODB_CSV
        stringReader0 = io.StringIO("'(j,S=d65E5LngZpK")
        cSVParser0 = cSVFormat0.parse(stringReader0)
        stringArray0 = [""]
        cSVRecord0 = CSVRecord(cSVParser0, stringArray0, "'(j,S=d65E5LngZpK", 0, 0)
        hashMap0 = {"dzxj9RRU33YH](zd8k": "'(j,S=d65E5LngZpK"}
        hashMap1 = cSVRecord0.putIn(hashMap0)
        self.assertEqual(len(hashMap1), 1)

    def test04(self) -> None:

        cSVFormat0 = CSVFormat.DEFAULT
        cSVParser0 = CSVParser.parse4(
            "The comment start marker character cannot be a line break", cSVFormat0
        )
        cSVRecord0 = cSVParser0.nextRecord()
        hashMap0 = {}
        cSVRecord0.putIn(hashMap0)
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())

    def test03(self) -> None:

        pipedReader0 = io.PipeReader(0)
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVParser0 = CSVParser(pipedReader0, cSVFormat0, 2, -2998)
        cSVRecord0 = CSVRecord(cSVParser0, None, "", -2998, 2)
        cSVRecord0.size()
        self.assertEqual(-2998, cSVRecord0.getRecordNumber())
        self.assertEqual(2, cSVRecord0.getCharacterPosition())

    def test02(self) -> None:

        cSVFormat0 = CSVFormat.RFC4180
        cSVParser0 = CSVParser.parse4("Default", cSVFormat0)
        cSVRecord0 = cSVParser0.nextRecord()
        cSVRecord0.toList()
        self.assertEqual(0, cSVRecord0.getCharacterPosition())
        self.assertEqual(1, cSVRecord0.getRecordNumber())

    def test01(self) -> None:

        pipedReader0 = io.PipedReader()
        cSVFormat_Builder0 = Builder.create0()
        cSVFormat0 = cSVFormat_Builder0.build()
        cSVParser0 = CSVParser(pipedReader0, cSVFormat0, 2, -2998)
        cSVRecord0 = CSVRecord(cSVParser0, None, "", -2998, 2)
        cSVRecord0.values()
        self.assertEqual(2, cSVRecord0.getCharacterPosition())
        self.assertEqual(-2998, cSVRecord0.getRecordNumber())

    def test00(self) -> None:

        cSVFormat0 = CSVFormat.DEFAULT
        cSVParser0 = CSVParser.parse4("', recordNumber=", cSVFormat0)
        cSVRecord0 = cSVParser0.nextRecord()
        boolean0 = cSVRecord0.isSet0(2)
        self.assertFalse(boolean0)
        self.assertEqual(1, cSVRecord0.getRecordNumber())
        self.assertEqual(0, cSVRecord0.getCharacterPosition())
