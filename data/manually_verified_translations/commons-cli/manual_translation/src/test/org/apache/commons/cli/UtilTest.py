from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Util import *


class UtilTest(unittest.TestCase):

    def testStripLeadingHyphens(self) -> None:

        self.assertEqual(Util.stripLeadingHyphens("-f"), "f")
        self.assertEqual(Util.stripLeadingHyphens("--foo"), "foo")
        self.assertEqual(Util.stripLeadingHyphens("---foo"), "-foo")
        self.assertIsNone(Util.stripLeadingHyphens(None))

    def testStripLeadingAndTrailingQuotes(self) -> None:

        self.assertEqual("foo", Util.stripLeadingAndTrailingQuotes('"foo"'))
        self.assertEqual('foo "bar"', Util.stripLeadingAndTrailingQuotes('foo "bar"'))
        self.assertEqual('"foo" bar', Util.stripLeadingAndTrailingQuotes('"foo" bar'))
        self.assertEqual(
            '"foo" and "bar"', Util.stripLeadingAndTrailingQuotes('"foo" and "bar"')
        )
        self.assertEqual('"', Util.stripLeadingAndTrailingQuotes('"'))
