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
from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.Field import *

# from src.test.org.apache.commons.validator.Field_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Field_ESTest(unittest.TestCase):

    def test59(self) -> None:

        field0 = Field()
        field0.getDependencyList()
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())

    def test58(self) -> None:

        field0 = Field()
        boolean0 = field0.isClientValidation()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(boolean0)

    def test57(self) -> None:

        field0 = Field()
        string0 = field0.getIndexedProperty()
        self.assertIsNone(string0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())

    def test56(self) -> None:

        field0 = Field()
        string0 = field0.getIndexedListProperty()
        self.assertIsNone(string0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())

    def test55(self) -> None:

        field0 = Field()
        string0 = field0.getDepends()
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertIsNone(string0)

    def test54(self) -> None:

        field0 = Field()
        int0 = field0.getPage()
        self.assertEqual(0, int0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())

    def test53(self) -> None:

        field0 = Field()
        int0 = field0.getFieldOrder()
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, int0)

    def test52(self) -> None:

        field0 = Field()
        field0.setKey(".")
        string0 = field0.getKey()

        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(".", string0)
        self.assertIsNotNone(string0)
        self.assertTrue(field0.isClientValidation())

    def test51(self) -> None:

        field0 = Field()
        string0 = field0.getProperty()
        self.assertIsNone(string0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())

    def test50(self) -> None:

        field0 = Field()
        field0.setDepends("\n")

        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertEqual("\n", field0.getDepends())
        self.assertTrue(field0.isClientValidation())

    def test49(self) -> None:

        field0 = Field()
        field0.addArg(None)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())

    def test48(self) -> None:

        field0 = Field()
        arg0 = Arg()
        field0.addArg(arg0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())

    def test47(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("")
        field0.addArg(arg0)
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(-1, arg0.getPosition())
        self.assertTrue(field0.isClientValidation())

    def test46(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        field0.addArg(arg0)
        field0.addArg(arg0)
        self.assertEqual(0, arg0.getPosition())
        self.assertEqual(0, field0.getPage())

    def test45(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.name = "[]"
        arg0.setKey("rw.apacefcommons.vLliator.ValidaorE8cepOin")
        field0.addArg(arg0)
        self.assertEqual(0, arg0.getPosition())

        field0.getArg1("org.apache.commons.validator.Field.DEFAULT", 0)
        self.assertEqual(0, field0.getPage())

    def test44(self) -> None:

        field0 = Field()
        arg0 = Arg()
        field0.args = None
        arg0.setKey("0U>KQl")

        try:
            field0.addArg(arg0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.validator.Field", e)

    def test43(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        arg0.setName("[]")
        field0.addArg(arg0)
        arg0.setPosition(-1)
        field0.addArg(arg0)
        self.assertEqual(1, arg0.getPosition())

    def test42(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        arg0.setPosition(5195)
        field0.addArg(arg0)
        arg0.setPosition(-606)
        field0.addArg(arg0)
        self.assertEqual(5196, arg0.getPosition())

    def test41(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        field0.addArg(arg0)
        arg0.setName("[]")
        arg0.setPosition(-20)
        field0.addArg(arg0)
        self.assertEqual(1, arg0.getPosition())

    def test40(self) -> None:

        field0 = Field()
        field0.getArg1("", 0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())

    def test39(self) -> None:

        field0 = Field()
        field0._key = ""
        string0 = field0.getKey()
        self.assertEqual("", string0)
        self.assertIsNotNone(string0)
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())

    def test38(self) -> None:

        field0 = Field()
        string0 = field0.getKey()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())
        self.assertIsNone(string0)

    def test37(self) -> None:

        field0 = Field()
        field0.setIndexedListProperty("")
        boolean0 = field0.isIndexed()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertFalse(boolean0)

    def test36(self) -> None:
        field0 = Field()
        field0.setIndexedListProperty("[]")
        boolean0 = field0.isIndexed()
        self.assertTrue(boolean0)

    def test35(self) -> None:

        field0 = Field()
        boolean0 = field0.isDependency("$S<4ijpBQ")
        self.assertFalse(boolean0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())

    def test34(self) -> None:

        field0 = Field()
        field0.setDepends("[]")
        boolean0 = field0.isDependency("[]")
        self.assertTrue(boolean0)
        self.assertEqual("[]", field0.getDepends())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())

    def test33(self) -> None:

        field0 = Field()
        field0.getArg0(0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())

    def test32(self) -> None:

        field0 = Field()
        mapArray0 = [{} for _ in range(4)]
        field0._args = mapArray0
        field0.getArg1(")Rb&=~=K}t", 0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())

    def test31(self) -> None:

        field0 = Field()
        mapArray0 = [{} for _ in range(4)]
        hashMap0 = {}
        mapArray0[0] = hashMap0
        field0.args = mapArray0
        field0.getArg1("", 0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())

    def test30(self) -> None:

        field0 = Field()
        arg0 = Arg()
        mapArray0 = [{} for _ in range(4)]
        field0.args = mapArray0
        mapArray0[0]["|V7pg0A*((2+"] = arg0
        arg1 = field0.getArg1("|V7pg0A*((2+", 0)
        self.assertIsNotNone(arg1)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())

    def test29(self) -> None:

        field0 = Field()
        boolean0 = field0.isIndexed()
        self.assertFalse(boolean0)
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())

    def test28(self) -> None:

        field0 = Field()

        try:
            field0.getArg0(-2372)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test27(self) -> None:

        field0 = Field()
        field0._args = None

        try:
            field0.getArg0(-13)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test26(self) -> None:

        field0 = Field()

        try:
            field0.getArg1("[]", -2372)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            pass

    def test25(self) -> None:

        field0 = Field()
        field0._args = None

        try:
            field0.getArg1("[]", 0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test24(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        field0.addArg(arg0)

        try:
            field0.getArgs(None)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test23(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.position = 5002
        arg0.setKey("[]")
        field0.addArg(arg0)
        field0.getArgs("&-<8K3$.__|")
        # Undeclared exception in Java code
        field0.getArgs(None)

    def test22(self) -> None:

        field0 = Field()

        try:
            field0.setDepends(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test21(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        field0.addArg(arg0)
        self.assertEqual(0, arg0.getPosition())

        field0.getArg0(0)
        self.assertEqual(0, field0.getFieldOrder())

    def test20(self) -> None:

        arg0 = Arg()
        arg0.setResource(False)
        arg0.setKey("fa$)&L/6m;o,4")
        field0 = Field()
        arg0.setPosition(696)
        field0.addArg(arg0)
        self.assertEqual(696, arg0.getPosition())

        field0.getArg0(696)
        self.assertEqual(0, field0.getPage())

    def test19(self) -> None:

        field0 = Field()
        arg0 = Arg()
        arg0.setKey("[]")
        field0.addArg(arg0)
        self.assertEqual(0, arg0.getPosition())

        field0.getArg1("var:", 0)
        self.assertEqual(0, field0.getFieldOrder())

    def test18(self) -> None:

        arg0 = Arg()
        arg0.setResource(False)
        arg0.setKey("fa$)&L/6m;o,4")
        field0 = Field()
        arg0.setPosition(696)
        field0.addArg(arg0)
        self.assertEqual(696, arg0.getPosition())

        field0.getArg1("No ValidatorAction named ", 696)
        self.assertTrue(field0.isClientValidation())

    def test17(self) -> None:

        field0 = Field()
        argArray0 = field0.getArgs("[]")
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, len(argArray0))

    def test16(self) -> None:

        field0 = Field()
        field0._depends = ""
        string0 = field0.getDepends()
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())
        self.assertEqual("", string0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertIsNotNone(string0)

    def test15(self) -> None:

        field0 = Field()
        field0.setDepends("Ki")
        string0 = field0.getDepends()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertEqual("Ki", string0)
        self.assertIsNotNone(string0)
        self.assertTrue(field0.isClientValidation())

    def test14(self) -> None:
        field0 = Field()
        field0.setFieldOrder(-143)
        int0 = field0.getFieldOrder()
        self.assertEqual(-143, int0)

    def test13(self) -> None:
        field0 = Field()
        field0.setFieldOrder(182)
        int0 = field0.getFieldOrder()
        self.assertEqual(182, int0)

    def test12(self) -> None:

        field0 = Field()
        field0.setIndexedListProperty("")
        string0 = field0.getIndexedListProperty()
        self.assertTrue(field0.isClientValidation())
        self.assertEqual("", string0)
        self.assertIsNotNone(string0)
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())

    def test11(self) -> None:

        field0 = Field()
        field0._indexedListProperty = "BaFJjva0n;X^N-V-"
        string0 = field0.getIndexedListProperty()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertIsNotNone(string0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual("BaFJjva0n;X^N-V-", string0)

    def test10(self) -> None:

        field0 = Field()
        field0.setIndexedProperty("")
        string0 = field0.getIndexedProperty()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertIsNotNone(string0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual("", string0)

    def test09(self) -> None:

        field0 = Field()
        field0.setIndexedProperty("0FRgz[b3e+WQ=zW3ADw")
        string0 = field0.getIndexedProperty()
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertEqual("0FRgz[b3e+WQ=zW3ADw", string0)
        self.assertTrue(field0.isClientValidation())
        self.assertIsNotNone(string0)

    def test08(self) -> None:
        field0 = Field()
        field0.setPage(-4551)
        int0 = field0.getPage()
        self.assertEqual(-4551, int0)

    def test07(self) -> None:
        field0 = Field()
        field0.setPage(502)
        int0 = field0.getPage()
        self.assertEqual(502, int0)

    def test06(self) -> None:

        field0 = Field()
        field0.setProperty("")
        string0 = field0.getProperty()
        self.assertEqual(0, field0.getPage())
        self.assertIsNotNone(string0)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual("", string0)
        self.assertTrue(field0.isClientValidation())

    def test05(self) -> None:

        field0 = Field()
        field0.setProperty("  key=")
        string0 = field0.getProperty()
        self.assertIsNotNone(string0)
        self.assertTrue(field0.isClientValidation())
        self.assertEqual(0, field0.getPage())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual("  key=", string0)

    def test04(self) -> None:

        field0 = Field()
        self.assertTrue(field0.isClientValidation())

        field0.setClientValidation(False)
        boolean0 = field0.isClientValidation()
        self.assertFalse(boolean0)

    def test03(self) -> None:

        field0 = Field()
        field0.setDepends("Tp9~S:($*K'@*d.\"Y,")

        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual("Tp9~S:($*K'@*d.\"Y,", field0.getDepends())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())

    def test02(self) -> None:

        field0 = Field()
        field0.getArg0(1)
        self.assertEqual(0, field0.getFieldOrder())
        self.assertEqual(0, field0.getPage())
        self.assertTrue(field0.isClientValidation())

    def test01(self) -> None:

        field0 = Field()
        field0.setProperty("  key=")
        field0.indexedListProperty = "/s[Vy/["
        field0.generateKey()
        self.assertTrue(field0.isIndexed())

    def test00(self) -> None:

        field0 = Field()
        field0.setProperty("dpG'G8 F*m")
        field0.generateKey()

        self.assertEqual("dpG'G8 F*m", field0.getProperty())
        self.assertEqual(0, field0.getPage())
        self.assertFalse(field0.isIndexed())
        self.assertEqual(0, field0.getFieldOrder())
        self.assertTrue(field0.isClientValidation())
