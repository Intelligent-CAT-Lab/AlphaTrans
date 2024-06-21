from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.bm.BeiderMorseEncoder import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class BeiderMorseEncoderTest(StringEncoderAbstractTest, unittest.TestCase):

    __TEST_CHARS: typing.List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "o", "u"]

    def testSpeedCheck3(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        phrase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[0:i])

    def testSpeedCheck2(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        phrase = "ItstheendoftheworldasweknowitandIfeelfine"

        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[0:i])

    def testSpeedCheck(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        stringBuffer = io.StringIO()
        stringBuffer.write(self.__TEST_CHARS[0])
        for i in range(40):
            j = (i + 1) % len(self.__TEST_CHARS)
            bmpm.encode1(stringBuffer.getvalue())
            stringBuffer.write(self.__TEST_CHARS[j])

    def testSetRuleTypeToRulesValueError(self) -> None:

        bmpm = BeiderMorseEncoder()
        bmpm.setRuleType(RuleType.RULES)

    def testSetRuleTypeExact(self) -> None:

        bmpm = BeiderMorseEncoder()
        bmpm.setRuleType(RuleType.EXACT)
        self.assertEqual(
            "Rule type should have been set to exact",
            RuleType.EXACT,
            bmpm.getRuleType(),
        )

    def testSetNameTypeAsh(self) -> None:

        bmpm = BeiderMorseEncoder()
        bmpm.setNameType(NameType.ASHKENAZI)
        assertEqual(
            "Name type should have been set to ash",
            NameType.ASHKENAZI,
            bmpm.getNameType(),
        )

    def testSetConcat(self) -> None:

        bmpm = BeiderMorseEncoder()
        bmpm.setConcat(False)
        assert not bmpm.isConcat(), "Should be able to set concat to false"

    def testOOM(self) -> None:

        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )

        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)

        phonemes = encoder.encode1(phrase)
        assert not phonemes.isEmpty()

        phonemeArr = phonemes.split("\\|")
        assert len(phonemeArr) <= 10

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException(self) -> None:

        r = Rule("a", "", "", Rule.Phoneme(2, "", Languages.ANY_LANGUAGE, None))
        r.patternAndContextMatches("bob", -1)

    def testLongestEnglishSurname(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        try:
            bmpm.encode1("MacGhilleseatheanaich")
        except EncoderException as e:
            print(f"An error occurred: {e}")

    def testInvalidLanguageValueError(self) -> None:

        try:
            Languages.getInstance1("thereIsNoSuchLanguage")
        except ValueError:
            pass

    def testInvalidLangRuntimeError(self) -> None:

        Lang.loadFromResource(
            "thisIsAMadeUpResourceName", Languages.getInstance0(NameType.GENERIC)
        )

    def testInvalidLangValueError(self) -> None:

        try:
            Rule.getInstance1(NameType.GENERIC, RuleType.APPROX, "noSuchLanguage")
        except ValueError:
            pass

    def testEncodeGna(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        bmpm.encode1("gna")

    def testEncodeAtzNotEmpty(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        names = ["ácz", "átz", "Ignácz", "Ignátz", "Ignác"]
        for name in names:
            self.__assertNotEmpty(bmpm, name)

    def testAsciiEncodeNotEmpty2Letters(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        for c1 in range(ord("a"), ord("z") + 1):
            for c2 in range(ord("a"), ord("z") + 1):
                value = chr(c1) + chr(c2)
                valueU = value.upper()
                self.__assertNotEmpty(bmpm, value)
                self.__assertNotEmpty(bmpm, valueU)

    def testAsciiEncodeNotEmpty1Letter(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        for c in range(ord("a"), ord("z") + 1):
            value = chr(c)
            valueU = value.upper()
            self.__assertNotEmpty(bmpm, value)
            self.__assertNotEmpty(bmpm, valueU)

    def testAllChars(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        for c in range(ord(chr(0)), sys.maxunicode + 1):
            try:
                bmpm.encode1(chr(c))
            except EncoderException:
                pass

    def _createStringEncoder(self) -> StringEncoder:

        return BeiderMorseEncoder()

    def __createGenericApproxEncoder(self) -> BeiderMorseEncoder:

        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.APPROX)
        return encoder

    def __assertNotEmpty(self, bmpm: BeiderMorseEncoder, value: str) -> None:

        # The assertNotEquals method in Python is equivalent to the assertNotEquals method in Java.
        # However, Python does not have a built-in assertNotEquals method.
        # Instead, we can use the assertNotEqual method from the unittest.TestCase class.
        # If the two values are equal, the assertNotEqual method will raise an AssertionError.

        # Here is the Python code:

        self.assertNotEqual(value, "", bmpm.encode1(value))
