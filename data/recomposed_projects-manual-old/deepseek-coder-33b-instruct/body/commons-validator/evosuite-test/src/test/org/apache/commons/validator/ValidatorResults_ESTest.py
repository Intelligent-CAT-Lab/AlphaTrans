from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.ValidatorResult import *
from src.main.org.apache.commons.validator.ValidatorResults import *

# from src.test.org.apache.commons.validator.ValidatorResults_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ValidatorResults_ESTest(unittest.TestCase):

    def test17(self) -> None:

        validatorResults0 = ValidatorResults()
        set0 = validatorResults0.getPropertyNames()
        self.assertEqual(0, len(set0))

    def test16(self) -> None:

        validatorResults0 = ValidatorResults()
        self.assertTrue(validatorResults0.isEmpty())

        field0 = Field()
        validatorResults0.add0(field0, "[]", True)
        boolean0 = validatorResults0.isEmpty()
        self.assertFalse(boolean0)

    def test15(self) -> None:
        validatorResults0 = ValidatorResults()
        validatorResults0.merge(validatorResults0)
        self.assertTrue(validatorResults0.isEmpty())

    def test14(self) -> None:
        validatorResults0 = ValidatorResults()
        validatorResults0.clear()
        self.assertTrue(validatorResults0.isEmpty())

    def test13(self) -> None:

        validatorResults0 = ValidatorResults()
        boolean0 = validatorResults0.isEmpty()
        self.assertTrue(boolean0)

    def test12(self) -> None:

        validatorResults0 = ValidatorResults()
        field0 = Field()
        validatorResults0.add0(field0, "[]", True)
        map0 = validatorResults0.getResultValueMap()
        self.assertTrue(not map0)

    def test11(self) -> None:

        validatorResults0 = ValidatorResults()
        field0 = Field()
        object0 = object()
        validatorResults0.add1(field0, "[]", False, object0)
        map0 = validatorResults0.getResultValueMap()
        self.assertFalse(map0)

    def test10(self) -> None:
        validatorResults0 = ValidatorResults()
        validatorResult0 = validatorResults0.getValidatorResult(None)
        self.assertIsNone(validatorResult0)

    def test09(self) -> None:

        validatorResults0 = ValidatorResults()
        field0 = Field()
        object0 = object()
        validatorResults0.add1(field0, "", False, object0)
        validatorResults0.add1(field0, "~+^*", False, object0)
        self.assertIsNone(field0.getProperty())

    def test08(self) -> None:

        validatorResults0 = ValidatorResults()
        try:
            validatorResults0.add0(None, "L*", True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.validator.ValidatorResults", e)

    def test07(self) -> None:

        validatorResults0 = ValidatorResults()

        try:
            validatorResults0.add1(None, "", True, "")
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertIsNone(e.getMessage())

    def test06(self) -> None:

        validatorResults0 = ValidatorResults()
        validatorResults0.hResults = None

        with self.assertRaises(RuntimeError):
            validatorResults0.clear()
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.validator.ValidatorResults", RuntimeError)

    def test05(self) -> None:

        validatorResults0 = ValidatorResults()
        validatorResults0.hResults = None

        with self.assertRaises(RuntimeError):
            validatorResults0.getPropertyNames()

    def test04(self) -> None:

        validatorResults0 = ValidatorResults()
        validatorResults0.hResults = None

        try:
            validatorResults0.getResultValueMap()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(type(e)), "<class 'RuntimeError'>")

    def test03(self) -> None:

        validatorResults0 = ValidatorResults()
        validatorResults0._hResults = None

        with self.assertRaises(RuntimeError):
            validatorResults0.getValidatorResult("[]")

    def test02(self) -> None:

        validatorResults0 = ValidatorResults()
        validatorResults0._hResults = None

        with pytest.raises(RuntimeError):
            validatorResults0.isEmpty()

    def test01(self) -> None:

        validatorResults0 = ValidatorResults()

        try:
            validatorResults0.merge(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test00(self) -> None:

        validatorResults0 = ValidatorResults()
        field0 = Field()
        validatorResults0.add0(
            field0, "org.apache.commons.validator.ValidatorResult$ResultStatus", False
        )
        validatorResult0 = validatorResults0.getValidatorResult(None)
        self.assertIsNotNone(validatorResult0)
