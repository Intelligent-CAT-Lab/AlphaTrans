from __future__ import annotations
import re
import sys
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.test.org.apache.commons.cli.ParserTestCase import *


class GnuParserTest(ParserTestCase, unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def testUnrecognizedOptionWithBursting(self) -> None:
        pass






    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption4(self) -> None:
        pass









    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption3(self) -> None:
        pass




    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption2(self) -> None:
        pass






    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption1(self) -> None:
        pass






    @pytest.mark.skip(reason="Ignore")
    def testStopBursting2(self) -> None:
        pass







    @pytest.mark.skip(reason="Ignore")
    def testStopBursting(self) -> None:
        pass




    @pytest.mark.skip(reason="Ignore")
    def testShortWithUnexpectedArgument(self) -> None:
        pass


    @pytest.mark.skip(reason="Ignore")
    def testPartialLongOptionSingleDash(self) -> None:
        pass





    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:
        pass



    @pytest.mark.skip(reason="Ignore")
    def testMissingArgWithBursting(self) -> None:
        pass





    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument2(self) -> None:
        pass






    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:
        pass





    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:
        pass




    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:
        pass




    @pytest.mark.skip(reason="Ignore")
    def testBursting(self) -> None:
        pass








    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:
        pass


    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption3(self) -> None:
        pass





    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption2(self) -> None:
        pass





    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption1(self) -> None:
        pass




    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
        pass


    def setUp(self) -> None:

        super().setUp()
        self._parser = GnuParser()
