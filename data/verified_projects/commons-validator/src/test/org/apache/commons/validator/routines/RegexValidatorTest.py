import pytest

from src.main.org.apache.commons.validator.routines.RegexValidator import *
import unittest
import re


class RegexValidatorTest(unittest.TestCase):

    __REGEX = "^([abc]*)(?:\\-)([DEF]*)(?:\\-)([123]*)$"

    __COMPONENT_1 = "([abc]{3})"
    __COMPONENT_2 = "([DEF]{3})"
    __COMPONENT_3 = "([123]{3})"
    __SEPARATOR_1 = "(?:\\-)"
    __SEPARATOR_2 = "(?:\\s)"
    __REGEX_1 = "^" +\
        __COMPONENT_1 +\
        __SEPARATOR_1 +\
        __COMPONENT_2 +\
        __SEPARATOR_1 +\
        __COMPONENT_3 +\
        "$"
    __REGEX_2 = "^" +\
        __COMPONENT_1 +\
        __SEPARATOR_2 +\
        __COMPONENT_2 +\
        __SEPARATOR_2 +\
        __COMPONENT_3 +\
        "$"
    __REGEX_3 = "^" +\
        __COMPONENT_1 +\
        __COMPONENT_2 +\
        __COMPONENT_3 +\
        "$"
    __MULTIPLE_REGEX = [__REGEX_1, __REGEX_2, __REGEX_3]


    
    def setUp(self) -> None:
        try:
            super().setUp()
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    @pytest.mark.test
    def testSingle(self) -> None:
        sensitive = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX)
        insensitive = RegexValidator.RegexValidator2(RegexValidatorTest.__REGEX, False)

        self.assertEqual(
            True,
            sensitive.isValid("ac-DE-1"),
            "Sensitive isValid() valid"
        )
        self.assertEqual(
            False,
            sensitive.isValid("AB-de-1"),
            "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True,
            insensitive.isValid("AB-de-1"),
            "Insensitive isValid() valid"
        )
        self.assertEqual(
            False,
            insensitive.isValid("ABd-de-1"),
            "Insensitive isValid() invalid"
        )

        self.assertEqual(
            "acDE1",
            sensitive.validate("ac-DE-1"),
            "Sensitive validate() valid"
        )
        self.assertEqual(
            None,
            sensitive.validate("AB-de-1"),
            "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1",
            insensitive.validate("AB-de-1"),
            "Insensitive validate() valid"
        )
        self.assertEqual(
            None,
            insensitive.validate("ABd-de-1"),
            "Insensitive validate() invalid"
        )

        self.__checkArray(
            "Sensitive match() valid",
            ["ac", "DE", "1"],
            sensitive.match("ac-DE-1")
        )
        self.__checkArray(
            "Sensitive match() invalid",
            None,
            sensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() valid",
            ["AB", "de", "1"],
            insensitive.match("AB-de-1"),
        )
        self.__checkArray(
            "Insensitive match() invalid",
            None,
            insensitive.match("ABd-de-1")
        )
        self.assertEqual(
            "ABC",
            RegexValidator.RegexValidator3("^([A-Z]*)$").validate("ABC"),
            "validate one"
        )
        self.__checkArray(
            "match one",
            ["ABC"],
            RegexValidator.RegexValidator3("^([A-Z]*)$").match("ABC")
        )

    
    @pytest.mark.test
    def testMultipleSensitive(self) -> None:
        multiple = RegexValidator.RegexValidator1(RegexValidatorTest.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX_3)

        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(
            True,
            multiple.isValid(value),
            "Sensitive isValid() Multiple"
        )
        self.assertEqual(
            False,
            single1.isValid(value),
            "Sensitive isValid() 1st"
        )
        self.assertEqual(
            True,
            single2.isValid(value),
            "Sensitive isValid() 2nd"
        )
        self.assertEqual(
            False,
            single3.isValid(value),
            "Sensitive isValid() 3rd"
        )

        self.assertEqual(
            expect,
            multiple.validate(value),
            "Sensitive validate() Multiple"
        )
        self.assertEqual(
            None,
            single1.validate(value),
            "Sensitive validate() 1st"
        )
        self.assertEqual(
            expect,
            single2.validate(value),
            "Sensitive validate() 2nd"
        )
        self.assertEqual(
            None,
            single3.validate(value),
            "Sensitive validate() 3rd"
        )

        self.__checkArray(
            "Sensitive match() Multiple",
            array,
            multiple.match(value)
        )
        self.__checkArray(
            "Sensitive match() 1st",
            None,
            single1.match(value)
        )
        self.__checkArray(
            "Sensitive match() 2nd",
            array,
            single2.match(value)
        )
        self.__checkArray(
            "Sensitive match() 3rd",
            None,
            single3.match(value)
        )

        value = "AAC*FDE*321"
        self.assertEqual(
            False,
            multiple.isValid(value),
            "isValid() Invalid"
        )
        self.assertEqual(
            None,
            multiple.validate(value),
            "validate() Invalid"
        )
        self.assertEqual(
            None,
            multiple.match(value),
            "match() Multiple"
        )

    
    @pytest.mark.test
    def testMultipleInsensitive(self) -> None:
        multiple = RegexValidator(RegexValidatorTest.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(RegexValidatorTest.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(RegexValidatorTest.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(RegexValidatorTest.__REGEX_3, False)

        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(
            True,
            multiple.isValid(value),
            "isValid() Multiple"
        )
        self.assertEqual(
            False,
            single1.isValid(value),
            "isValid() 1st"
        )
        self.assertEqual(
            True,
            single2.isValid(value),
            "isValid() 2nd"
        )
        self.assertEqual(
            False,
            single3.isValid(value),
            "isValid() 3rd"
        )

        self.assertEqual(
            expect,
            multiple.validate(value),
            "validate() Multiple"
        )
        self.assertEqual(
            None,
            single1.validate(value),
            "validate() 1st"
        )
        self.assertEqual(
            expect,
            single2.validate(value),
            "validate() 2nd"
        )
        self.assertEqual(
            None,
            single3.validate(value),
            "validate() 3rd"
        )

        self.__checkArray(
            "match() Multiple",
            array,
            multiple.match(value)
        )
        self.__checkArray(
            "match() 1st",
            None,
            single1.match(value),
        )
        self.__checkArray(
            "match() 2nd",
            array,
            single2.match(value)
        )
        self.__checkArray(
            "match() 3rd",
            None,
            single3.match(value)
        )

        value = "AAC*FDE*321"
        self.assertEqual(
            False,
            multiple.isValid(value),
            "isValid() Invalid"
        )
        self.assertEqual(
            None,
            multiple.validate(value),
            "validate() Invalid"
        )
        self.assertEqual(
            None,
            multiple.match(value),
            "match() Multiple"
        )

    
    @pytest.mark.test
    def testNullValue(self) -> None:
        validator = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX)
        self.assertEqual(
            False,
            validator.isValid(None),
            "Instance isValid()"
        )
        self.assertEqual(
            None,
            validator.validate(None),
            "Instance validate()"
        )
        self.assertEqual(
            None,
            validator.match(None),
            "Instance match()"
        )

    
    @pytest.mark.test
    def testMissingRegex(self) -> None:
        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator3(None)
        self.assertEqual(
            "Regular expression[0] is missing",
            str(context.exception),
            "Single Null"
        )

        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator3("")
        self.assertEqual(
            "Regular expression[0] is missing",
            str(context.exception),
            "Single Zero Length"
        )

        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator1(None)
        self.assertEqual(
            "Regular expressions are missing",
            str(context.exception),
            "Null Array"
        )

        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator1([])
        self.assertEqual(
            "Regular expressions are missing",
            str(context.exception),
            "Zero Length Array"
        )

        expressions = ["ABC", None]
        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator1(expressions)
        self.assertEqual(
            "Regular expression[1] is missing",
            str(context.exception),
            "Array has Null"
        )

        expressions = ["", "ABC"]
        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator1(expressions)
        self.assertEqual(
            "Regular expression[0] is missing",
            str(context.exception),
            "Array has Zero Length"
        )

    
    @pytest.mark.test
    def testExceptions(self) -> None:
        invalidRegex = "^([abCD12]*$"
        with self.assertRaises(re.error):
            RegexValidator.RegexValidator3(invalidRegex)

    
    @pytest.mark.test
    def testToString(self) -> None:
        single = RegexValidator.RegexValidator3(RegexValidatorTest.__REGEX)
        self.assertEqual(
            "RegexValidator{" + RegexValidatorTest.__REGEX + "}",
            single.toString(),
            "Single"
        )

        multiple = RegexValidator.RegexValidator1(
            [RegexValidatorTest.__REGEX, RegexValidatorTest.__REGEX]
        )
        self.assertEqual(
            "RegexValidator{" +\
                RegexValidatorTest.__REGEX +\
                "," + RegexValidatorTest.__REGEX +\
                "}",
            multiple.toString(),
            "Multiple"
        )

    
    def __checkArray(self, label, expect, result) -> None:
        if expect is None or result is None:
            if expect is None and result is None:
                return
            else:
                self.fail(
                    label + " Null expect=" + str(expect) + " result=" + str(result)
                )
            return

        if len(expect) != len(result):
            self.fail(
                label + " Length expect=" + str(len(expect)) + " result=" + str(len(result))
            )

        for i in range(len(expect)):
            self.assertEqual(
                expect[i],
                result[i],
                label + " value[" + str(i) + "]"
            )
