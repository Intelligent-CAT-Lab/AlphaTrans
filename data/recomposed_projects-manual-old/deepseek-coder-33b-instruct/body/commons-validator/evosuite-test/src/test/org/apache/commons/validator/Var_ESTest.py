from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Var import *

# from src.test.org.apache.commons.validator.Var_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Var_ESTest(unittest.TestCase):

    def test18(self) -> None:

        var0 = Var(1, 'eD"`+mvS,e\t-', 'eD"`+mvS,e\t-', "")
        string0 = var0.getJsType()
        self.assertFalse(var0.isResource())
        self.assertIsNotNone(string0)
        self.assertEqual("", string0)
        self.assertEqual('eD"`+mvS,e\t-', var0.getValue())
        self.assertEqual('eD"`+mvS,e\t-', var0.getName())

    def test17(self) -> None:

        var0 = Var(1, 'eD"`+mvS,e\t-', 'eD"`+mvS,e\t-', "")
        self.assertEqual("", var0.getJsType())

        var0.setJsType('eD"`+mvS,e\t-')
        string0 = var0.getJsType()
        self.assertEqual('eD"`+mvS,e\t-', string0)

    def test16(self) -> None:

        var0 = Var(1, 'eD"`+mvS,e\t-', 'eD"`+mvS,e\t-', "")
        self.assertFalse(var0.isResource())

        var0.setResource(True)
        var0.toString()
        self.assertTrue(var0.isResource())

    def test15(self) -> None:

        var0 = Var(3188, "", "", "a;zTu9C8@s{8xNzX")
        string0 = var0.getName()
        self.assertIsNone(string0)
        self.assertFalse(var0.isResource())

    def test14(self) -> None:

        var0 = Var(3188, "", "", "a;zTu9C8@s{8xNzX")
        string0 = var0.getValue()
        self.assertFalse(var0.isResource())
        self.assertIsNone(string0)

    def test13(self) -> None:

        var0 = Var(-1, None, None, None)
        boolean0 = var0.isResource()
        self.assertFalse(boolean0)

    def test12(self) -> None:

        var0 = Var(3188, "", "", "a;zTu9C8@s{8xNzX")
        string0 = var0.getBundle()
        self.assertIsNone(string0)
        self.assertFalse(var0.isResource())

    def test11(self) -> None:

        var0 = Var(3188, "", "", "a;zTu9C8@s{8xNzX")
        var1 = var0.clone()
        self.assertFalse(var1.isResource())

    def test10(self) -> None:

        var0 = Var(1, 'eD"`+mvS,e\t-', 'eD"`+mvS,e\t-', "")
        var0.setBundle("")
        self.assertEqual("", var0.getJsType())
        self.assertEqual('eD"`+mvS,e\t-', var0.getName())
        self.assertEqual('eD"`+mvS,e\t-', var0.getValue())
        self.assertFalse(var0.isResource())
        self.assertEqual("", var0.getBundle())

    def test09(self) -> None:

        var0 = Var(3188, "", "", "a;zTu9C8@s{8xNzX")
        string0 = var0.toString()
        self.assertEqual(
            "Var: name=null  value=null  resource=false  jsType=null\n", string0
        )

    def test08(self) -> None:

        var0 = Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "")
        var0.setBundle("")
        string0 = var0.getBundle()
        self.assertEqual("", string0)
        self.assertFalse(var0.isResource())

    def test07(self) -> None:

        var0 = Var(-1, None, None, None)
        var0.setBundle("org.apache.commons.validator.Var")
        string0 = var0.getBundle()
        self.assertEqual("org.apache.commons.validator.Var", string0)
        self.assertFalse(var0.isResource())

    def test06(self) -> None:

        var0 = Var(0, "", "", None)
        string0 = var0.getJsType()
        self.assertFalse(var0.isResource())
        self.assertIsNone(string0)

    def test05(self) -> None:

        var0 = Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "")
        var0.setName("")
        var0.getName()
        self.assertFalse(var0.isResource())
        self.assertEqual("", var0.getName())

    def test04(self) -> None:

        var0 = Var(0, "", "", None)
        var0.setName("sD@!\n")
        assert var0.getName() == "sD@!\n"
        assert not var0.isResource()
        assert var0.getName() == "sD@!\n"

    def test03(self) -> None:

        var0 = Var(0, "", "", None)
        var0.setValue("")
        string0 = var0.getValue()
        self.assertFalse(var0.isResource())
        self.assertEqual("", string0)

    def test02(self) -> None:

        var0 = Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "")
        var0.setValue("Var: name=")
        var0.getValue()
        self.assertFalse(var0.isResource())
        self.assertEqual("Var: name=", var0.getValue())

    def test01(self) -> None:

        var0 = Var(-1, None, None, None)
        self.assertFalse(var0.isResource())

        var0.setResource(True)
        boolean0 = var0.isResource()
        self.assertTrue(boolean0)

    def test00(self) -> None:

        var0 = Var(1, None, "", "")
        self.assertEqual("", var0.getJsType())
        self.assertEqual("", var0.getValue())
        self.assertFalse(var0.isResource())
