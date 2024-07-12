from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEngineRegressionTest(unittest.TestCase):

    def testCompatibilityWithOriginalVersion(self) -> None:

        args = {"nameType": "GENERIC", "ruleType": "APPROX"}
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom",
        )
        self.assertEqual(
            self.__encode(args, True, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn"
        )

        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abrom|avram|avrom|imbram|imbrom|obram|obrom|ombram|ombrom|ovram|ovrom",
        )
        self.assertEqual(
            self.__encode(args, True, "Halpern"),
            "YlpYrn|Ylpirn|alpYrn|alpirn|olpYrn|olpirn|xalpirn|xolpirn",
        )

    def testSolrSEPHARDIC(self) -> None:

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrASHKENAZI(self) -> None:

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrGENERIC(self) -> None:

        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    @staticmethod
    def __encode(args: typing.Dict[str, str], concat: bool, input: str) -> str:

        nameTypeArg = args.get("nameType")
        nameType = NameType.GENERIC if nameTypeArg is None else NameType[nameTypeArg]

        ruleTypeArg = args.get("ruleType")
        ruleType = RuleType.APPROX if ruleTypeArg is None else RuleType[ruleTypeArg]

        engine = PhoneticEngine.PhoneticEngine0(nameType, ruleType, concat)

        languageSetArg = args.get("languageSet")
        if languageSetArg is None or languageSetArg == "auto":
            languageSet = None
        else:
            languageSet = LanguageSet.from_(set(languageSetArg.split(",")))

        if languageSet is None:
            return engine.encode0(input)
        return engine.encode1(input, languageSet)
