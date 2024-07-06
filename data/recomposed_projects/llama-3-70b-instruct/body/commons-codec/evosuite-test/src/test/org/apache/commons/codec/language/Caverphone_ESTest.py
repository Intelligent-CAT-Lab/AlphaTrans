from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Caverphone import *

# from src.test.org.apache.commons.codec.language.Caverphone_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Caverphone_ESTest(unittest.TestCase):

    def test6(self) -> None:
        caverphone0 = Caverphone()
        boolean0 = caverphone0.isCaverphoneEqual(":h~k?EwnC.", ":h~k?EwnC.")
        self.assertTrue(boolean0)

    def test5(self) -> None:

        caverphone0 = Caverphone()
        object0 = caverphone0.encode0("S}i-#eXys3+QIkD")
        self.assertEqual("SKSKKT1111", object0)

    def test4(self) -> None:

        caverphone0 = Caverphone()
        string0 = caverphone0.encode1("S}i-#eXys3+QIkD")
        self.assertEqual(string0, "SKSKKT1111")

    def test3(self) -> None:

        caverphone0 = Caverphone()
        string0 = caverphone0.caverphone("dg")
        self.assertEqual("K111111111", string0)

    def test2(self) -> None:

        caverphone0 = Caverphone()
        object0 = object()
        try:
            caverphone0.encode0(object0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Parameter supplied to Caverphone encode is not of type java.lang.String
            self.verifyException("org.apache.commons.codec.language.Caverphone", e)

    def test0(self) -> None:
        caverphone0 = Caverphone()
        boolean0 = caverphone0.isCaverphoneEqual("Vj*RlZ<T/x<B", "%L_1Q)/{}g{@c)`q!")
        self.assertFalse(boolean0)
