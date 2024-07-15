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
        assert s.encode1("Heggenburger") == "H251"
        assert s.encode1("Blackman") == "B425"
        assert s.encode1("Schmidt") == "S530"
        assert s.encode1("Lippmann") == "L150"
        assert (
            s.encode1("Dodds") == "D200"
        )  # 'o' is not a separator here - it is silent
        assert s.encode1("Dhdds") == "D200"  # 'h' is silent
        assert s.encode1("Dwdds") == "D200"  # 'w' is silent

    def testWikipediaAmericanSoundex(self) -> None:

        soundex = Soundex()

        self.assertEqual("R163", soundex.encode1("Robert"))
        self.assertEqual("R163", soundex.encode1("Rupert"))
        self.assertEqual("A261", soundex.encode1("Ashcraft"))
        self.assertEqual("A261", soundex.encode1("Ashcroft"))
        self.assertEqual("T522", soundex.encode1("Tymczak"))
        self.assertEqual("P236", soundex.encode1("Pfister"))

    def testUsMappingOWithDiaeresis(self) -> None:

        # Testing the encoding of 'o'
        self.assertEqual("O000", self.getStringEncoder().encode1("o"))

        # Testing the encoding of '�'
        if unicodedata.name("\u00f6").startswith("LATIN SMALL LETTER O WITH DIAERESIS"):
            try:
                self.assertEqual("\u00d6000", self.getStringEncoder().encode1("\u00f6"))
                self.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            self.assertEqual("", self.getStringEncoder().encode1("\u00f6"))

    def testUsMappingEWithAcute(self) -> None:

        from unidecode import unidecode

        assert self.getStringEncoder().encode1("e") == "E000"

        if unidecode("é") == "e":  # e-acute
            try:
                assert self.getStringEncoder().encode1("é") == "E000"
                pytest.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            assert self.getStringEncoder().encode1("é") == ""

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

        self.assertEquals(
            "W452",
            Soundex(1, False, Soundex.US_ENGLISH_MAPPING_STRING, None).soundex(
                "Williams"
            ),
        )

    def testNewInstance2(self) -> None:

        self.assertEqual(
            "W452",
            Soundex(2, False, None, list(Soundex.US_ENGLISH_MAPPING_STRING)).soundex(
                "Williams"
            ),
        )

    def testNewInstance(self) -> None:

        soundex = Soundex(3, False, None, None)
        self.assertEqual("W452", soundex.soundex("Williams"))

    def testMsSqlServer3(self) -> None:

        soundex = Soundex()

        self.assertEqual("A500", soundex.encode1("Ann"))
        self.assertEqual("A536", soundex.encode1("Andrew"))
        self.assertEqual("J530", soundex.encode1("Janet"))
        self.assertEqual("M626", soundex.encode1("Margaret"))
        self.assertEqual("S315", soundex.encode1("Steven"))
        self.assertEqual("M240", soundex.encode1("Michael"))
        self.assertEqual("R163", soundex.encode1("Robert"))
        self.assertEqual("L600", soundex.encode1("Laura"))
        self.assertEqual("A500", soundex.encode1("Anne"))

    def testMsSqlServer2(self) -> None:

        self.checkEncodingVariations(
            "E625",
            ["Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"],
        )

    def testMsSqlServer1(self) -> None:

        soundex = Soundex()

        self.assertEqual("S530", soundex.encode1("Smith"))
        self.assertEqual("S530", soundex.encode1("Smythe"))

    def testHWRuleEx3(self) -> None:

        soundex = Soundex()
        self.assertEqual("S460", soundex.encode1("Sgler"))
        self.assertEqual("S460", soundex.encode1("Swhgler"))

        variations = [
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
        ]

        for variation in variations:
            self.assertEqual("S460", soundex.encode1(variation))

    def testHWRuleEx2(self) -> None:

        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTHDAVIS"))
        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTH-DAVIS"))

    def testHWRuleEx1(self) -> None:

        soundex = Soundex()

        self.assertEqual("A261", soundex.encode1("Ashcraft"))
        self.assertEqual("A261", soundex.encode1("Ashcroft"))
        self.assertEqual("Y330", soundex.encode1("yehudit"))
        self.assertEqual("Y330", soundex.encode1("yhwdyt"))

    def testEncodeIgnoreTrimmable(self) -> None:

        soundex = Soundex()
        result = soundex.encode1(" \t\n\r Washington \t\n\r ")
        self.assertEqual("W252", result)

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

        soundex = Soundex()

        self.assertEqual("H452", soundex.encode1("HOLMES"))
        self.assertEqual("A355", soundex.encode1("ADOMOMI"))
        self.assertEqual("V536", soundex.encode1("VONDERLEHR"))
        self.assertEqual("B400", soundex.encode1("BALL"))
        self.assertEqual("S000", soundex.encode1("SHAW"))
        self.assertEqual("J250", soundex.encode1("JACKSON"))
        self.assertEqual("S545", soundex.encode1("SCANLON"))
        self.assertEqual("S532", soundex.encode1("SAINTJOHN"))

    def testEncodeBatch3(self) -> None:

        soundex = Soundex()

        self.assertEqual("W252", soundex.encode1("Washington"))
        self.assertEqual("L000", soundex.encode1("Lee"))
        self.assertEqual("G362", soundex.encode1("Gutierrez"))
        self.assertEqual("P236", soundex.encode1("Pfister"))
        self.assertEqual("J250", soundex.encode1("Jackson"))
        self.assertEqual("T522", soundex.encode1("Tymczak"))
        self.assertEqual("V532", soundex.encode1("VanDeusen"))

    def testEncodeBatch2(self) -> None:

        soundex = Soundex()

        self.assertEqual("A462", soundex.encode1("Allricht"))
        self.assertEqual("E166", soundex.encode1("Eberhard"))
        self.assertEqual("E521", soundex.encode1("Engebrethson"))
        self.assertEqual("H512", soundex.encode1("Heimbach"))
        self.assertEqual("H524", soundex.encode1("Hanselmann"))
        self.assertEqual("H431", soundex.encode1("Hildebrand"))
        self.assertEqual("K152", soundex.encode1("Kavanagh"))
        self.assertEqual("L530", soundex.encode1("Lind"))
        self.assertEqual("L222", soundex.encode1("Lukaschowsky"))
        self.assertEqual("M235", soundex.encode1("McDonnell"))
        self.assertEqual("M200", soundex.encode1("McGee"))
        self.assertEqual("O155", soundex.encode1("Opnian"))
        self.assertEqual("O155", soundex.encode1("Oppenheimer"))
        self.assertEqual("R355", soundex.encode1("Riedemanas"))
        self.assertEqual("Z300", soundex.encode1("Zita"))
        self.assertEqual("Z325", soundex.encode1("Zitzmeinn"))

    def testEncodeBasic(self) -> None:

        soundex = Soundex()

        self.assertEqual("T235", soundex.encode1("testing"))
        self.assertEqual("T000", soundex.encode1("The"))
        self.assertEqual("Q200", soundex.encode1("quick"))
        self.assertEqual("B650", soundex.encode1("brown"))
        self.assertEqual("F200", soundex.encode1("fox"))
        self.assertEqual("J513", soundex.encode1("jumped"))
        self.assertEqual("O160", soundex.encode1("over"))
        self.assertEqual("T000", soundex.encode1("the"))
        self.assertEqual("L200", soundex.encode1("lazy"))
        self.assertEqual("D200", soundex.encode1("dogs"))

    def testDifference(self) -> None:

        soundex = Soundex()

        self.assertEqual(0, soundex.difference(None, None))
        self.assertEqual(0, soundex.difference("", ""))
        self.assertEqual(0, soundex.difference(" ", " "))
        self.assertEqual(4, soundex.difference("Smith", "Smythe"))
        self.assertEqual(2, soundex.difference("Ann", "Andrew"))
        self.assertEqual(1, soundex.difference("Margaret", "Andrew"))
        self.assertEqual(0, soundex.difference("Janet", "Margaret"))
        self.assertEqual(4, soundex.difference("Green", "Greene"))
        self.assertEqual(0, soundex.difference("Blotchet-Halls", "Greene"))
        self.assertEqual(4, soundex.difference("Smith", "Smythe"))
        self.assertEqual(4, soundex.difference("Smithers", "Smythers"))
        self.assertEqual(2, soundex.difference("Anothers", "Brothers"))

    def testBadCharacters(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the encode1 method with the string "HOL>MES"
        result = soundex.encode1("HOL>MES")

        # Assert that the result is "H452"
        self.assertEqual(result, "H452")

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
