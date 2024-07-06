from __future__ import annotations
import math
import time
import inspect
import locale
import re
import mock
import os
import typing
from typing import *
import enum
import numbers
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.JDKStringConverter import *

# from src.test.org.joda.convert.JDKStringConverter_ESTest_scaffolding import *


class JDKStringConverter_ESTest(unittest.TestCase):

    def test52(self) -> None:

        jdk_string_converter0 = JDKStringConverter.DATE

        with pytest.raises(ValueError):
            jdk_string_converter0.convertToString(jdk_string_converter0)
            pytest.fail("Expecting exception: ValueError")

    def test51(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, ":")

    def test50(self) -> None:

        jdk_string_converter0 = JDKStringConverter.ATOMIC_LONG
        jdk_string_converter1 = JDKStringConverter.ATOMIC_BOOLEAN
        class0 = object
        atomic_boolean0 = jdk_string_converter1.convertFromString(class0, "true")
        jdk_string_converter0.convertToString(atomic_boolean0)
        self.assertEqual("true", atomic_boolean0.toString())
        self.assertTrue(atomic_boolean0.get())

    def test49(self) -> None:

        jDKStringConverter0 = JDKStringConverter.ATOMIC_LONG
        class0 = Date
        # Undeclared exception in Python is ValueError
        try:
            jDKStringConverter0.convertFromString(class0, "@HFM?a{brd7*|m")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # For input string: \"@HFM?a{brd7*|m\"
            self.assertEqual(str(e), "Invalid format: @HFM?a{brd7*|m")

    def test48(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BIG_DECIMAL
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "_tRA|Ld")

    def test47(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BIG_INTEGER
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "Pv+>=")
            self.fail("Expecting exception: ValueError")

        self.verifyException("java.math.BigInteger", ValueError())

    def test46(self) -> None:

        jDKStringConverter0 = JDKStringConverter.FLOAT
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "G3th")

    def test45(self) -> None:

        jDKStringConverter0 = JDKStringConverter.DOUBLE
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "m-RA|La")

    def test44(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CHAR_ARRAY
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "J3th")
        self.assertIsNotNone(object0)

    def test43(self) -> None:

        jdk_string_converter0 = JDKStringConverter.CHAR_ARRAY

        try:
            jdk_string_converter0.convertToString(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test42(self) -> None:

        jDKStringConverter0 = JDKStringConverter.ATOMIC_INTEGER
        class0 = Date
        object0 = jDKStringConverter0.convertFromString(class0, "4")
        self.assertEqual("4", str(object0))

    def test41(self) -> None:

        jdk_string_converter0 = JDKStringConverter.INET_ADDRESS
        class0 = jdk_string_converter0.getEffectiveType()

        with pytest.raises(TypeError):
            jdk_string_converter0.convertToString(class0)
            self.fail("Expecting exception: TypeError")

    def test39(self) -> None:

        jDKStringConverter0 = JDKStringConverter.URI
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "B]y4m")
            self.fail("Expecting exception: ValueError")

        self.verifyException("java.net.URI", ValueError)

    def test38(self) -> None:

        class0 = Date
        jDKStringConverter0 = JDKStringConverter.URL

        try:
            jDKStringConverter0.convertFromString(
                class0, "org.threeten.bp.LocalDateTime"
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.convert.JDKStringConverter$26", e)

    def test36(self) -> None:

        jDKStringConverter0 = JDKStringConverter.TIME_ZONE
        class0 = jDKStringConverter0.getEffectiveType()

        try:
            jDKStringConverter0.convertToString(class0)
            self.fail("Expecting exception: TypeError")

        except TypeError as e:
            self.verifyException("org.joda.convert.JDKStringConverter$24", e)

    def test35(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CURRENCY
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "RenamedTypes")

        verifyException("java.util.Currency", ValueError)

    def test34(self) -> None:

        jDKStringConverter0 = JDKStringConverter.PACKAGE
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "qqKF")
        self.assertIsNone(object0)

    def test33(self) -> None:

        jdk_string_converter0 = JDKStringConverter.PACKAGE
        mock_date0 = MockDate(
            -1846777314, -1846777314, 3962, 1, -1846777314, -1846777314
        )

        with pytest.raises(TypeError):
            jdk_string_converter0.convertToString(mock_date0)
            self.fail("Expecting exception: TypeError")

    def test32(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CALENDAR
        jDKStringConverter1 = JDKStringConverter.CLASS

        try:
            jDKStringConverter1.convertToString(jDKStringConverter0)
            self.fail("Expecting exception: TypeError")

        except TypeError as e:
            self.verifyException("org.joda.convert.JDKStringConverter$21", e)

    def test31(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CLASS
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(RuntimeError) as excinfo:
            jDKStringConverter0.convertFromString(class0, "'U'Q")

        assert str(excinfo.value) == "Unable to create type: 'U'Q"

    def test30(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CHAR_SEQUENCE
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "$S,3Mt~x-@p8MSHJB")
        self.assertEqual("$S,3Mt~x-@p8MSHJB", object0)

    def test29(self) -> None:

        jDKStringConverter0 = JDKStringConverter.STRING
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "8")
        self.assertEqual("8", object0)

    def test28(self) -> None:

        jDKStringConverter0 = JDKStringConverter.STRING_BUILDER
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "zsed^=XjU^U_}f)f")
        self.assertEqual("zsed^=XjU^U_}f)f", str(object0))

    def test27(self) -> None:

        jDKStringConverter0 = JDKStringConverter.STRING_BUFFER
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "4O@SQ")
        self.assertEqual("4O@SQ", str(object0))

    def test26(self) -> None:

        jDKStringConverter0 = JDKStringConverter.INTEGER
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, 'stfy9qdt5k"')

    def test25(self) -> None:

        jDKStringConverter0 = JDKStringConverter.LONG
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "X_ciLifUQ0o{X@")

    def test24(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BYTE
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "G3th")

    def test23(self) -> None:

        jdk_string_converter0 = JDKStringConverter.SHORT
        class0 = jdk_string_converter0.getEffectiveType()

        with pytest.raises(ValueError):
            jdk_string_converter0.convertFromString(
                class0, "javax.time.calendar.LocalDate"
            )

    def test21(self) -> None:

        class0 = Character
        jDKStringConverter0 = JDKStringConverter.CHARACTER
        object0 = jDKStringConverter0.convertFromString(class0, "B")
        self.assertEqual("B", object0)

    def test20(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CHARACTER
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "BW94x")
            self.fail("Expecting exception: ValueError")

        self.verifyException("org.joda.convert.JDKStringConverter$10", ValueError)

    def test19(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BOOLEAN
        class0 = Date
        object0 = jDKStringConverter0.convertFromString(class0, "false")
        self.assertEqual(False, object0)

    def test18(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BOOLEAN
        class0 = Date

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "6N[*v")
            self.fail("Expecting exception: ValueError")

        # verifyException("org.joda.convert.JDKStringConverter$12", e)
        # This line is commented out in the original Java code, so I'm not sure what it's supposed to do.
        # If it's a custom function, you'll need to implement it.

    def test17(self) -> None:

        jDKStringConverter0 = JDKStringConverter.valueOf("ATOMIC_BOOLEAN")
        class0 = Date
        atomicBoolean0 = jDKStringConverter0.convertFromString(class0, "false")
        self.assertFalse(atomicBoolean0.get())

    def test16(self) -> None:

        jDKStringConverter0 = JDKStringConverter.valueOf("ATOMIC_BOOLEAN")
        class0 = ChronoLocalDate

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "ATOMIC_BOOLEAN")
            # Boolean value must be 'true' or 'false', case insensitive
            self.verifyException("org.joda.convert.JDKStringConverter$19", ValueError)

    def test15(self) -> None:

        jDKStringConverter0 = JDKStringConverter.LOCALE
        class0 = Date
        locale0 = jDKStringConverter0.convertFromString(class0, "CHARACTER")
        self.assertEqual("", locale0.getVariant())

    def test14(self) -> None:

        jDKStringConverter0 = JDKStringConverter.LOCALE
        class0 = Date
        object0 = jDKStringConverter0.convertFromString(class0, "r_^1_RfW-Xv,")
        self.assertEqual("r_^1_RfW-Xv,", str(object0))

    def test13(self) -> None:

        jDKStringConverter0 = JDKStringConverter.LOCALE
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "zsed^=XjU^U_}f)f")
        self.assertEqual("zsed^=xju^u_}F)F", str(object0))

    def test12(self) -> None:

        jDKStringConverter0 = JDKStringConverter.INET_ADDRESS
        class0 = jDKStringConverter0.getEffectiveType()
        jDKStringConverter1 = JDKStringConverter.DATE

        with pytest.raises(RuntimeError):
            jDKStringConverter1.convertFromString(
                class0, "Method names must not be null"
            )
            self.fail("Expecting exception: RuntimeError")

    def test11(self) -> None:

        jDKStringConverter0 = JDKStringConverter.DATE
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "==")
            self.fail("Expecting exception: ValueError")

        # Unable to parse date: ==
        # verifyException("org.joda.convert.JDKStringConverter$30", e)

    def test10(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CALENDAR

        try:
            jDKStringConverter0.convertToString(jDKStringConverter0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.assertEqual(
                str(e), "Unable to convert calendar as it is not a GregorianCalendar"
            )

    def test09(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CALENDAR
        class0 = jDKStringConverter0.getEffectiveType()

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(class0, "B]y4m")
            pytest.fail("Expecting exception: ValueError")

    def test08(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CALENDAR
        class0 = object

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(
                class0,
                "Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'",
            )

        # Unable to parse date: Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'
        # verifyException("org.joda.convert.JDKStringConverter$31", e)

    def test07(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY
        class0 = Date
        object0 = jDKStringConverter0.convertFromString(class0, "QV4I#H4;eA~=")
        self.assertIsNotNone(object0)

    def test06(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CHAR_ARRAY
        class0 = jDKStringConverter0.getType()
        self.assertFalse(inspect.isclass(class0))

    def test05(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CHAR_SEQUENCE
        class0 = jDKStringConverter0.getType()
        self.assertFalse(class0.isPrimitive())

    def test04(self) -> None:

        jDKStringConverterArray0 = JDKStringConverter.values()
        self.assertEqual(31, len(jDKStringConverterArray0))

    def test03(self) -> None:

        jdk_string_converter0 = JDKStringConverter.DATE
        mock_date0 = MockDate()
        string0 = jdk_string_converter0.convertToString(mock_date0)
        self.assertEqual("2014-02-14T20:21:21.320+00:00", string0)

    def test02(self) -> None:

        jDKStringConverter0 = JDKStringConverter.DATE
        class0 = Date

        with pytest.raises(ValueError):
            jDKStringConverter0.convertFromString(
                class0, "StringConverterFactory array must not contain a null element"
            )

        # Unable to parse date: StringConverterFactory array must not contain a null element
        # verifyException("org.joda.convert.JDKStringConverter$30", e)

    def test01(self) -> None:

        jDKStringConverter0 = JDKStringConverter.CALENDAR
        class0 = Date

        try:
            jDKStringConverter0.convertFromString(
                class0, "org.joda.convert.JDKStringConverter"
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.JDKStringConverter$31", e)

    def test00(self) -> None:

        jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY
        class0 = jDKStringConverter0.getEffectiveType()
        object0 = jDKStringConverter0.convertFromString(class0, "ZbN_| ]t?uLQ")
        string0 = jDKStringConverter0.convertToString(object0)
        self.assertEqual("ZbN////t/uLQ", string0)
