from __future__ import annotations
import re
import unittest
import pytest
import io
import os
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Soundex import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class SoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSimplifiedSoundex(self) -> None:

        s = Soundex.US_ENGLISH_SIMPLIFIED

        assert s.encode1("WILLIAMS") == "W452"
        assert s.encode1("BARAGWANATH") == "B625"
        assert s.encode1("DONNELL") == "D540"
        assert s.encode1("LLOYD") == "L300"
        assert s.encode1("WOOLCOCK") == "W422"
        assert s.encode1("Dodds") == "D320"
        assert s.encode1("Dwdds") == "D320"  # w is a separator
        assert s.encode1("Dhdds") == "D320"  # h is a separator

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

        # Asserting the encoding of 'o'
        assert self.getStringEncoder().encode1("o") == "O000"

        # Checking if 'o' with diaeresis is a letter
        if unicodedata.name(chr(246)) == "LATIN SMALL LETTER O WITH DIAERESIS":
            try:
                # Asserting the encoding of 'o' with diaeresis
                assert self.getStringEncoder().encode1(chr(246)) == "Ö000"
                assert False, "Expected ValueError not thrown"
            except ValueError:
                pass
        else:
            # Asserting the encoding of 'o' with diaeresis
            assert self.getStringEncoder().encode1(chr(246)) == ""

    def testUsMappingEWithAcute(self) -> None:

        # Asserting the encoding of 'e'
        self.assertEqual("E000", self.getStringEncoder().encode1("e"))

        # Checking if 'e-acute' is a letter
        if unicodedata.name("\u00e9").startswith("LATIN SMALL LETTER E"):
            try:
                # Asserting the encoding of 'e-acute'
                self.assertEqual("\u00c9000", self.getStringEncoder().encode1("\u00e9"))
                self.fail("Expected ValueError not thrown")
            except ValueError:
                pass
        else:
            # Asserting the encoding of 'e-acute'
            self.assertEqual("", self.getStringEncoder().encode1("\u00e9"))

    def testUsEnglishStatic(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the soundex method on the instance
        result = soundex.soundex("Williams")

        # Assert that the result is as expected
        self.assertEqual("W452", result)

    def testSoundexUtilsNullBehaviour(self) -> None:

        # Testing clean method with null input
        self.assertIsNone(SoundexUtils.clean(None))

        # Testing clean method with empty string input
        self.assertEqual("", SoundexUtils.clean(""))

        # Testing differenceEncoded method with null and empty string input
        self.assertEqual(0, SoundexUtils.differenceEncoded(None, ""))
        self.assertEqual(0, SoundexUtils.differenceEncoded("", None))

    def testSoundexUtilsConstructable(self) -> None:

        # Create an instance of SoundexUtils
        SoundexUtils()

    def testNewInstance3(self) -> None:

        soundex = Soundex(1, False, Soundex.US_ENGLISH_MAPPING_STRING, None)
        result = soundex.soundex("Williams")

        self.assertEqual("W452", result)

    def testNewInstance2(self) -> None:

        # Create a new instance of Soundex
        soundex = Soundex(2, False, None, list(Soundex.US_ENGLISH_MAPPING_STRING))

        # Call the soundex method
        result = soundex.soundex("Williams")

        # Assert the result
        self.assertEqual("W452", result)

    def testNewInstance(self) -> None:

        # Create a new instance of Soundex
        soundex_instance = Soundex(3, False, None, None)

        # Call the soundex method on the instance
        result = soundex_instance.soundex("Williams")

        # Assert that the result is as expected
        self.assertEquals("W452", result)

    def testMsSqlServer3(self) -> None:

        soundex = Soundex()

        assert soundex.encode1("Ann") == "A500"
        assert soundex.encode1("Andrew") == "A536"
        assert soundex.encode1("Janet") == "J530"
        assert soundex.encode1("Margaret") == "M626"
        assert soundex.encode1("Steven") == "S315"
        assert soundex.encode1("Michael") == "M240"
        assert soundex.encode1("Robert") == "R163"
        assert soundex.encode1("Laura") == "L600"
        assert soundex.encode1("Anne") == "A500"

    def testMsSqlServer2(self) -> None:

        self.checkEncodingVariations(
            "E625",
            ["Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"],
        )

    def testMsSqlServer1(self) -> None:

        # Instantiate the Soundex class
        soundex = Soundex()

        # Assert the expected output
        self.assertEqual("S530", soundex.encode1("Smith"))
        self.assertEqual("S530", soundex.encode1("Smythe"))

    def testHWRuleEx3(self) -> None:

        # Testing the encode1 method
        try:
            assert self.getStringEncoder().encode1("Sgler") == "S460"
            assert self.getStringEncoder().encode1("Swhgler") == "S460"
        except EncoderException as e:
            print(f"EncoderException: {e}")

        # Testing the checkEncodingVariations method
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
            try:
                assert self.getStringEncoder().encode1(variation) == "S460"
            except EncoderException as e:
                print(f"EncoderException: {e}")

    def testHWRuleEx2(self) -> None:

        soundex = Soundex()

        self.assertEquals("B312", soundex.encode1("BOOTHDAVIS"))
        self.assertEquals("B312", soundex.encode1("BOOTH-DAVIS"))

    def testHWRuleEx1(self) -> None:

        soundex = Soundex()

        self.assertEqual("A261", soundex.encode1("Ashcraft"))
        self.assertEqual("A261", soundex.encode1("Ashcroft"))
        self.assertEqual("Y330", soundex.encode1("yehudit"))
        self.assertEqual("Y330", soundex.encode1("yhwdyt"))

    def testEncodeIgnoreTrimmable(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the encode1 method with the given string
        result = soundex.encode1(" \t\n\r Washington \t\n\r ")

        # Assert that the result is equal to the expected value
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

        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))
        self.assertEqual("S545", self.getStringEncoder().encode1("SCANLON"))
        self.assertEqual("S532", self.getStringEncoder().encode1("SAINTJOHN"))

    def testEncodeBatch3(self) -> None:

        soundex = Soundex()

        assert soundex.encode1("Washington") == "W252"
        assert soundex.encode1("Lee") == "L000"
        assert soundex.encode1("Gutierrez") == "G362"
        assert soundex.encode1("Pfister") == "P236"
        assert soundex.encode1("Jackson") == "J250"
        assert soundex.encode1("Tymczak") == "T522"
        assert soundex.encode1("VanDeusen") == "V532"

    def testEncodeBatch2(self) -> None:

        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))
        self.assertEqual("Z300", self.getStringEncoder().encode1("Zita"))
        self.assertEqual("Z325", self.getStringEncoder().encode1("Zitzmeinn"))

    def testEncodeBasic(self) -> None:

        soundex = Soundex()

        assert soundex.encode1("testing") == "T235"
        assert soundex.encode1("The") == "T000"
        assert soundex.encode1("quick") == "Q200"
        assert soundex.encode1("brown") == "B650"
        assert soundex.encode1("fox") == "F200"
        assert soundex.encode1("jumped") == "J513"
        assert soundex.encode1("over") == "O160"
        assert soundex.encode1("the") == "T000"
        assert soundex.encode1("lazy") == "L200"
        assert soundex.encode1("dogs") == "D200"

    def testDifference(self) -> None:

        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.assertEqual(4, self.getStringEncoder().difference("Smithers", "Smythers"))
        self.assertEqual(2, self.getStringEncoder().difference("Anothers", "Brothers"))

    def testBadCharacters(self) -> None:

        # Create an instance of the Soundex class
        soundex = Soundex()

        # Call the encode1 method from the Soundex class
        result = soundex.encode1("HOL>MES")

        # Assert that the result is equal to "H452"
        self.assertEqual("H452", result)

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
