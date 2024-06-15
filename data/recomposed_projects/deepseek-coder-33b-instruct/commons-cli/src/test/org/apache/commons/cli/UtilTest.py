from __future__ import annotations
import unittest
import pytest
import io
from src.main.org.apache.commons.cli.Util import *


class UtilTest(unittest.TestCase):

    def testStripLeadingHyphens(self) -> None:

        from src.main.org.apache.commons.cli.Util import stripLeadingHyphens

        assert stripLeadingHyphens("-f") == "f"
        assert stripLeadingHyphens("--foo") == "foo"
        assert stripLeadingHyphens("---foo") == "-foo"
        assert stripLeadingHyphens(None) == None

    def testStripLeadingAndTrailingQuotes(self) -> None:

        assert Util.stripLeadingAndTrailingQuotes('"foo"') == "foo"
        assert Util.stripLeadingAndTrailingQuotes('foo "bar"') == 'foo "bar"'
        assert Util.stripLeadingAndTrailingQuotes('"foo" bar') == '"foo" bar'
        assert (
            Util.stripLeadingAndTrailingQuotes('"foo" and "bar"') == '"foo" and "bar"'
        )
        assert Util.stripLeadingAndTrailingQuotes('"') == '"'
