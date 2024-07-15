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
from src.main.org.apache.commons.codec.language.DaitchMokotoffSoundex import *


class DaitchMokotoffSoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSpecialRomanianCharacters(self) -> None:

        # The soundex method is not defined in the provided Python code, so I'll assume it's defined elsewhere
        # and I'll use the Python built-in function `self.assertEqual` to compare the expected and actual results
        self.assertEqual(self.__soundex("ţamas"), "364000|464000")  # t-cedilla
        self.assertEqual(self.__soundex("țamas"), "364000|464000")  # t-comma

    def testSoundexBasic3(self) -> None:

        self.assertEqual("734000|739400", self.__soundex("Peters"))
        self.assertEqual("734600|739460", self.__soundex("Peterson"))
        self.assertEqual("645740", self.__soundex("Moskowitz"))
        self.assertEqual("645740", self.__soundex("Moskovitz"))
        self.assertEqual("154600|145460|454600|445460", self.__soundex("Jackson"))
        self.assertEqual(
            "154654|154645|154644|145465|145464|454654|454645|454644|445465|445464",
            self.__soundex("Jackson-Jackson"),
        )

    def testSoundexBasic2(self) -> None:

        self.assertEqual("467000|567000", self.__soundex("Ceniow"))
        self.assertEqual("467000", self.__soundex("Tsenyuv"))
        self.assertEqual("587400|587500", self.__soundex("Holubica"))
        self.assertEqual("587400", self.__soundex("Golubitsa"))
        self.assertEqual("746480|794648", self.__soundex("Przemysl"))
        self.assertEqual("746480", self.__soundex("Pshemeshil"))
        self.assertEqual(
            "944744|944745|944754|944755|945744|945745|945754|945755",
            self.__soundex("Rosochowaciec"),
        )
        self.assertEqual("945744", self.__soundex("Rosokhovatsets"))

    def testSoundexBasic(self) -> None:

        self.assertEqual("583600", self.__soundex("GOLDEN"))
        self.assertEqual("087930", self.__soundex("Alpert"))
        self.assertEqual("791900", self.__soundex("Breuer"))
        self.assertEqual("579000", self.__soundex("Haber"))
        self.assertEqual("665600", self.__soundex("Mannheim"))
        self.assertEqual("664000", self.__soundex("Mintz"))
        self.assertEqual("370000", self.__soundex("Topf"))
        self.assertEqual("586660", self.__soundex("Kleinmann"))
        self.assertEqual("769600", self.__soundex("Ben Aron"))

        self.assertEqual("097400|097500", self.__soundex("AUERBACH"))
        self.assertEqual("097400|097500", self.__soundex("OHRBACH"))
        self.assertEqual("874400", self.__soundex("LIPSHITZ"))
        self.assertEqual("874400|874500", self.__soundex("LIPPSZYC"))
        self.assertEqual("876450", self.__soundex("LEWINSKY"))
        self.assertEqual("876450", self.__soundex("LEVINSKI"))
        self.assertEqual("486740", self.__soundex("SZLAMAWICZ"))
        self.assertEqual("486740", self.__soundex("SHLAMOVITZ"))

    def testEncodeIgnoreTrimmable(self) -> None:

        # Test with trimmable characters
        self.assertEqual("746536", self.__encode(" \t\n\r Washington \t\n\r "))

        # Test without trimmable characters
        self.assertEqual("746536", self.__encode("Washington"))

    def testEncodeIgnoreHyphens(self) -> None:

        self.checkEncodingVariations(
            "565463",
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
            "079600",
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

    def testAdjacentCodes(self) -> None:

        self.assertEqual("054800", self.__soundex("AKSSOL"))

        self.assertIn(
            self.__soundex("GERSCHFELD"), ["547830", "545783", "594783", "594578"]
        )

    def testAccentedCharacterFolding(self) -> None:

        # The unaccented version of "Straßburg" is "Strasburg"
        self.assertEqual("294795", self.__soundex("Straßburg"))
        self.assertEqual("294795", self.__soundex("Strasburg"))

        # The unaccented version of "Éregon" is "Eregon"
        self.assertEqual("095600", self.__soundex("Éregon"))
        self.assertEqual("095600", self.__soundex("Eregon"))

    def _createStringEncoder(self) -> DaitchMokotoffSoundex:
        return DaitchMokotoffSoundex.DaitchMokotoffSoundex1()

    def testEncodeBasic(self) -> None:

        self.assertEqual("097400", self.__encode("AUERBACH"))
        self.assertEqual("097400", self.__encode("OHRBACH"))
        self.assertEqual("874400", self.__encode("LIPSHITZ"))
        self.assertEqual("874400", self.__encode("LIPPSZYC"))
        self.assertEqual("876450", self.__encode("LEWINSKY"))
        self.assertEqual("876450", self.__encode("LEVINSKI"))
        self.assertEqual("486740", self.__encode("SZLAMAWICZ"))
        self.assertEqual("486740", self.__encode("SHLAMOVITZ"))

    def __encode(self, source: str) -> str:
        return self._stringEncoder.encode1(source)

    def __soundex(self, source: str) -> str:
        return self._stringEncoder.soundex0(source)
