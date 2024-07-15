from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Soundex import *

# from src.test.org.apache.commons.codec.language.Soundex_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Soundex_ESTest(unittest.TestCase):

    def test32(self) -> None:
        soundex0 = Soundex.US_ENGLISH
        int0 = soundex0.getMaxLength()
        self.assertEqual(4, int0)

    def test30(self) -> None:

        soundex0 = Soundex(0, True, "01230120022455012623010202", None)
        self.assertEqual(4, soundex0.getMaxLength())

    def test29(self) -> None:

        charArray0 = [""] * 1
        soundex0 = Soundex(2, False, "R232", charArray0)
        self.assertEqual(4, soundex0.getMaxLength())

    def test28(self) -> None:

        soundex0 = Soundex(1, True, "[ESVm-:1-J%d xs", None)

        try:
            soundex0.encode1("[ESVm-:1-J%d xs")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test27(self) -> None:

        charArray0 = [""] * 5
        soundex0 = Soundex(-3189, False, "#wn`ah#", charArray0)
        string0 = soundex0.soundex("#wn`ah#")
        self.assertEqual("W500", string0)
        self.assertEqual(4, soundex0.getMaxLength())

    def test26(self) -> None:

        charArray0 = ["-"] + ["0"] * 4
        soundex0 = Soundex(2, False, "01230120022455012623010202", charArray0)
        self.assertEqual(4, soundex0.getMaxLength())

    def test24(self) -> None:

        soundex0 = Soundex.US_ENGLISH_GENEALOGY
        string0 = soundex0.soundex("")
        assert string0 is not None
        self.assertEqual("", string0)

    def test23(self) -> None:

        charArray0 = ["\0"] * 6
        soundex0 = Soundex(1, True, "tMZ~y", charArray0)
        int0 = soundex0.US_ENGLISH.difference("tMZ~y", "ls}L,=e5s")
        self.assertEqual(0, int0)
        self.assertEqual(4, soundex0.getMaxLength())

    def test22(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        int0 = soundex0.difference(",&hw.", ",&hw.")
        self.assertEqual(int0, 4)

    def test20(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        object0 = soundex0.US_ENGLISH_SIMPLIFIED.encode0("GEx%a(J=Kn")
        self.assertEqual("G225", object0)

    def test19(self) -> None:

        soundex0 = Soundex.US_ENGLISH_GENEALOGY
        try:
            soundex0.encode0(soundex0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test18(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        string0 = soundex0.soundex(None)
        self.assertIsNone(string0)

    def test17(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        string0 = soundex0.US_ENGLISH_SIMPLIFIED.soundex("&R]`C$ZjTTG/mkXWX&1")
        self.assertEqual("R232", string0)

    def test16(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        string0 = soundex0.soundex("?Pw7GN2$jH_}}AWKO")
        self.assertEqual("P252", string0)

    def test15(self) -> None:

        soundex0 = Soundex.US_ENGLISH_GENEALOGY
        string0 = soundex0.soundex(" (index=")
        self.assertEqual("I532", string0)

    def test14(self) -> None:

        soundex0 = None
        try:
            soundex0 = Soundex(2, False, "01230120022455012623010202", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.codec.language.Soundex", e)
            self.assertIsInstance(e, RuntimeError)

    def test12(self) -> None:

        charArray0 = ["\0"] * 17
        soundex0 = Soundex(1, False, "l&nU<S=b[mc O/|", charArray0)

        try:
            soundex0.encode0("l&nU<S=b[mc O/|")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test11(self) -> None:

        charArray0 = [""] * 6
        soundex0 = Soundex(1, True, "SG}9^jv)Z*t]", charArray0)

        try:
            soundex0.soundex("SG}9^jv)Z*t]")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test07(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        string0 = soundex0.encode1("")
        self.assertEqual("", string0)

    def test06(self) -> None:

        soundex0 = Soundex.US_ENGLISH
        string0 = soundex0.encode1("?Pw7GN2$jH_}}AWKO")
        self.assertEqual("P252", string0)

    def test05(self) -> None:

        soundex0 = Soundex.US_ENGLISH_GENEALOGY
        string0 = soundex0.US_ENGLISH.encode1(None)
        self.assertIsNone(string0)

    def test04(self) -> None:
        soundex0 = Soundex.US_ENGLISH
        soundex0.setMaxLength((-1299))
        int0 = soundex0.getMaxLength()
        self.assertEqual((-1299), int0)

    def test03(self) -> None:
        soundex0 = Soundex.US_ENGLISH_SIMPLIFIED
        soundex0.setMaxLength(0)
        int0 = soundex0.getMaxLength()
        self.assertEqual(0, int0)

    def test02(self) -> None:

        soundex0 = Soundex(0, False, "01230120022455012623010202", None)
        self.assertEqual(4, soundex0.getMaxLength())

    def test01(self) -> None:

        charArray0 = [""] * 6
        soundex0 = Soundex(1, True, "tMZ~y", charArray0)

        try:
            soundex0.difference("8F=We8&{CTF0]dYY-mz", " K=")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.codec.language.Soundex", e)

    def test00(self) -> None:

        charArray0 = [""]
        soundex0 = Soundex(
            1,
            False,
            "Parameter supplied to Soundex encode is not of type java.lang.String",
            charArray0,
        )
        string0 = soundex0.soundex('Uv|Ukt"Yq oY(')
        self.assertEqual("U os", string0)
        self.assertEqual(4, soundex0.getMaxLength())
