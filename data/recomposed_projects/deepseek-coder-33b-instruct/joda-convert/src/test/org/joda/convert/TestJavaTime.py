from __future__ import annotations
import io
from src.main.org.joda.convert.StringConvert import *


class TestJavaTime:

    def test_basics(self) -> None:

        test = StringConvert.INSTANCE

        zoneIdClass = Class.forName("java.time.ZoneId")
        assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneIdClass, "Europe/Paris").toString(),
        )

        zoneRegionClass = Class.forName("java.time.ZoneRegion")
        assertEqual(
            "Europe/Paris",
            test.convertFromString(zoneRegionClass, "Europe/Paris").toString(),
        )
