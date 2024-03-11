# Imports Begin
from src.main.org.apache.commons.validator.routines.RegexValidator import *
import unittest
import typing
from typing import *

# Imports End


class RegexValidatorTest(unittest.TestCase, TestCase):

    # Class Fields Begin
    __REGEX: str = "^([abc]*)(?:\\-)([DEF]*)(?:\\-)([123]*)$"
    __COMPONENT_1: str = ""  # LLM could not translate field
    __COMPONENT_2: str = "([DEF]{3})"
    __COMPONENT_3: str = "([123]{3})"
    __SEPARATOR_1: str = ""  # LLM could not translate field
    __SEPARATOR_2: str = "(?:\\s)"
    __REGEX_1: str = (
        "^" + COMPONENT_1 + SEPARATOR_1 + COMPONENT_2 + SEPARATOR_1 + COMPONENT_3 + "$"
    )
    __REGEX_2: str = (
        "^" + COMPONENT_1 + SEPARATOR_2 + COMPONENT_2 + SEPARATOR_2 + COMPONENT_3 + "$"
    )
    __REGEX_3: str = "^" + COMPONENT_1 + COMPONENT_2 + COMPONENT_3 + "$"
    __MULTIPLE_REGEX: List[str] = [REGEX_1, REGEX_2, REGEX_3]
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:

        super().tearDown()

    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testToString(self) -> None:

        pass  # LLM could not translate method body

    def testExceptions(self) -> None:

        invalid_regex = "^([abCD12]*$"
        try:
            RegexValidator.RegexValidator3(invalid_regex)
        except re.error:
            pass

    def testMissingRegex(self) -> None:

        pass  # LLM could not translate method body

    def testNullValue(self) -> None:

        validator = RegexValidator.RegexValidator3(REGEX)
        self.assertEqual(validator.isValid(None), False)
        self.assertEqual(validator.validate(None), None)
        self.assertEqual(validator.match(None), None)

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

        pass  # LLM could not translate method body

    def testSingle(self) -> None:

        pass  # LLM could not translate method body

    def __init__(self, name: str) -> None:

        super().__init__(name)

    def __checkArray(
        self, label: str, expect: typing.List[str], result: typing.List[str]
    ) -> None:

        if expect is None or result is None:
            if expect is None and result is None:
                return
            else:
                self.fail(f"{label} Null expect={expect} result={result}")
            return
        if len(expect) != len(result):
            self.fail(f"{label} Length expect={len(expect)} result={len(result)}")
        for i, (exp, res) in enumerate(zip(expect, result)):
            self.assertEqual(f"{label} value[{i}]", exp, res)

    # Class Methods End
