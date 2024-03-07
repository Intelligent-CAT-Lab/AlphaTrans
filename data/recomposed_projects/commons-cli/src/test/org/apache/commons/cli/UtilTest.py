# Imports Begin
from src.main.org.apache.commons.cli.Util import *
import unittest

# Imports End


class UtilTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testStripLeadingHyphens(self) -> None:

        self.assertEqual("f", Util.stripLeadingHyphens("-f"))
        self.assertEqual("foo", Util.stripLeadingHyphens("--foo"))
        self.assertEqual("-foo", Util.stripLeadingHyphens("---foo"))
        self.assertIsNone(Util.stripLeadingHyphens(None))

    def testStripLeadingAndTrailingQuotes(self) -> None:

        self.assertEqual(Util.stripLeadingAndTrailingQuotes('"foo"'), "foo")
        self.assertEqual(Util.stripLeadingAndTrailingQuotes('foo "bar"'), 'foo "bar"')
        self.assertEqual(Util.stripLeadingAndTrailingQuotes('"foo" bar'), '"foo" bar')
        self.assertEqual(
            Util.stripLeadingAndTrailingQuotes('"foo" and "bar"'), '"foo" and "bar"'
        )
        self.assertEqual(Util.stripLeadingAndTrailingQuotes('"'), '"')

    # Class Methods End
