# Imports Begin
from src.main.org.joda.convert.StringConvert import *
import unittest
import typing
from typing import *

# Imports End


class TestJavaTime(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_basics(self) -> None:

        test = StringConvert.INSTANCE
        zone_id_class = self.convert_from_string(
            cls=typing.Type[typing.Any], str="java.time.ZoneId"
        )
        self.assertEqual(
            "Europe/Paris",
            test.convert_from_string(zone_id_class, "Europe/Paris").toString(),
        )
        zone_region_class = self.convert_from_string(
            cls=typing.Type[typing.Any], str="java.time.ZoneRegion"
        )
        self.assertEqual(
            "Europe/Paris",
            test.convert_from_string(zone_region_class, "Europe/Paris").toString(),
        )

    # Class Methods End
