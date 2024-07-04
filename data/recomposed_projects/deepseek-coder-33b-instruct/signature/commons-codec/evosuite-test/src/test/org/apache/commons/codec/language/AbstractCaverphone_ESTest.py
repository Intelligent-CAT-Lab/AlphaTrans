from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.test.org.apache.commons.codec.language.AbstractCaverphone_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.language.Caverphone1 import *
from src.main.org.apache.commons.codec.language.Caverphone2 import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AbstractCaverphone_ESTest(unittest.TestCase):

    def test3(self) -> None:

        caverphone1_0 = Caverphone1()
        boolean0 = caverphone1_0.isEncodeEqual("#k3$Fm", "#k3$Fm")
        self.assertTrue(boolean0)

    def test2(self) -> None:

        caverphone2_0 = Caverphone2()
        object0 = caverphone2_0.encode("")
        self.assertEqual("1111111111", object0)

    def test1(self) -> None:

        caverphone2_0 = Caverphone2()
        try:
            caverphone2_0.encode(caverphone2_0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Parameter supplied to Caverphone encode is not of type java.lang.String
            self.verifyException(
                "org.apache.commons.codec.language.AbstractCaverphone", e
            )

    def test0(self) -> None:

        caverphone2_0 = Caverphone2()
        boolean0 = caverphone2_0.isEncodeEqual("fH=wJ~F5?s/PRO=", "`+%='kr*{rr.a]b")
        self.assertFalse(boolean0)
