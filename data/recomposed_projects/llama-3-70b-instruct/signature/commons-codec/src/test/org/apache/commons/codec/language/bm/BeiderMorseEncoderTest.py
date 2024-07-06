from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
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
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        phrase: str = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[0:i])

    def testSpeedCheck2(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        phrase: str = "ItstheendoftheworldasweknowitandIfeelfine"

        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[0:i])

    def testSpeedCheck(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        stringBuffer: StringBuilder = StringBuilder()
        stringBuffer.append(self.__TEST_CHARS[0])
        for i in range(0, 40):
            j: int = i + 1
            if j == len(self.__TEST_CHARS):
                j = 0
            bmpm.encode1(stringBuffer.toString())
            stringBuffer.append(self.__TEST_CHARS[j])

    def testSetRuleTypeToRulesValueError(self) -> None:
        bmpm = BeiderMorseEncoder()
        with self.assertRaises(ValueError):
            bmpm.setRuleType(RuleType.RULES)

    def testSetRuleTypeExact(self) -> None:
        bmpm: BeiderMorseEncoder = BeiderMorseEncoder()
        bmpm.setRuleType(RuleType.EXACT)
        self.assertEqual(
            "Rule type should have been set to exact",
            RuleType.EXACT,
            bmpm.getRuleType(),
        )

    def testSetNameTypeAsh(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setNameType(NameType.ASHKENAZI)
        self.assertEqual(
            "Name type should have been set to ash",
            NameType.ASHKENAZI,
            bmpm.getNameType(),
        )

    def testSetConcat(self) -> None:
        bmpm: BeiderMorseEncoder = BeiderMorseEncoder()
        bmpm.setConcat(False)
        self.assertFalse("Should be able to set concat to false", bmpm.isConcat())

    def testOOM(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)
        phonemes = encoder.encode1(phrase)
        self.assertFalse(phonemes.isEmpty())
        phonemeArr = phonemes.split("|")
        self.assertTrue(phonemeArr.length <= 10)

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException(self) -> None:
        r = Rule("a", "", "", Phoneme(2, "", Languages.ANY_LANGUAGE, None))
        r.patternAndContextMatches("bob", -1)

    def testLongestEnglishSurname(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        bmpm.encode1("MacGhilleseatheanaich")

    def testInvalidLanguageValueError(self) -> None:
        with self.assertRaises(ValueError):
            Languages.getInstance1("thereIsNoSuchLanguage")

    def testInvalidLangRuntimeError(self) -> None:
        with self.assertRaises(ValueError):
            Lang.loadFromResource(
                "thisIsAMadeUpResourceName", Languages.getInstance0(NameType.GENERIC)
            )

    def testInvalidLangValueError(self) -> None:
        with self.assertRaises(ValueError):
            Rule.getInstance1(NameType.GENERIC, RuleType.APPROX, "noSuchLanguage")

    def testEncodeGna(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        bmpm.encode1("gna")

    def testEncodeAtzNotEmpty(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        names: List[str] = [
            "\u00e1cz",
            "\u00e1tz",
            "Ign\u00e1cz",
            "Ign\u00e1tz",
            "Ign\u00e1c",
        ]
        for name in names:
            self.__assertNotEmpty(bmpm, name)

    def testAsciiEncodeNotEmpty2Letters(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        for c1 in range(ord("a"), ord("z") + 1):
            for c2 in range(ord("a"), ord("z") + 1):
                value: str = chr(c1) + chr(c2)
                valueU: str = value.upper()
                self.__assertNotEmpty(bmpm, value)
                self.__assertNotEmpty(bmpm, valueU)

    def testAsciiEncodeNotEmpty1Letter(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        for c in range(ord("a"), ord("z") + 1):
            value: str = chr(c)
            valueU: str = value.upper()
            self.__assertNotEmpty(bmpm, value)
            self.__assertNotEmpty(bmpm, valueU)

    def testAllChars(self) -> None:
        bmpm: BeiderMorseEncoder = self.__createGenericApproxEncoder()
        for c in range(Character.MIN_VALUE, Character.MAX_VALUE):
            bmpm.encode1(Character.toString(c))

    def _createStringEncoder(self) -> StringEncoder:
        return BeiderMorseEncoder()

    def __createGenericApproxEncoder(self) -> BeiderMorseEncoder:
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.APPROX)
        return encoder

    def __assertNotEmpty(self, bmpm: BeiderMorseEncoder, value: str) -> None:
        assert value != "", bmpm.encode1(value)
