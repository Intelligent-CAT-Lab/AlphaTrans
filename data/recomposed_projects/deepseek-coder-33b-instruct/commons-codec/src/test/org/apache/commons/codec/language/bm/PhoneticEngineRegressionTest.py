from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
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

        args = {"nameType": "ASHKENAZI", "ruleType": "APPROX"}
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
        assert (
            self.__encode(args, True, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        args["ruleType"] = "EXACT"
        assert self.__encode(args, True, "Angelo") == "anZelo|andZelo|anxelo"
        assert self.__encode(args, True, "D'Angelo") == "anZelo|andZelo|anxelo"
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, True, "Angelo") == "andZelo|anxelo"
        assert self.__encode(args, True, "1234") == ""

        args = {}
        args["nameType"] = "SEPHARDIC"
        assert (
            self.__encode(args, False, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        args["ruleType"] = "EXACT"
        assert self.__encode(args, False, "Angelo") == "anZelo|andZelo|anxelo"
        assert self.__encode(args, False, "D'Angelo") == "danZelo|dandZelo|danxelo"
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, False, "Angelo") == "andZelo|anxelo"
        assert self.__encode(args, False, "1234") == ""

        args = {}
        args["nameType"] = "SEPHARDIC"
        assert (
            self.__encode(args, True, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, True, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        assert (
            self.__encode(args, True, "D'Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert (
            self.__encode(args, True, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        assert self.__encode(args, True, "1234") == ""

        args = {}
        args["nameType"] = "SEPHARDIC"
        assert (
            self.__encode(args, False, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, False, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        assert (
            self.__encode(args, False, "D'Angelo")
            == "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert (
            self.__encode(args, False, "Angelo")
            == "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu"
        )
        assert self.__encode(args, False, "1234") == ""

    def testSolrASHKENAZI(self) -> None:

        args = dict()
        args["nameType"] = "ASHKENAZI"
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "EXACT"
        assert self.__encode(args, True, "Angelo") == "andZelo|angelo|anhelo|anxelo"
        assert (
            self.__encode(args, True, "D'Angelo") == "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, True, "Angelo") == "angelo|anxelo"
        assert self.__encode(args, True, "1234") == ""

        args = dict()
        args["nameType"] = "ASHKENAZI"
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "EXACT"
        assert self.__encode(args, False, "Angelo") == "andZelo|angelo|anhelo|anxelo"
        assert (
            self.__encode(args, False, "D'Angelo") == "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, False, "Angelo") == "angelo|anxelo"
        assert self.__encode(args, False, "1234") == ""

        args = dict()
        args["nameType"] = "ASHKENAZI"
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        assert (
            self.__encode(args, True, "D'Angelo")
            == "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, True, "Angelo") == "angilo|anxilo|ongilo|onxilo"
        assert self.__encode(args, True, "1234") == ""

        args = dict()
        args["nameType"] = "ASHKENAZI"
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo"
        )
        assert (
            self.__encode(args, False, "D'Angelo")
            == "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, False, "Angelo") == "angilo|anxilo|ongilo|onxilo"
        assert self.__encode(args, False, "1234") == ""

    def testSolrGENERIC(self) -> None:

        args = {}
        args["nameType"] = "GENERIC"
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "EXACT"
        assert (
            self.__encode(args, True, "Angelo")
            == "anZelo|andZelo|angelo|anhelo|anjelo|anxelo"
        )
        assert (
            self.__encode(args, True, "D'Angelo")
            == "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, True, "Angelo") == "andZelo|angelo|anxelo"
        assert self.__encode(args, True, "1234") == ""

        args = {}
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "EXACT"
        assert (
            self.__encode(args, False, "Angelo")
            == "anZelo|andZelo|angelo|anhelo|anjelo|anxelo"
        )
        assert (
            self.__encode(args, False, "D'Angelo")
            == "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert self.__encode(args, False, "Angelo") == "andZelo|angelo|anxelo"
        assert self.__encode(args, False, "1234") == ""

        args = {}
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, True, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        assert (
            self.__encode(args, True, "D'Angelo")
            == "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert (
            self.__encode(args, True, "Angelo")
            == "angilo|anxilo|anzilo|ongilo|onxilo|onzilo"
        )
        assert self.__encode(args, True, "1234") == ""

        args = {}
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        args["ruleType"] = "APPROX"
        assert (
            self.__encode(args, False, "Angelo")
            == "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo"
        )
        assert (
            self.__encode(args, False, "D'Angelo")
            == "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)"
        )
        args["languageSet"] = "italian,greek,spanish"
        assert (
            self.__encode(args, False, "Angelo")
            == "angilo|anxilo|anzilo|ongilo|onxilo|onzilo"
        )
        assert self.__encode(args, False, "1234") == ""

    @staticmethod
    def __encode(args: typing.Dict[str, str], concat: bool, input: str) -> str:

        pass  # LLM could not translate this method
