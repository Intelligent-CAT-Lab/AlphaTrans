from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI18Test(unittest.TestCase):

    def testCLI18(self) -> None:

        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(
            Option(
                0,
                None,
                "bbb",
                "bbbbbbb dksh fkshd fkhs dkfhsdk fhskd hksdks dhfowehfsdhfkjshf skfhkshf sf"
                + " jkshfk sfh skfh skf f",
                False,
                None,
            )
        )
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

        formatter = HelpFormatter()
        out = io.StringIO()

        formatter.printHelp3(
            io.TextIOWrapper(out),
            80,
            "foobar",
            "dsfkfsh kdh hsd hsdh fkshdf ksdh fskdh fsdh fkshfk sfdkjhskjh fkjh fkjsh khsdkj"
            + " hfskdhf skjdfh ksf khf s",
            options,
            2,
            2,
            "blort j jgj j jg jhghjghjgjhgjhg jgjhgj jhg jhg hjg jgjhghjg jhg hjg jhgjg"
            + " jgjhghjg jg jgjhgjgjg jhg jhgjh"
            + "\r"
            + "\n"
            + "rarrr",
            True,
        )
