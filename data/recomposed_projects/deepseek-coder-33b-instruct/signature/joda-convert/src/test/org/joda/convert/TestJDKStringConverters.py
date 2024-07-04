from __future__ import annotations
import time
import re
import uuid
import os
import datetime
import decimal
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.JDKStringConverter import *
from src.main.org.joda.convert.RenameHandler import *
from src.test.org.joda.convert.Status import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.TypedStringConverter import *


class TestJDKStringConverters(unittest.TestCase):

    def test_Enum_withRename(self) -> None:

        test = StringConvert.create().findTypedConverter(Status)
        self.assertEqual("VALID", test.convertToString(Status.VALID))
        self.assertEqual("INVALID", test.convertToString(Status.INVALID))
        self.assertEqual(Status.VALID, test.convertFromString(Status, "VALID"))
        self.assertEqual(Status.INVALID, test.convertFromString(Status, "INVALID"))
        with self.assertRaises(RuntimeError):
            test.convertFromString(Status, "OK")
        RenameHandler.INSTANCE.renamedEnum("OK", Status.VALID)
        self.assertEqual(Status.VALID, test.convertFromString(Status, "OK"))
        self.assertEqual(Status.VALID, test.convertFromString(Status, "VALID"))
        self.assertEqual(Status.INVALID, test.convertFromString(Status, "INVALID"))

    def test_Enum_invalidConstant(self) -> None:

        # Create a StringConvert instance
        test = StringConvert.create().findTypedConverter(RoundingMode)

        # Expect a RuntimeError to be raised when converting an invalid string
        with pytest.raises(RuntimeError):
            test.convertFromString(RoundingMode, "RUBBISH")

    def test_Enum(self) -> None:

        test = StringConvert.create().findTypedConverter(RoundingMode)
        self.assertEqual(RoundingMode, test.getEffectiveType())
        self.assertEqual("CEILING", test.convertToString(RoundingMode.CEILING))
        self.assertEqual(
            RoundingMode.CEILING, test.convertFromString(RoundingMode, "CEILING")
        )

    def test_Calendar_notGregorian(self) -> None:

        class Calendar:
            def roll(self, field: int, up: bool) -> None:
                pass

            def getMinimum(self, field: int) -> int:
                return 0

            def getMaximum(self, field: int) -> int:
                return 0

            def getLeastMaximum(self, field: int) -> int:
                return 0

            def getGreatestMinimum(self, field: int) -> int:
                return 0

            def computeTime(self) -> None:
                pass

            def computeFields(self) -> None:
                pass

            def add(self, field: int, amount: int) -> None:
                pass

        with pytest.raises(RuntimeError):
            JDKStringConverter.CALENDAR.convertToString(Calendar())

    def test_Calendar_invalidFormat(self) -> None:

        with pytest.raises(RuntimeError):
            JDKStringConverter.CALENDAR.convertFromString(
                GregorianCalendar, "2010-09-03XXX:34:05.000+02:00[Europe/London]"
            )

    def test_Calendar_invalidLength(self) -> None:

        with pytest.raises(RuntimeError):
            JDKStringConverter.CALENDAR.convertFromString(
                GregorianCalendar, "2010-09-03"
            )

    def test_Calendar(self) -> None:

        test = JDKStringConverter.CALENDAR

        cal = GregorianCalendar(TimeZone.getTimeZone("Europe/Paris"))
        cal.set(2010, 9 - 1, 3, 12, 34, 5)
        cal.set(Calendar.MILLISECOND, 0)
        self.doTest0(test, Calendar, cal, "2010-09-03T12:34:05.000+02:00[Europe/Paris]")

        cal2 = GregorianCalendar(TimeZone.getTimeZone("Europe/Paris"))
        cal2.set(2011, 1 - 1, 4, 12, 34, 5)
        cal2.set(Calendar.MILLISECOND, 0)
        self.doTest0(
            test, Calendar, cal2, "2011-01-04T12:34:05.000+01:00[Europe/Paris]"
        )

    def test_Date_invalidFormat(self) -> None:

        with pytest.raises(RuntimeError):
            JDKStringConverter.DATE.convertFromString(
                Date, "2010-09-03XXX:34:05.000+02:00"
            )

    def test_Date_invalidLength(self) -> None:

        with pytest.raises(RuntimeError):
            JDKStringConverter.DATE.convertFromString(Date, "2010-09-03")

    def test_Date(self) -> None:

        zone = time.tzset()
        try:
            time.tzset("Europe/Paris")
            test = JDKStringConverter.DATE
            self.doTest0(
                test,
                datetime.date,
                datetime.date(2010, 9, 3),
                "2010-09-03T12:34:05.000+02:00",
            )
            self.doTest0(
                test,
                datetime.date,
                datetime.date(2011, 1, 4),
                "2011-01-04T12:34:05.000+01:00",
            )
        finally:
            time.tzset(zone)

    def test_File(self) -> None:

        test = JDKStringConverter.FILE
        file = File("/path/to/file")
        self.doTest0(test, File, file, str(file))

    def test_InetAddress(self) -> None:

        from socket import gethostbyname
        from ipaddress import ip_address

        test = JDKStringConverter.INET_ADDRESS
        self.doTest0(test, ip_address, ip_address("1.2.3.4"), "1.2.3.4")

        obj = ip_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        str = test.convertToString(obj)
        self.assertTrue(
            str == "2001:db8:85a3:0:0:8a2e:370:7334"
            or str == "2001:db8:85a3::8a2e:370:7334"
        )
        self.assertEqual(obj, test.convertFromString(ip_address, str))
        self.assertEqual(
            obj, test.convertFromString(ip_address, "2001:db8:85a3:0:0:8a2e:370:7334")
        )
        self.assertEqual(
            obj, test.convertFromString(ip_address, "2001:db8:85a3::8a2e:370:7334")
        )

    def test_URI(self) -> None:

        test = JDKStringConverter.URI
        self.doTest0(
            test,
            URI,
            URI.create("http://localhost:8080/my/test"),
            "http://localhost:8080/my/test",
        )
        self.doTest0(test, URI, URI.create("/my/test"), "/my/test")
        self.doTest0(test, URI, URI.create("/my/../test"), "/my/../test")
        self.doTest0(test, URI, URI.create("urn:hello"), "urn:hello")

    def test_URL_invalidFormat(self) -> None:

        pass  # LLM could not translate this method

    def test_URL(self) -> None:

        test = JDKStringConverter.URL
        self.doTest0(
            test,
            URL,
            URL("http://localhost:8080/my/test"),
            "http://localhost:8080/my/test",
        )
        self.doTest0(test, URL, URL(None, "ftp:world"), "ftp:world")

    def test_UUID(self) -> None:

        test = JDKStringConverter.UUID
        uuid = uuid.uuid4()
        self.doTest0(test, uuid.UUID, uuid, str(uuid))

    def test_TimeZone(self) -> None:

        test = JDKStringConverter.TIME_ZONE
        self.doTest0(
            test, TimeZone, TimeZone.getTimeZone("Europe/London"), "Europe/London"
        )
        self.doTest0(
            test, TimeZone, TimeZone.getTimeZone("America/New_York"), "America/New_York"
        )

    def test_Currency(self) -> None:

        test = JDKStringConverter.CURRENCY
        self.doTest0(test, Currency, Currency.getInstance("GBP"), "GBP")
        self.doTest0(test, Currency, Currency.getInstance("USD"), "USD")

    def test_Package(self) -> None:

        pass  # LLM could not translate this method

    def test_Class_withRename(self) -> None:

        try:
            JDKStringConverter.CLASS.convertFromString(Class, "org.foo.StringConvert")
            self.fail()
        except RuntimeError:
            pass

        RenameHandler.INSTANCE.renamedType("org.foo.StringConvert", StringConvert)

        self.assertEqual(
            StringConvert,
            JDKStringConverter.CLASS.convertFromString(Class, "org.foo.StringConvert"),
        )

    def test_Class_fail(self) -> None:
        with pytest.raises(RuntimeError):
            JDKStringConverter.CLASS.convertFromString(Class, "RUBBISH")

    def test_Class_array(self) -> None:

        pass  # LLM could not translate this method

    def test_Class_primitive(self) -> None:

        test = JDKStringConverter.CLASS

        self.doTest0(test, Class, byte, "byte")
        self.doTest0(test, Class, short, "short")
        self.doTest0(test, Class, int, "int")
        self.doTest0(test, Class, long, "long")
        self.doTest0(test, Class, float, "float")
        self.doTest0(test, Class, double, "double")
        self.doTest0(test, Class, bool, "boolean")
        self.doTest0(test, Class, str, "char")
        self.doTest0(test, Class, None, "void")

    def test_Class(self) -> None:

        test = JDKStringConverter.CLASS
        self.doTest0(test, Class, Locale, "java.util.Locale")
        self.doTest0(test, Class, FromString, "org.joda.convert.FromString")

    def test_Locale(self) -> None:

        test = JDKStringConverter.LOCALE
        self.doTest0(test, Locale, Locale("en"), "en")
        self.doTest0(test, Locale, Locale("en", "GB"), "en_GB")
        self.doTest0(test, Locale, Locale("en", "GB", "VARIANT_B"), "en_GB_VARIANT_B")

    def test_AtomicBoolean_fail(self) -> None:

        with pytest.raises(ValueError):
            JDKStringConverter.ATOMIC_BOOLEAN.convertFromString(
                AtomicBoolean, "RUBBISH"
            )

    def test_AtomicBoolean_false(self) -> None:

        test = JDKStringConverter.ATOMIC_BOOLEAN
        obj = AtomicBoolean(False)
        self.assertEqual(AtomicBoolean, type(test.getType()))
        self.assertEqual("false", test.convertToString(obj))
        back = test.convertFromString(AtomicBoolean, "false")
        self.assertEqual(False, back.get())

    def test_AtomicBoolean_true(self) -> None:

        test = JDKStringConverter.ATOMIC_BOOLEAN
        obj = AtomicBoolean(True)
        self.assertEqual(AtomicBoolean, test.getType())
        self.assertEqual("true", test.convertToString(obj))
        back = test.convertFromString(AtomicBoolean, "true")
        self.assertEqual(True, back.get())

    def test_AtomicInteger(self) -> None:

        test = JDKStringConverter.ATOMIC_INTEGER
        obj = AtomicInteger(12)
        self.assertEqual(AtomicInteger, test.getType())
        self.assertEqual("12", test.convertToString(obj))
        back = test.convertFromString(AtomicInteger, "12")
        self.assertEqual(12, back.get())

    def test_AtomicLong(self) -> None:

        test = JDKStringConverter.ATOMIC_LONG
        obj = AtomicLong(12)
        self.assertEqual(AtomicLong, test.getType())
        self.assertEqual("12", test.convertToString(obj))
        back = test.convertFromString(AtomicLong, "12")
        self.assertEqual(12, back.get())

    def test_BigDecimal(self) -> None:

        from decimal import Decimal

        test = JDKStringConverter.BIG_DECIMAL
        self.doTest0(test, Decimal, Decimal("12.23"), "12.23")

    def test_BigInteger(self) -> None:

        from java.math import BigInteger

        test = JDKStringConverter.BIG_INTEGER
        self.doTest0(test, BigInteger, BigInteger.valueOf(12), "12")

    def test_Float(self) -> None:

        test = JDKStringConverter.FLOAT
        self.doTest0(test, float, 12.2, "12.2")

    def test_Double(self) -> None:

        test = JDKStringConverter.DOUBLE
        self.doTest0(test, float, 12.4, "12.4")

    def test_Boolean_fail(self) -> None:

        with pytest.raises(ValueError):
            JDKStringConverter.BOOLEAN.convertFromString(Boolean, "RUBBISH")

    def test_Boolean(self) -> None:

        test = JDKStringConverter.BOOLEAN
        self.doTest0(test, bool, True, "true")
        self.doTest0(test, bool, False, "false")

    def test_byteArray4(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([73, 97, 112, 77])
        str = "SWFwTQ=="
        self.assertEqual(bytearray, type(test.getType()))
        self.assertEqual(str, test.convertToString(array))
        self.assertTrue(array == bytearray(test.convertFromString(bytearray, str)))

    def test_byteArray3(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77])
        str = "TQ=="
        self.assertEqual(bytearray, type(test.getType()))
        self.assertEqual(str, test.convertToString(array))
        self.assertTrue(array == bytearray(test.convertFromString(bytearray, str)))

    def test_byteArray2(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77, 97])
        str = "TWE="
        self.assertEqual(bytearray, type(test.getType()))
        self.assertEqual(str, test.convertToString(array))
        self.assertTrue(array == bytearray(test.convertFromString(bytearray, str)))

    def test_byteArray1(self) -> None:

        test = JDKStringConverter.BYTE_ARRAY
        array = bytearray([77, 97, 112])
        str = "TWFw"
        self.assertEqual(bytearray, type(test.getType()))
        self.assertEqual(str, test.convertToString(array))
        self.assertTrue(array == bytearray(test.convertFromString(bytearray, str)))

    def test_Byte(self) -> None:

        test = JDKStringConverter.BYTE
        self.doTest0(test, Byte, Byte(12), "12")

    def test_charArray(self) -> None:

        test = JDKStringConverter.CHAR_ARRAY
        array = ["M", "a", "p"]
        str = "Map"
        self.assertEqual(list, type(test.getType()))
        self.assertEqual(str, test.convertToString(array))
        self.assertTrue(array == test.convertFromString(list, str))

    def test_Character_fail(self) -> None:

        with pytest.raises(ValueError):
            JDKStringConverter.CHARACTER.convertFromString(Character, "RUBBISH")

    def test_Character(self) -> None:

        test = JDKStringConverter.CHARACTER
        self.doTest0(test, Character, Character.valueOf("a"), "a")
        self.doTest0(test, Character, Character.valueOf("z"), "z")

    def test_Short(self) -> None:

        test = JDKStringConverter.SHORT
        self.doTest0(test, Short, Short.valueOf(12), "12")

    def test_Int(self) -> None:

        test = JDKStringConverter.INTEGER
        self.doTest0(test, int, 12, "12")

    def test_Long(self) -> None:

        test = JDKStringConverter.LONG
        self.doTest0(test, Long, Long.valueOf(12), "12")

    def test_CharSequence(self) -> None:

        test = JDKStringConverter.CHAR_SEQUENCE
        self.doTest0(test, CharSequence, "Hello", "Hello")
        self.doTest1(test, CharSequence, StringBuffer("Hello"), "Hello", "Hello")
        self.doTest1(test, CharSequence, StringBuilder("Hello"), "Hello", "Hello")

    def test_StringBuilder(self) -> None:

        test = JDKStringConverter.STRING_BUILDER
        obj = StringBuilder("Hello")
        self.assertEqual(StringBuilder, test.getType())
        self.assertEqual("Hello", test.convertToString(obj))
        back = test.convertFromString(StringBuilder, "Hello")
        self.assertEqual("Hello", back.toString())

    def test_StringBuffer(self) -> None:

        test = JDKStringConverter.STRING_BUFFER
        obj = io.StringIO("Hello")
        self.assertEqual(io.StringIO, type(test.getType()))
        self.assertEqual("Hello", test.convertToString(obj))
        back = test.convertFromString(io.StringIO, "Hello")
        self.assertEqual("Hello", back.getvalue())

    def test_String(self) -> None:

        test = JDKStringConverter.STRING
        self.doTest0(test, str, "Hello", "Hello")

    def doTest1(
        self,
        test: JDKStringConverter,
        cls: typing.Type[typing.Any],
        obj: typing.Any,
        str: str,
        objFromStr: typing.Any,
    ) -> None:

        self.assertEqual(cls, test.getType())
        self.assertEqual(str, test.convertToString(obj))
        self.assertEqual(objFromStr, test.convertFromString(cls, str))

    def doTest0(
        self,
        test: JDKStringConverter,
        cls: typing.Type[typing.Any],
        obj: typing.Any,
        str: str,
    ) -> None:
        self.doTest1(test, cls, obj, str, obj)
