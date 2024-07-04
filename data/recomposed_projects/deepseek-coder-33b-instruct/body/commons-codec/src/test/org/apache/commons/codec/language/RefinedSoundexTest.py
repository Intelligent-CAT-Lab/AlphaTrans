from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.RefinedSoundex import *


class RefinedSoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testNewInstance3(self) -> None:

        self.assertEqual(
            "D6043",
            RefinedSoundex(0, RefinedSoundex.US_ENGLISH_MAPPING_STRING, None).soundex(
                "dogs"
            ),
        )

    def testNewInstance2(self) -> None:

        self.assertEqual(
            "D6043",
            RefinedSoundex(
                1, None, list(RefinedSoundex.US_ENGLISH_MAPPING_STRING)
            ).soundex("dogs"),
        )

    def testNewInstance(self) -> None:

        refined_soundex = RefinedSoundex(2, None, None)
        self.assertEqual("D6043", refined_soundex.soundex("dogs"))

    def testGetMappingCodeNonLetter(self) -> None:

        refined_soundex = RefinedSoundex()
        code = refined_soundex.getMappingCode("#")
        self.assertEqual(code, "0")

    def testEncode(self) -> None:

        self.assertEqual("T6036084", self.getStringEncoder().encode1("testing"))
        self.assertEqual("T6036084", self.getStringEncoder().encode1("TESTING"))
        self.assertEqual("T60", self.getStringEncoder().encode1("The"))
        self.assertEqual("Q503", self.getStringEncoder().encode1("quick"))
        self.assertEqual("B1908", self.getStringEncoder().encode1("brown"))
        self.assertEqual("F205", self.getStringEncoder().encode1("fox"))
        self.assertEqual("J408106", self.getStringEncoder().encode1("jumped"))
        self.assertEqual("O0209", self.getStringEncoder().encode1("over"))
        self.assertEqual("T60", self.getStringEncoder().encode1("the"))
        self.assertEqual("L7050", self.getStringEncoder().encode1("lazy"))
        self.assertEqual("D6043", self.getStringEncoder().encode1("dogs"))

        self.assertEqual("D6043", RefinedSoundex.US_ENGLISH.encode1("dogs"))

    def testDifference(self) -> None:

        refined_soundex = RefinedSoundex()

        self.assertEqual(0, refined_soundex.difference(None, None))
        self.assertEqual(0, refined_soundex.difference("", ""))
        self.assertEqual(0, refined_soundex.difference(" ", " "))
        self.assertEqual(6, refined_soundex.difference("Smith", "Smythe"))
        self.assertEqual(3, refined_soundex.difference("Ann", "Andrew"))
        self.assertEqual(1, refined_soundex.difference("Margaret", "Andrew"))
        self.assertEqual(1, refined_soundex.difference("Janet", "Margaret"))
        self.assertEqual(5, refined_soundex.difference("Green", "Greene"))
        self.assertEqual(1, refined_soundex.difference("Blotchet-Halls", "Greene"))
        self.assertEqual(6, refined_soundex.difference("Smith", "Smythe"))
        self.assertEqual(8, refined_soundex.difference("Smithers", "Smythers"))
        self.assertEqual(5, refined_soundex.difference("Anothers", "Brothers"))

    def _createStringEncoder(self) -> RefinedSoundex:
        return RefinedSoundex(2, None, None)
