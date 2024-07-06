from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.DaitchMokotoffSoundex import *

# from src.test.org.apache.commons.codec.language.DaitchMokotoffSoundex_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DaitchMokotoffSoundex_ESTest(unittest.TestCase):

    def test09(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1()
        string0 = daitchMokotoffSoundex0.soundex0(
            "org.apache.comm4ns.codec.language.DaitchMokotoffSoundex"
        )
        self.assertEqual("095744|095745|095754|095755", string0)

    def test07(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex(False)
        string0 = daitchMokotoffSoundex0.encode1("`%")
        self.assertEqual("000000", string0)
        self.assertIsNotNone(string0)

    def test06(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1()
        object0 = daitchMokotoffSoundex0.encode0("/*\u00EE=i")
        self.assertEqual("000000", object0)
        self.assertIsNotNone(object0)

    def test04(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1()

        with pytest.raises(RuntimeError):
            daitchMokotoffSoundex0.soundex0(None)

    def test03(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1()
        string0 = daitchMokotoffSoundex0.soundex0("=A8S(N$6mMVaL'?")
        self.assertEqual("046678", string0)

    def test02(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex(False)
        try:
            daitchMokotoffSoundex0.encode0(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Parameter supplied to DaitchMokotoffSoundex encode is not of type java.lang.String
            #
            self.verifyException(
                "org.apache.commons.codec.language.DaitchMokotoffSoundex", e
            )

    def test01(self) -> None:

        daitchMokotoffSoundex0 = DaitchMokotoffSoundex(False)
        string0 = daitchMokotoffSoundex0.encode1(None)
        self.assertIsNone(string0)
