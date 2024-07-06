from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *

# from src.test.org.apache.commons.fileupload.util.mime.MimeUtility_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MimeUtility_ESTest(unittest.TestCase):

    def test9(self) -> None:

        string0 = MimeUtility.decodeText("=?=?=?'? ")
        self.assertEqual("=?=?=?'?", string0)

    def test8(self) -> None:

        string0 = MimeUtility.decodeText('G~Kx"K-1)dL')
        self.assertEqual('G~Kx"K-1)dL', string0)

    def test7(self) -> None:

        string0 = MimeUtility.decodeText(" =??=??=?")
        self.assertEqual(" ", string0)

    def test6(self) -> None:

        string0 = MimeUtility.decodeText("f=?=?j?.?=?=?")
        self.assertEqual("f=?=?j?.?=?=?", string0)

    def test5(self) -> None:

        string0 = MimeUtility.decodeText("=?=?=??=?==")
        self.assertEqual("", string0)

    def test4(self) -> None:

        string0 = MimeUtility.decodeText(" =?")
        self.assertEqual(" =?", string0)

    def test3(self) -> None:

        string0 = MimeUtility.decodeText("=?=?")
        self.assertEqual("=?=?", string0)

    def test2(self) -> None:

        try:
            MimeUtility.decodeText("=?=?Q?6?=?=?=_?=?_=?")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid RFC 2047 encoding
            #
            self.verifyException(
                "org.apache.commons.fileupload.util.mime.MimeUtility", e
            )

    def test1(self) -> None:

        try:
            MimeUtility.decodeText("=?=?=?=?=?")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid RFC 2047 encoding
            #
            self.verifyException(
                "org.apache.commons.fileupload.util.mime.MimeUtility", e
            )

    def test0(self) -> None:

        try:
            MimeUtility.decodeText(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.verifyException(
                "org.apache.commons.fileupload.util.mime.MimeUtility", e
            )
