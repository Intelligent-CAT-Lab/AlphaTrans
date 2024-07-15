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
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.ValidatorResult import *

# from src.test.org.apache.commons.validator.ValidatorResult_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ValidatorResult_ESTest(unittest.TestCase):

    def test26(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult_ResultStatus0 = ResultStatus.ResultStatus0(
            validatorResult0, True, field0
        )
        validatorResult_ResultStatus0.getResult()
        self.assertTrue(validatorResult_ResultStatus0.isValid())

    def test25(self) -> None:
        validatorResult0 = ValidatorResult(None)
        validatorResult_ResultStatus0 = ValidatorResult.ResultStatus.ResultStatus0(
            validatorResult0, False, validatorResult0
        )
        validatorResult_ResultStatus0.setValid(False)
        self.assertFalse(validatorResult_ResultStatus0.isValid())

    def test24(self) -> None:

        object0 = object()
        validatorResult0 = ValidatorResult(None)
        validatorResult_ResultStatus0 = ResultStatus(
            1, object0, validatorResult0, False
        )
        validatorResult_ResultStatus0.setResult(None)
        self.assertFalse(validatorResult_ResultStatus0.isValid())

    def test23(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.add0("[]", True)
        boolean0 = validatorResult0.isValid("[]")
        self.assertTrue(boolean0)

    def test22(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        map0 = validatorResult0.getActionMap()
        validatorResult0._hAction = map0

        with self.assertRaises(NotImplementedError):
            validatorResult0.add0("[]", False)

    def test21(self) -> None:
        validatorResult0 = ValidatorResult(None)
        iterator0 = validatorResult0.getActions()
        assert iterator0 is not None

    def test20(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        boolean0 = validatorResult0.containsAction("[]")
        self.assertFalse(boolean0)

    def test19(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.add1("[]", False, field0)
        boolean0 = validatorResult0.containsAction("[]")
        self.assertTrue(boolean0)

    def test18(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        boolean0 = validatorResult0.isValid("[]")
        self.assertFalse(boolean0)

    def test17(self) -> None:
        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.add1("[]", True, field0)
        field1 = validatorResult0.getResult("[]")
        self.assertEqual(0, field1.getPage())

    def test16(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        object0 = validatorResult0.getResult(
            "org.apache.commons.validator.ValidatorResult"
        )
        self.assertIsNone(object0)

    def test15(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult_ResultStatus0 = ResultStatus(1, None, validatorResult0, False)
        self.assertFalse(validatorResult_ResultStatus0.isValid())

    def test14(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.hAction = None

        with self.assertRaises(RuntimeError):
            validatorResult0.add0("[]", True)

    def test13(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.hAction = None

        try:
            validatorResult0.add1("[]", False, field0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.validator.ValidatorResult", e)

    def test12(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        map0 = validatorResult0.getActionMap()
        validatorResult0.hAction = map0

        with self.assertRaises(NotImplementedError):
            validatorResult0.add1("[]", False, "[]")

    def test11(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0._hAction = None

        with self.assertRaises(RuntimeError):
            validatorResult0.containsAction("[]")

    def test10(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0._hAction = None

        with self.assertRaises(RuntimeError):
            validatorResult0.getActionMap()

    def test09(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0._hAction = None

        with self.assertRaises(RuntimeError):
            validatorResult0.getActions()

    def test08(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.hAction = None

        try:
            validatorResult0.getResult("X&5g^+`")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.validator.ValidatorResult", e)

    def test07(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        validatorResult0.hAction = None

        with self.assertRaises(RuntimeError):
            validatorResult0.isValid("[]")

    def test06(self) -> None:
        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        field0.setFieldOrder(-1604)
        field1 = validatorResult0.getField()
        self.assertIsNone(field1.getDepends())

    def test05(self) -> None:
        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        field0.setFieldOrder(1086)
        field1 = validatorResult0.getField()
        self.assertIsNone(field1.getProperty())

    def test04(self) -> None:

        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        field0.page = -4423
        field1 = validatorResult0.getField()
        self.assertEqual(0, field1.getFieldOrder())

    def test03(self) -> None:
        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        field0.setPage(1701)
        field1 = validatorResult0.getField()
        self.assertIsNone(field1.getDepends())

    def test02(self) -> None:
        field0 = Field()
        validatorResult0 = ValidatorResult(field0)
        field0.setClientValidation(False)
        field1 = validatorResult0.getField()
        self.assertEqual(0, field1.getPage())

    def test01(self) -> None:
        field0 = Field()
        field0.setIndexedListProperty("g(a\rQk")
        validatorResult0 = ValidatorResult(field0)
        field1 = validatorResult0.getField()
        self.assertIs(field1, field0)

    def test00(self) -> None:
        validatorResult0 = ValidatorResult(None)
        field0 = validatorResult0.getField()
        self.assertIsNone(field0)
