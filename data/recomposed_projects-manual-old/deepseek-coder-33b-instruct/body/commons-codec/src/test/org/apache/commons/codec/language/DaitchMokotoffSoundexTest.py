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

        dm = DaitchMokotoffSoundex()
        self.assertEqual("364000|464000", dm.soundex0("ţamas"))  # t-cedilla
        self.assertEqual("364000|464000", dm.soundex0("țamas"))  # t-comma

    def testSoundexBasic3(self) -> None:

        dm = DaitchMokotoffSoundex()

        self.assertEqual("734000|739400", dm.soundex0("Peters"))
        self.assertEqual("734600|739460", dm.soundex0("Peterson"))
        self.assertEqual("645740", dm.soundex0("Moskowitz"))
        self.assertEqual("645740", dm.soundex0("Moskovitz"))
        self.assertEqual("154600|145460|454600|445460", dm.soundex0("Jackson"))
        self.assertEqual(
            "154654|154645|154644|145465|145464|454654|454645|454644|445465|445464",
            dm.soundex0("Jackson-Jackson"),
        )

    def testSoundexBasic2(self) -> None:

        dm = DaitchMokotoffSoundex()

        self.assertEqual("467000|567000", dm.soundex0("Ceniow"))
        self.assertEqual("467000", dm.soundex0("Tsenyuv"))
        self.assertEqual("587400|587500", dm.soundex0("Holubica"))
        self.assertEqual("587400", dm.soundex0("Golubitsa"))
        self.assertEqual("746480|794648", dm.soundex0("Przemysl"))
        self.assertEqual("746480", dm.soundex0("Pshemeshil"))
        self.assertEqual(
            "944744|944745|944754|944755|945744|945745|945754|945755",
            dm.soundex0("Rosochowaciec"),
        )
        self.assertEqual("945744", dm.soundex0("Rosokhovatsets"))

    def testSoundexBasic(self) -> None:

        dm = DaitchMokotoffSoundex()

        self.assertEqual("583600", dm.soundex0("GOLDEN"))
        self.assertEqual("087930", dm.soundex0("Alpert"))
        self.assertEqual("791900", dm.soundex0("Breuer"))
        self.assertEqual("579000", dm.soundex0("Haber"))
        self.assertEqual("665600", dm.soundex0("Mannheim"))
        self.assertEqual("664000", dm.soundex0("Mintz"))
        self.assertEqual("370000", dm.soundex0("Topf"))
        self.assertEqual("586660", dm.soundex0("Kleinmann"))
        self.assertEqual("769600", dm.soundex0("Ben Aron"))

        self.assertEqual("097400|097500", dm.soundex0("AUERBACH"))
        self.assertEqual("097400|097500", dm.soundex0("OHRBACH"))
        self.assertEqual("874400", dm.soundex0("LIPSHITZ"))
        self.assertEqual("874400|874500", dm.soundex0("LIPPSZYC"))
        self.assertEqual("876450", dm.soundex0("LEWINSKY"))
        self.assertEqual("876450", dm.soundex0("LEVINSKI"))
        self.assertEqual("486740", dm.soundex0("SZLAMAWICZ"))
        self.assertEqual("486740", dm.soundex0("SHLAMOVITZ"))

    def testEncodeIgnoreTrimmable(self) -> None:

        self.assertEqual("746536", self.__encode(" \t\n\r Washington \t\n\r "))
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

        dm = DaitchMokotoffSoundex()

        self.assertEqual("294795", dm.soundex0("Straßburg"))
        self.assertEqual("294795", dm.soundex0("Strasburg"))

        self.assertEqual("095600", dm.soundex0("Éregon"))
        self.assertEqual("095600", dm.soundex0("Eregon"))

    def _createStringEncoder(self) -> DaitchMokotoffSoundex:

        return DaitchMokotoffSoundex.DaitchMokotoffSoundex1()

    def testEncodeBasic(self) -> None:

        dm = DaitchMokotoffSoundex()

        self.assertEqual("097400", dm.encode1("AUERBACH"))
        self.assertEqual("097400", dm.encode1("OHRBACH"))
        self.assertEqual("874400", dm.encode1("LIPSHITZ"))
        self.assertEqual("874400", dm.encode1("LIPPSZYC"))
        self.assertEqual("876450", dm.encode1("LEWINSKY"))
        self.assertEqual("876450", dm.encode1("LEVINSKI"))
        self.assertEqual("486740", dm.encode1("SZLAMAWICZ"))
        self.assertEqual("486740", dm.encode1("SHLAMOVITZ"))

    def __encode(self, source: str) -> str:

        if source is None:
            return None

        dm = DaitchMokotoffSoundex()
        return dm.encode1(source)

    def __soundex(self, source: str) -> str:

        dm = DaitchMokotoffSoundex()
        return dm.soundex0(source)
