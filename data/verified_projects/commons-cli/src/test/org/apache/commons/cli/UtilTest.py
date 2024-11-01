import pytest

from src.main.org.apache.commons.cli.Util import *
import unittest

class UtilTest(unittest.TestCase):

    @pytest.mark.test
    def testStripLeadingAndTrailingQuotes(self) -> None:
        self.assertEqual("foo", Util.stripLeadingAndTrailingQuotes("\"foo\""))
        self.assertEqual("foo \"bar\"", Util.stripLeadingAndTrailingQuotes("foo \"bar\""))
        self.assertEqual("\"foo\" bar", Util.stripLeadingAndTrailingQuotes("\"foo\" bar"))
        self.assertEqual(
                "\"foo\" and \"bar\"", Util.stripLeadingAndTrailingQuotes("\"foo\" and \"bar\""))
        self.assertEqual("\"", Util.stripLeadingAndTrailingQuotes("\""))

    
    @pytest.mark.test
    def testStripLeadingHyphens(self) -> None:
        self.assertEqual("f", Util.stripLeadingHyphens("-f"))
        self.assertEqual("foo", Util.stripLeadingHyphens("--foo"))
        self.assertEqual("-foo", Util.stripLeadingHyphens("---foo"))
        self.assertIsNone(Util.stripLeadingHyphens(None))
