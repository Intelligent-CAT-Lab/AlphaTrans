from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Msg import *

# from src.test.org.apache.commons.validator.Msg_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Msg_ESTest(unittest.TestCase):

    def test14(self) -> None:

        msg0 = Msg()
        msg0.setBundle("  key=")
        self.assertTrue(msg0.isResource())

    def test13(self) -> None:

        msg0 = Msg()
        msg0.getBundle()
        self.assertTrue(msg0.isResource())

    def test12(self) -> None:

        msg0 = Msg()
        msg0.setKey("")
        string0 = msg0.getKey()
        assert string0 is not None
        assert msg0.isResource()

    def test11(self) -> None:

        msg0 = Msg()
        self.assertTrue(msg0.isResource())

        msg0.setResource(False)
        boolean0 = msg0.isResource()
        self.assertFalse(boolean0)

    def test10(self) -> None:

        msg0 = Msg()
        msg0.getName()
        self.assertTrue(msg0.isResource())

    def test09(self) -> None:

        msg0 = Msg()
        msg0.getKey()
        self.assertTrue(msg0.isResource())

    def test08(self) -> None:

        msg0 = Msg()
        boolean0 = msg0.isResource()
        self.assertTrue(boolean0)

    def test07(self) -> None:

        msg0 = Msg()
        msg1 = msg0.clone()
        self.assertTrue(msg1.isResource())

    def test06(self) -> None:

        msg0 = Msg()
        msg0._bundle = ""
        string0 = msg0.getBundle()
        self.assertIsNotNone(string0)
        self.assertTrue(msg0.isResource())

    def test05(self) -> None:

        msg0 = Msg()
        msg0._bundle = "  key="
        string0 = msg0.getBundle()
        self.assertIsNotNone(string0)
        self.assertTrue(msg0.isResource())

    def test04(self) -> None:

        msg0 = Msg()
        msg0.setKey(",dF*z{m")
        string0 = msg0.getKey()
        self.assertIsNotNone(string0)
        self.assertTrue(msg0.isResource())

    def test03(self) -> None:

        msg0 = Msg()
        msg0._name = ""
        string0 = msg0.getName()
        self.assertTrue(msg0.isResource())
        self.assertIsNotNone(string0)

    def test02(self) -> None:

        msg0 = Msg()
        msg0.setName("s$oc0a<k6")
        string0 = msg0.getName()
        self.assertTrue(msg0.isResource())
        self.assertIsNotNone(string0)

    def test01(self) -> None:

        msg0 = Msg()
        msg0.name = ""
        string0 = msg0.toString()
        self.assertEqual("Msg: name=  key=None  resource=True  bundle=None\n", string0)

    def test00(self) -> None:

        msg0 = Msg()
        msg0._bundle = "i{lR:Wbi.h:V(-}"
        string0 = msg0.toString()
        self.assertEqual(
            string0, "Msg: name=None  key=None  resource=True  bundle=i{lR:Wbi.h:V(-}\n"
        )
