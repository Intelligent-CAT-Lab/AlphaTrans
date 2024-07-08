from __future__ import annotations
import re
import os
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class RegexValidatorTest(unittest.TestCase):

    __SEPARATOR_2: str = "(?:\\s)"
    __SEPARATOR_1: str = "(?:\\-)"
    __COMPONENT_3: str = "([123]{3})"
    __COMPONENT_2: str = "([DEF]{3})"
    __COMPONENT_1: str = "([abc]{3})"
    __REGEX: str = "^([abc]*)(?:\\-)([DEF]*)(?:\\-)([123]*)$"
    __REGEX_3: str = "^" + __COMPONENT_1 + __COMPONENT_2 + __COMPONENT_3 + "$"
    __REGEX_2: str = (
        f"^{__COMPONENT_1}{__SEPARATOR_2}{__COMPONENT_2}{__SEPARATOR_2}{__COMPONENT_3}$"
    )
    __REGEX_1: str = (
        f"^{__COMPONENT_1}{__SEPARATOR_1}{__COMPONENT_2}{__SEPARATOR_1}{__COMPONENT_3}$"
    )
    __MULTIPLE_REGEX: typing.List[str] = [__REGEX_1, __REGEX_2, __REGEX_3]

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:
        super().setUp()

    def testToString(self) -> None:
        single: RegexValidator = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(
            "Single", "RegexValidator{" + self.__REGEX + "}", single.toString()
        )

        multiple: RegexValidator = RegexValidator.RegexValidator1(
            [self.__REGEX, self.__REGEX]
        )
        self.assertEqual(
            "Multiple",
            "RegexValidator{" + self.__REGEX + "," + self.__REGEX + "}",
            multiple.toString(),
        )

    def testExceptions(self) -> None:
        invalidRegex = "^([abCD12]*$"
        try:
            RegexValidator.RegexValidator3(invalidRegex)
        except re.error:
            pass

    def testMissingRegex(self) -> None:
        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator3(None)
            self.fail("Single Null - expected ValueError")
        self.assertEqual(
            "Single Null", "Regular expression[0] is missing", e.getMessage()
        )

        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator3("")
            self.fail("Single Zero Length - expected ValueError")
        self.assertEqual(
            "Single Zero Length", "Regular expression[0] is missing", e.getMessage()
        )

        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator1(None)
            self.fail("Null Array - expected ValueError")
        self.assertEqual(
            "Null Array", "Regular expressions are missing", e.getMessage()
        )

        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator1([])
            self.fail("Zero Length Array - expected ValueError")
        self.assertEqual(
            "Zero Length Array", "Regular expressions are missing", e.getMessage()
        )

        expressions = ["ABC", None]
        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator1(expressions)
            self.fail("Array has Null - expected ValueError")
        self.assertEqual(
            "Array has Null", "Regular expression[1] is missing", e.getMessage()
        )

        expressions = ["", "ABC"]
        with self.assertRaises(ValueError) as e:
            RegexValidator.RegexValidator1(expressions)
            self.fail("Array has Zero Length - expected ValueError")
        self.assertEqual(
            "Array has Zero Length", "Regular expression[0] is missing", e.getMessage()
        )

    def testNullValue(self) -> None:
        validator = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual("Instance isValid()", False, validator.isValid(None))
        self.assertEqual("Instance validate()", None, validator.validate(None))
        self.assertEqual("Instance match()", None, validator.match(None))

    def testMultipleInsensitive(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)

        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual("isValid() Multiple", True, multiple.isValid(value))
        self.assertEqual("isValid() 1st", False, single1.isValid(value))
        self.assertEqual("isValid() 2nd", True, single2.isValid(value))
        self.assertEqual("isValid() 3rd", False, single3.isValid(value))

        self.assertEqual("validate() Multiple", expect, multiple.validate(value))
        self.assertEqual("validate() 1st", None, single1.validate(value))
        self.assertEqual("validate() 2nd", expect, single2.validate(value))
        self.assertEqual("validate() 3rd", None, single3.validate(value))

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual("isValid() Invalid", False, multiple.isValid(value))
        self.assertEqual("validate() Invalid", None, multiple.validate(value))
        self.assertEqual("match() Multiple", None, multiple.match(value))

    def testMultipleSensitive(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)

        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual("Sensitive isValid() Multiple", True, multiple.isValid(value))
        self.assertEqual("Sensitive isValid() 1st", False, single1.isValid(value))
        self.assertEqual("Sensitive isValid() 2nd", True, single2.isValid(value))
        self.assertEqual("Sensitive isValid() 3rd", False, single3.isValid(value))

        self.assertEqual(
            "Sensitive validate() Multiple", expect, multiple.validate(value)
        )
        self.assertEqual("Sensitive validate() 1st", None, single1.validate(value))
        self.assertEqual("Sensitive validate() 2nd", expect, single2.validate(value))
        self.assertEqual("Sensitive validate() 3rd", None, single3.validate(value))

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual("isValid() Invalid", False, multiple.isValid(value))
        self.assertEqual("validate() Invalid", None, multiple.validate(value))
        self.assertEqual("match() Multiple", None, multiple.match(value))

    def testSingle(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        self.assertEqual(
            "Sensitive isValid() valid", True, sensitive.isValid("ac-DE-1")
        )
        self.assertEqual(
            "Sensitive isValid() invalid", False, sensitive.isValid("AB-de-1")
        )
        self.assertEqual(
            "Insensitive isValid() valid", True, insensitive.isValid("AB-de-1")
        )
        self.assertEqual(
            "Insensitive isValid() invalid", False, insensitive.isValid("ABd-de-1")
        )

        self.assertEqual(
            "Sensitive validate() valid", "acDE1", sensitive.validate("ac-DE-1")
        )
        self.assertEqual(
            "Sensitive validate() invalid", None, sensitive.validate("AB-de-1")
        )
        self.assertEqual(
            "Insensitive validate() valid", "ABde1", insensitive.validate("AB-de-1")
        )
        self.assertEqual(
            "Insensitive validate() invalid", None, insensitive.validate("ABd-de-1")
        )

        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )
        self.assertEqual(
            "validate one",
            "ABC",
            (RegexValidator.RegexValidator3("^([A-Z]*)$")).validate("ABC"),
        )
        self.__checkArray(
            "match one",
            ["ABC"],
            (RegexValidator.RegexValidator3("^([A-Z]*)$")).match("ABC"),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __checkArray(
        self, label: str, expect: typing.List[str], result: typing.List[str]
    ) -> None:
        if expect is None or result is None:
            if expect is None and result is None:
                return  # valid, both null
            else:
                self.fail(label + " Null expect=" + expect + " result=" + result)
            return  # not strictly necessary, but prevents possible NPE below

        if len(expect) != len(result):
            self.fail(
                label + " Length expect=" + len(expect) + " result=" + len(result)
            )

        for i in range(len(expect)):
            self.assertEqual(label + " value[" + i + "]", expect[i], result[i])
