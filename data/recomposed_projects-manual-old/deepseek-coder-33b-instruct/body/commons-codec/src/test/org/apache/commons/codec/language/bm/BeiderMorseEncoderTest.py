from __future__ import annotations
import re
import sys
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

    __TEST_CHARS: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "o", "u"]

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
        stringBuffer = [self.__TEST_CHARS[0]]
        for i in range(40):
            j = (i + 1) % len(self.__TEST_CHARS)
            bmpm.encode1("".join(stringBuffer))
            stringBuffer.append(self.__TEST_CHARS[j])

    def testSetRuleTypeToRulesValueError(self) -> None:

        bmpm = BeiderMorseEncoder()

        with pytest.raises(ValueError):
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
        self.assertEqual(
            "Name type should have been set to ash",
            NameType.ASHKENAZI,
            bmpm.getNameType(),
        )

    def testSetConcat(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setConcat(False)
        self.assertFalse(bmpm.isConcat(), "Should be able to set concat to false")

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
        self.assertFalse(phonemes == "" or phonemes is None)

        phonemeArr = phonemes.split("|")
        self.assertTrue(len(phonemeArr) <= 10)

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException(self) -> None:

        r = Rule("a", "", "", Phoneme(2, "", Languages.ANY_LANGUAGE, None))
        with pytest.raises(IndexError):
            r.patternAndContextMatches("bob", -1)

    def testLongestEnglishSurname(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        bmpm.encode1("MacGhilleseatheanaich")

    def testInvalidLanguageValueError(self) -> None:

        with pytest.raises(ValueError):
            Languages.getInstance1("thereIsNoSuchLanguage")

    def testInvalidLangRuntimeError(self) -> None:

        with pytest.raises(ValueError):
            Lang.loadFromResource(
                "thisIsAMadeUpResourceName", Languages.getInstance0(NameType.GENERIC)
            )

    def testInvalidLangValueError(self) -> None:
        with pytest.raises(ValueError):
            Rule.getInstance1(NameType.GENERIC, RuleType.APPROX, "noSuchLanguage")

    def testEncodeGna(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        try:
            bmpm.encode1("gna")
        except EncoderException as e:
            pytest.fail("Unexpected EncoderException: " + str(e))

    def testEncodeAtzNotEmpty(self) -> None:

        bmpm = self.__createGenericApproxEncoder()
        names = ["\u00e1cz", "\u00e1tz", "Ign\u00e1cz", "Ign\u00e1tz", "Ign\u00e1c"]
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
        for c in range(0, sys.maxunicode + 1):
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

        if bmpm.encode1(value) == "":
            raise EncoderException("The encoded value is empty")
