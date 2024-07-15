from __future__ import annotations
import time
import locale
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.AmbiguousOptionException import *

# from src.test.org.apache.commons.cli.AmbiguousOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AmbiguousOptionException_ESTest(unittest.TestCase):

    def test2(self) -> None:
        list0 = ["d=7 pDtt,nCa"]
        ambiguousOptionException0 = AmbiguousOptionException("d=7 pDtt,nCa", list0)
        collection0 = ambiguousOptionException0.getMatchingOptions()
        self.assertTrue("d=7 pDtt,nCa" in collection0)

    def test1(self) -> None:

        locale_IsoCountryCode0 = Locale.IsoCountryCode.PART3
        set0 = Locale.getISOCountries(locale_IsoCountryCode0)
        ambiguousOptionException0 = AmbiguousOptionException("'  (could be: ", set0)

    def test0(self) -> None:

        ambiguousOptionException0 = None
        try:
            ambiguousOptionException0 = AmbiguousOptionException(
                "b+ypAm<DOx,Ai~yI", None
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.cli.AmbiguousOptionException", e)
