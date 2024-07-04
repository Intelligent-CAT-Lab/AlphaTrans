from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Arg import *

# from src.test.org.apache.commons.validator.Arg_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Arg_ESTest(unittest.TestCase):

    def test18(self) -> None:
        arg0 = Arg()
        arg0.setPosition(3166)
        self.assertEqual(3166, arg0.getPosition())

    def test17(self) -> None:
        arg0 = Arg()
        arg0.getKey()
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())

    def test16(self) -> None:
        arg0 = Arg()
        boolean0 = arg0.isResource()
        self.assertTrue(boolean0)
        self.assertEqual(-1, arg0.getPosition())

    def test15(self) -> None:

        arg0 = Arg()
        arg1 = arg0.clone()
        self.assertTrue(arg1.isResource())
        self.assertEqual(-1, arg1.getPosition())

    def test14(self) -> None:
        arg0 = Arg()
        arg0.getName()
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())

    def test13(self) -> None:
        arg0 = Arg()
        arg0.setKey("{fr;")
        string0 = arg0.getKey()
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())
        self.assertIsNotNone(string0)

    def test12(self) -> None:
        arg0 = Arg()
        arg0.getBundle()
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())

    def test11(self) -> None:

        arg0 = Arg()
        arg0.setName("org.apache.commons.validator.Arg")
        string0 = arg0.getName()
        assert string0 is not None
        assert arg0.isResource()
        assert arg0.getPosition() == -1

    def test10(self) -> None:
        arg0 = Arg()
        int0 = arg0.getPosition()
        self.assertEqual(-1, int0)
        self.assertTrue(arg0.isResource())

    def test09(self) -> None:

        arg0 = Arg()
        arg0.setBundle("")
        string0 = arg0.getBundle()
        self.assertIsNotNone(string0)
        self.assertEqual(-1, arg0.getPosition())
        self.assertTrue(arg0.isResource())

    def test08(self) -> None:

        arg0 = Arg()
        arg0._bundle = (
            "Arg: name=null  key=null  position=-1  bundle=null  resource=true\n"
        )
        string0 = arg0.getBundle()
        self.assertEqual((-1), arg0.getPosition())
        self.assertTrue(arg0.isResource())
        self.assertIsNotNone(string0)

    def test07(self) -> None:

        arg0 = Arg()
        arg0._key = ""
        string0 = arg0.getKey()
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())
        self.assertIsNotNone(string0)

    def test06(self) -> None:

        arg0 = Arg()
        arg0._name = ""
        string0 = arg0.getName()
        self.assertIsNotNone(string0)
        self.assertTrue(arg0.isResource())
        self.assertEqual(-1, arg0.getPosition())

    def test05(self) -> None:

        arg0 = Arg()
        arg0._position = 1675
        int0 = arg0.getPosition()
        self.assertEqual(1675, int0)

    def test04(self) -> None:

        arg0 = Arg()
        self.assertEqual(-1, arg0.getPosition())

        arg0.position = 0
        int0 = arg0.getPosition()
        self.assertEqual(0, int0)

    def test03(self) -> None:

        arg0 = Arg()
        self.assertTrue(arg0.isResource())

        arg0._resource = False
        arg0.isResource()
        self.assertEqual(-1, arg0.getPosition())

    def test02(self) -> None:
        arg0 = Arg()
        arg0._resource = False
        arg0.setResource(True)
        self.assertTrue(arg0.isResource())

    def test01(self) -> None:

        arg0 = Arg()
        arg0._bundle = ""
        string0 = arg0.toString()
        self.assertEqual(
            "Arg: name=None  key=None  position=-1  bundle=  resource=True\n", string0
        )

    def test00(self) -> None:

        arg0 = Arg()
        arg0.setKey("Pn")
        string0 = arg0.toString()
        self.assertEqual(
            "Arg: name=None  key=Pn  position=-1  bundle=None  resource=True\n", string0
        )
