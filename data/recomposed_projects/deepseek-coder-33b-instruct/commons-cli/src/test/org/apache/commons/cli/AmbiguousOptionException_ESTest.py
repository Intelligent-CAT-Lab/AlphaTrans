from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.AmbiguousOptionException import *

# from src.main.org.apache.commons.cli.AmbiguousOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AmbiguousOptionException_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test2(self) -> None:
        linkedList0 = []
        ambiguousOptionException0 = AmbiguousOptionException(
            "dVV]JIk_YP1X}i.", linkedList0
        )
        collection0 = ambiguousOptionException0.getMatchingOptions()
        self.assertFalse("dVV]JIk_YP1X}i." in collection0)

    @pytest.mark.test
    def test1(self) -> None:
        locale_IsoCountryCode0 = Locale.IsoCountryCode.PART1_ALPHA2
        set0 = Locale.getISOCountries(locale_IsoCountryCode0)
        ambiguousOptionException0 = AmbiguousOptionException(")mvOKs8Q:<o-X9.r6", set0)

    @pytest.mark.test
    def test0(self) -> None:
        ambiguousOptionException0 = None
        try:
            ambiguousOptionException0 = AmbiguousOptionException(">h@", None)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.AmbiguousOptionException", e)
