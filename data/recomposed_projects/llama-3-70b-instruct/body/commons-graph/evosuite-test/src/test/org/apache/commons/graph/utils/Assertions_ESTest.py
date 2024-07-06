from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.utils.Assertions import *

# from src.test.org.apache.commons.graph.utils.Assertions_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Assertions_ESTest(unittest.TestCase):

    def test17(self) -> None:

        objectArray0 = [None] * 2
        Assertions.checkArgument(True, ">F_N7VUY{+^Y_?e", objectArray0)
        self.assertEqual(2, len(objectArray0))

    def test16(self) -> None:

        objectArray0 = [None] * 1

        try:
            Assertions.checkArgument(False, "*?xPHo4x$%VZId", objectArray0)
            self.fail("Expecting exception: UnknownFormatConversionException")

        except ValueError as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test15(self) -> None:

        object0 = object()
        objectArray0 = [None]
        object1 = Assertions.checkNotNull(
            object0, "org.apache.commons.graph.utils.Assertions", objectArray0
        )
        self.assertIs(object1, object0)

    def test14(self) -> None:

        objectArray0 = [None]

        with pytest.raises(RuntimeError):
            Assertions.checkNotNull(None, ",NIUv", objectArray0)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test13(self) -> None:

        objectArray0 = [None] * 1
        Assertions.checkState(
            True, "org.apache.commons.graph.utils.Assertions", objectArray0
        )
        self.assertEqual(1, len(objectArray0))

    def test12(self) -> None:

        objectArray0 = [None] * 2

        try:
            Assertions.checkState(False, "@ErA-$n|]mRqwH", objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test11(self) -> None:

        objectArray0 = [None] * 1

        try:
            Assertions.checkArgument(False, '=sDq"ZS', objectArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test10(self) -> None:

        objectArray0 = [None] * 5

        try:
            Assertions.checkArgument(False, None, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test09(self) -> None:

        objectArray0 = [None] * 2
        objectArray0[0] = ":8}79/vFN%e2"

        try:
            Assertions.checkArgument(False, ":8}79/vFN%e2", objectArray0)
            self.fail("Expecting exception: IllegalFormatConversionException")

        except IllegalFormatConversionException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test08(self) -> None:

        objectArray0 = []

        try:
            Assertions.checkArgument(False, "%x", objectArray0)
            self.fail("Expecting exception: MissingFormatArgumentException")

        except ValueError as e:
            self.verifyException("java.util.Formatter", e)

    def test07(self) -> None:

        objectArray0 = [None]

        with pytest.raises(RuntimeError):
            Assertions.checkNotNull(None, None, objectArray0)

    def test06(self) -> None:

        objectArray0 = [None] * 17

        try:
            Assertions.checkNotNull(None, "?T1GF0]641W%,b", objectArray0)
            self.fail("Expecting exception: FormatFlagsConversionMismatchException")

        except FormatFlagsConversionMismatchException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test05(self) -> None:

        object0 = object()
        objectArray0 = [None] * 1
        objectArray0[0] = object0

        try:
            Assertions.checkNotNull(None, "k>eVq>Y4-S/Po%ddY", objectArray0)
            self.fail("Expecting exception: IllegalFormatConversionException")

        except IllegalFormatConversionException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test04(self) -> None:

        objectArray0 = [None] * 7

        try:
            Assertions.checkNotNull(None, "%<2bPu?oxXw5@,+", objectArray0)
            self.fail("Expecting exception: MissingFormatArgumentException")

        except MissingFormatArgumentException as e:
            self.verifyException("java.util.Formatter", e)

    def test03(self) -> None:

        objectArray0 = [None] * 7

        try:
            Assertions.checkNotNull(None, "t6$|%<0eu", objectArray0)
            self.fail("Expecting exception: MissingFormatWidthException")

        except MissingFormatWidthException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test02(self) -> None:

        try:
            Assertions.checkNotNull(None, '%5Qwl<]@/fAtZ"', None)
            self.fail("Expecting exception: UnknownFormatConversionException")

        except UnknownFormatConversionException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test01(self) -> None:

        objectArray0 = [None] * 5

        try:
            Assertions.checkState(False, None, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test00(self) -> None:

        objectArray0 = [None] * 6

        try:
            Assertions.checkState(False, "Q%IR", objectArray0)
            self.fail("Expecting exception: UnknownFormatConversionException")

        except RuntimeError as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)
