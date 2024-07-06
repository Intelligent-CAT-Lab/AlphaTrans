from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Soundex import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class SoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSimplifiedSoundex(self) -> None:
        s = Soundex.US_ENGLISH_SIMPLIFIED
        self.assertEqual("W452", s.encode1("WILLIAMS"))
        self.assertEqual("B625", s.encode1("BARAGWANATH"))
        self.assertEqual("D540", s.encode1("DONNELL"))
        self.assertEqual("L300", s.encode1("LLOYD"))
        self.assertEqual("W422", s.encode1("WOOLCOCK"))
        self.assertEqual("D320", s.encode1("Dodds"))
        self.assertEqual("D320", s.encode1("Dwdds"))  # w is a separator
        self.assertEqual("D320", s.encode1("Dhdds"))  # h is a separator

    def testGenealogy(self) -> None:
        s = Soundex.US_ENGLISH_GENEALOGY
        self.assertEqual("H251", s.encode1("Heggenburger"))
        self.assertEqual("B425", s.encode1("Blackman"))
        self.assertEqual("S530", s.encode1("Schmidt"))
        self.assertEqual("L150", s.encode1("Lippmann"))
        self.assertEqual(
            "D200", s.encode1("Dodds")
        )  # 'o' is not a separator here - it is silent
        self.assertEqual("D200", s.encode1("Dhdds"))  # 'h' is silent
        self.assertEqual("D200", s.encode1("Dwdds"))  # 'w' is silent

    def testWikipediaAmericanSoundex(self) -> None:
        self.assertEqual("R163", self._stringEncoder.encode1("Robert"))
        self.assertEqual("R163", self._stringEncoder.encode1("Rupert"))
        self.assertEqual("A261", self._stringEncoder.encode1("Ashcraft"))
        self.assertEqual("A261", self._stringEncoder.encode1("Ashcroft"))
        self.assertEqual("T522", self._stringEncoder.encode1("Tymczak"))
        self.assertEqual("P236", self._stringEncoder.encode1("Pfister"))

    def testUsMappingOWithDiaeresis(self) -> None:
        self.assertEqual("O000", self._stringEncoder.encode1("o"))
        if chr(0x00F6).isalpha():  # o-umlaut
            try:
                self.assertEqual("\u00d6000", self._stringEncoder.encode1("\u00f6"))
                self.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            self.assertEqual("", self._stringEncoder.encode1("\u00f6"))

    def testUsMappingEWithAcute(self) -> None:
        self.assertEqual("E000", self._stringEncoder.encode1("e"))
        if chr(0x00E9).isalpha():  # e-acute
            try:
                self.assertEqual("\u00c9000", self._stringEncoder.encode1("\u00e9"))
                self.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            self.assertEqual("", self._stringEncoder.encode1("\u00e9"))

    def testUsEnglishStatic(self) -> None:
        self.assertEqual("W452", Soundex.US_ENGLISH.soundex("Williams"))

    def testSoundexUtilsNullBehaviour(self) -> None:
        self.assertIsNone(SoundexUtils.clean(None))
        self.assertEqual("", SoundexUtils.clean(""))
        self.assertEqual(0, SoundexUtils.differenceEncoded(None, ""))
        self.assertEqual(0, SoundexUtils.differenceEncoded("", None))

    def testSoundexUtilsConstructable(self) -> None:
        SoundexUtils()

    def testNewInstance3(self) -> None:
        self.assertEqual(
            "W452",
            Soundex(1, False, Soundex.US_ENGLISH_MAPPING_STRING, None).soundex(
                "Williams"
            ),
        )

    def testNewInstance2(self) -> None:
        self.assertEqual(
            "W452",
            Soundex(2, False, None, Soundex.US_ENGLISH_MAPPING_STRING).soundex(
                "Williams"
            ),
        )

    def testNewInstance(self) -> None:
        self.assertEqual("W452", Soundex(3, False, None, None).soundex("Williams"))

    def testMsSqlServer3(self) -> None:
        self.assertEqual("A500", self._stringEncoder.encode1("Ann"))
        self.assertEqual("A536", self._stringEncoder.encode1("Andrew"))
        self.assertEqual("J530", self._stringEncoder.encode1("Janet"))
        self.assertEqual("M626", self._stringEncoder.encode1("Margaret"))
        self.assertEqual("S315", self._stringEncoder.encode1("Steven"))
        self.assertEqual("M240", self._stringEncoder.encode1("Michael"))
        self.assertEqual("R163", self._stringEncoder.encode1("Robert"))
        self.assertEqual("L600", self._stringEncoder.encode1("Laura"))
        self.assertEqual("A500", self._stringEncoder.encode1("Anne"))

    def testMsSqlServer2(self) -> None:
        self.checkEncodingVariations(
            "E625",
            ["Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"],
        )

    def testMsSqlServer1(self) -> None:
        self.assertEqual("S530", self._stringEncoder.encode1("Smith"))
        self.assertEqual("S530", self._stringEncoder.encode1("Smythe"))

    def testHWRuleEx3(self) -> None:
        self.assertEqual("S460", self._stringEncoder.encode1("Sgler"))
        self.assertEqual("S460", self._stringEncoder.encode1("Swhgler"))
        self.checkEncodingVariations(
            "S460",
            [
                "SAILOR",
                "SALYER",
                "SAYLOR",
                "SCHALLER",
                "SCHELLER",
                "SCHILLER",
                "SCHOOLER",
                "SCHULER",
                "SCHUYLER",
                "SEILER",
                "SEYLER",
                "SHOLAR",
                "SHULER",
                "SILAR",
                "SILER",
                "SILLER",
            ],
        )

    def testHWRuleEx2(self) -> None:
        self.assertEqual("B312", self._stringEncoder.encode1("BOOTHDAVIS"))
        self.assertEqual("B312", self._stringEncoder.encode1("BOOTH-DAVIS"))

    def testHWRuleEx1(self) -> None:
        self.assertEqual("A261", self._stringEncoder.encode1("Ashcraft"))
        self.assertEqual("A261", self._stringEncoder.encode1("Ashcroft"))
        self.assertEqual("Y330", self._stringEncoder.encode1("yehudit"))
        self.assertEqual("Y330", self._stringEncoder.encode1("yhwdyt"))

    def testEncodeIgnoreTrimmable(self) -> None:
        self.assertEqual(
            "W252", self._stringEncoder.encode1(" \t\n\r Washington \t\n\r ")
        )

    def testEncodeIgnoreHyphens(self) -> None:
        self.checkEncodingVariations(
            "K525",
            [
                "KINGSMITH",
                "-KINGSMITH",
                "K-INGSMITH",
                "KI-NGSMITH",
                "KIN-GSMITH",
                "KING-SMITH",
                "KINGS-MITH",
                "KINGSM-ITH",
                "KINGSMI-TH",
                "KINGSMIT-H",
                "KINGSMITH-",
            ],
        )

    def testEncodeIgnoreApostrophes(self) -> None:
        self.checkEncodingVariations(
            "O165",
            [
                "OBrien",
                "'OBrien",
                "O'Brien",
                "OB'rien",
                "OBr'ien",
                "OBri'en",
                "OBrie'n",
                "OBrien'",
            ],
        )

    def testEncodeBatch4(self) -> None:
        self.assertEqual("H452", self._stringEncoder.encode1("HOLMES"))
        self.assertEqual("A355", self._stringEncoder.encode1("ADOMOMI"))
        self.assertEqual("V536", self._stringEncoder.encode1("VONDERLEHR"))
        self.assertEqual("B400", self._stringEncoder.encode1("BALL"))
        self.assertEqual("S000", self._stringEncoder.encode1("SHAW"))
        self.assertEqual("J250", self._stringEncoder.encode1("JACKSON"))
        self.assertEqual("S545", self._stringEncoder.encode1("SCANLON"))
        self.assertEqual("S532", self._stringEncoder.encode1("SAINTJOHN"))

    def testEncodeBatch3(self) -> None:
        self.assertEqual("W252", self._stringEncoder.encode1("Washington"))
        self.assertEqual("L000", self._stringEncoder.encode1("Lee"))
        self.assertEqual("G362", self._stringEncoder.encode1("Gutierrez"))
        self.assertEqual("P236", self._stringEncoder.encode1("Pfister"))
        self.assertEqual("J250", self._stringEncoder.encode1("Jackson"))
        self.assertEqual("T522", self._stringEncoder.encode1("Tymczak"))
        self.assertEqual("V532", self._stringEncoder.encode1("VanDeusen"))

    def testEncodeBatch2(self) -> None:
        self.assertEqual("A462", self._stringEncoder.encode1("Allricht"))
        self.assertEqual("E166", self._stringEncoder.encode1("Eberhard"))
        self.assertEqual("E521", self._stringEncoder.encode1("Engebrethson"))
        self.assertEqual("H512", self._stringEncoder.encode1("Heimbach"))
        self.assertEqual("H524", self._stringEncoder.encode1("Hanselmann"))
        self.assertEqual("H431", self._stringEncoder.encode1("Hildebrand"))
        self.assertEqual("K152", self._stringEncoder.encode1("Kavanagh"))
        self.assertEqual("L530", self._stringEncoder.encode1("Lind"))
        self.assertEqual("L222", self._stringEncoder.encode1("Lukaschowsky"))
        self.assertEqual("M235", self._stringEncoder.encode1("McDonnell"))
        self.assertEqual("M200", self._stringEncoder.encode1("McGee"))
        self.assertEqual("O155", self._stringEncoder.encode1("Opnian"))
        self.assertEqual("O155", self._stringEncoder.encode1("Oppenheimer"))
        self.assertEqual("R355", self._stringEncoder.encode1("Riedemanas"))
        self.assertEqual("Z300", self._stringEncoder.encode1("Zita"))
        self.assertEqual("Z325", self._stringEncoder.encode1("Zitzmeinn"))

    def testEncodeBasic(self) -> None:
        self.assertEqual("T235", self._stringEncoder.encode1("testing"))
        self.assertEqual("T000", self._stringEncoder.encode1("The"))
        self.assertEqual("Q200", self._stringEncoder.encode1("quick"))
        self.assertEqual("B650", self._stringEncoder.encode1("brown"))
        self.assertEqual("F200", self._stringEncoder.encode1("fox"))
        self.assertEqual("J513", self._stringEncoder.encode1("jumped"))
        self.assertEqual("O160", self._stringEncoder.encode1("over"))
        self.assertEqual("T000", self._stringEncoder.encode1("the"))
        self.assertEqual("L200", self._stringEncoder.encode1("lazy"))
        self.assertEqual("D200", self._stringEncoder.encode1("dogs"))

    def testDifference(self) -> None:
        self.assertEqual(0, self._stringEncoder.difference(None, None))
        self.assertEqual(0, self._stringEncoder.difference("", ""))
        self.assertEqual(0, self._stringEncoder.difference(" ", " "))
        self.assertEqual(4, self._stringEncoder.difference("Smith", "Smythe"))
        self.assertEqual(2, self._stringEncoder.difference("Ann", "Andrew"))
        self.assertEqual(1, self._stringEncoder.difference("Margaret", "Andrew"))
        self.assertEqual(0, self._stringEncoder.difference("Janet", "Margaret"))
        self.assertEqual(4, self._stringEncoder.difference("Green", "Greene"))
        self.assertEqual(0, self._stringEncoder.difference("Blotchet-Halls", "Greene"))
        self.assertEqual(4, self._stringEncoder.difference("Smith", "Smythe"))
        self.assertEqual(4, self._stringEncoder.difference("Smithers", "Smythers"))
        self.assertEqual(2, self._stringEncoder.difference("Anothers", "Brothers"))

    def testBadCharacters(self) -> None:
        self.assertEqual("H452", self._stringEncoder.encode1("HOL>MES"))

    def testB650(self) -> None:
        self.checkEncodingVariations(
            "B650",
            [
                "BARHAM",
                "BARONE",
                "BARRON",
                "BERNA",
                "BIRNEY",
                "BIRNIE",
                "BOOROM",
                "BOREN",
                "BORN",
                "BOURN",
                "BOURNE",
                "BOWRON",
                "BRAIN",
                "BRAME",
                "BRANN",
                "BRAUN",
                "BREEN",
                "BRIEN",
                "BRIM",
                "BRIMM",
                "BRINN",
                "BRION",
                "BROOM",
                "BROOME",
                "BROWN",
                "BROWNE",
                "BRUEN",
                "BRUHN",
                "BRUIN",
                "BRUMM",
                "BRUN",
                "BRUNO",
                "BRYAN",
                "BURIAN",
                "BURN",
                "BURNEY",
                "BYRAM",
                "BYRNE",
                "BYRON",
                "BYRUM",
            ],
        )

    def _createStringEncoder(self) -> Soundex:
        return Soundex(3, False, None, None)
