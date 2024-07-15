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

        soundex = Soundex()

        self.assertEqual("R163", soundex.encode1("Robert"))
        self.assertEqual("R163", soundex.encode1("Rupert"))
        self.assertEqual("A261", soundex.encode1("Ashcraft"))
        self.assertEqual("A261", soundex.encode1("Ashcroft"))
        self.assertEqual("T522", soundex.encode1("Tymczak"))
        self.assertEqual("P236", soundex.encode1("Pfister"))

    def testUsMappingOWithDiaeresis(self) -> None:

        # Testing the encoding of 'o'
        self.assertEqual("O000", self._stringEncoder.encode1("o"))

        # Checking if 'o' with diaeresis is a letter
        if unicodedata.name(chr(0x00F6)).startswith("LATIN"):
            try:
                # Testing the encoding of 'o' with diaeresis
                self.assertEqual("\u00d6000", self._stringEncoder.encode1("\u00f6"))
                self.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            # Testing the encoding of 'o' with diaeresis when it's not a letter
            self.assertEqual("", self._stringEncoder.encode1("\u00f6"))

    def testUsMappingEWithAcute(self) -> None:

        # Testing the encoding of 'e'
        self.assertEqual("E000", self._stringEncoder.encode1("e"))

        # Testing the encoding of 'é'
        if unicodedata.name("\u00e9").startswith("LATIN SMALL LETTER E"):
            try:
                self.assertEqual("\u00c9000", self._stringEncoder.encode1("\u00e9"))
                self.fail("Expected ValueError not thrown")
            except EncoderException:
                pass
        else:
            self.assertEqual("", self._stringEncoder.encode1("\u00e9"))

    def testUsEnglishStatic(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the soundex method and compare the result with the expected result
        self.assertEqual("W452", soundex.soundex("Williams"))

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
            Soundex(2, False, None, list(Soundex.US_ENGLISH_MAPPING_STRING)).soundex(
                "Williams"
            ),
        )

    def testNewInstance(self) -> None:

        # Create an instance of Soundex with the parameters provided in the Java code
        soundex = Soundex(3, False, None, None)

        # Assert that the soundex method returns the expected result
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

        expected = "E625"
        variations = [
            "Erickson",
            "Erickson",
            "Erikson",
            "Ericson",
            "Ericksen",
            "Ericsen",
        ]

        for variation in variations:
            encoded = self._stringEncoder.encode(variation)
            self.assertEqual(encoded, expected)

    def testMsSqlServer1(self) -> None:

        soundex = Soundex()

        self.assertEqual("S530", soundex.encode1("Smith"))
        self.assertEqual("S530", soundex.encode1("Smythe"))

    def testHWRuleEx3(self) -> None:

        self.assertEqual(self.getStringEncoder().encode1("Sgler"), "S460")
        self.assertEqual(self.getStringEncoder().encode1("Swhgler"), "S460")

        variations = [
            "SAILOR",
            "SALYER",
            "SAYLER",
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
            self.assertEqual(self.getStringEncoder().encode1(variation), "S460")

    def testHWRuleEx2(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Assert that the encode1 method returns the expected result
        self.assertEqual("B312", soundex.encode1("BOOTHDAVIS"))
        self.assertEqual("B312", soundex.encode1("BOOTH-DAVIS"))

    def testHWRuleEx1(self) -> None:

        self.assertEqual(self._stringEncoder.encode1("Ashcraft"), "A261")
        self.assertEqual(self._stringEncoder.encode1("Ashcroft"), "A261")
        self.assertEqual(self._stringEncoder.encode1("yehudit"), "Y330")
        self.assertEqual(self._stringEncoder.encode1("yhwdyt"), "Y330")

    def testEncodeIgnoreTrimmable(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the encode1 method with the given string
        result = soundex.encode1(" \t\n\r Washington \t\n\r ")

        # Assert that the result is as expected
        self.assertEqual("W252", result)

    def testEncodeIgnoreHyphens(self) -> None:

        expected = "K525"
        variations = [
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
        ]

        for variation in variations:
            result = self._stringEncoder.encode(variation)
            self.assertEqual(expected, result)

    def testEncodeIgnoreApostrophes(self) -> None:

        expected = "O165"
        variations = [
            "OBrien",
            "'OBrien",
            "O'Brien",
            "OB'rien",
            "OBr'ien",
            "OBri'en",
            "OBrie'n",
            "OBrien'",
        ]

        for variation in variations:
            result = self._stringEncoder.encode(variation)
            self.assertEqual(expected, result)

    def testEncodeBatch4(self) -> None:

        self.assertEqual(self._stringEncoder.encode1("HOLMES"), "H452")
        self.assertEqual(self._stringEncoder.encode1("ADOMOMI"), "A355")
        self.assertEqual(self._stringEncoder.encode1("VONDERLEHR"), "V536")
        self.assertEqual(self._stringEncoder.encode1("BALL"), "B400")
        self.assertEqual(self._stringEncoder.encode1("SHAW"), "S000")
        self.assertEqual(self._stringEncoder.encode1("JACKSON"), "J250")
        self.assertEqual(self._stringEncoder.encode1("SCANLON"), "S545")
        self.assertEqual(self._stringEncoder.encode1("SAINTJOHN"), "S532")

    def testEncodeBatch3(self) -> None:

        self.assertEqual(self.getStringEncoder().encode1("Washington"), "W252")
        self.assertEqual(self.getStringEncoder().encode1("Lee"), "L000")
        self.assertEqual(self.getStringEncoder().encode1("Gutierrez"), "G362")
        self.assertEqual(self.getStringEncoder().encode1("Pfister"), "P236")
        self.assertEqual(self.getStringEncoder().encode1("Jackson"), "J250")
        self.assertEqual(self.getStringEncoder().encode1("Tymczak"), "T522")
        self.assertEqual(self.getStringEncoder().encode1("VanDeusen"), "V532")

    def testEncodeBatch2(self) -> None:

        self.assertEqual(self.getStringEncoder().encode1("Allricht"), "A462")
        self.assertEqual(self.getStringEncoder().encode1("Eberhard"), "E166")
        self.assertEqual(self.getStringEncoder().encode1("Engebrethson"), "E521")
        self.assertEqual(self.getStringEncoder().encode1("Heimbach"), "H512")
        self.assertEqual(self.getStringEncoder().encode1("Hanselmann"), "H524")
        self.assertEqual(self.getStringEncoder().encode1("Hildebrand"), "H431")
        self.assertEqual(self.getStringEncoder().encode1("Kavanagh"), "K152")
        self.assertEqual(self.getStringEncoder().encode1("Lind"), "L530")
        self.assertEqual(self.getStringEncoder().encode1("Lukaschowsky"), "L222")
        self.assertEqual(self.getStringEncoder().encode1("McDonnell"), "M235")
        self.assertEqual(self.getStringEncoder().encode1("McGee"), "M200")
        self.assertEqual(self.getStringEncoder().encode1("Opnian"), "O155")
        self.assertEqual(self.getStringEncoder().encode1("Oppenheimer"), "O155")
        self.assertEqual(self.getStringEncoder().encode1("Riedemanas"), "R355")
        self.assertEqual(self.getStringEncoder().encode1("Zita"), "Z300")
        self.assertEqual(self.getStringEncoder().encode1("Zitzmeinn"), "Z325")

    def testEncodeBasic(self) -> None:

        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))
        self.assertEqual("L200", self.getStringEncoder().encode1("lazy"))
        self.assertEqual("D200", self.getStringEncoder().encode1("dogs"))

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

        # Assuming that the method getStringEncoder() is defined in the parent class
        # and it returns an instance of StringEncoder
        self.assertEqual("H452", self.getStringEncoder().encode1("HOL>MES"))

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
