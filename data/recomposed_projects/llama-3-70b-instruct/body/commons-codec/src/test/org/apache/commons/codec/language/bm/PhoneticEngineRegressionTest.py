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

        pass  # LLM could not translate this method

    def testSolrSEPHARDIC(self) -> None:
        args: typing.Dict[str, str]

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

        pass  # LLM could not translate this method

    def testSolrGENERIC(self) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __encode(args: typing.Dict[str, str], concat: bool, input: str) -> str:

        pass  # LLM could not translate this method
