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
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.net.BCodec import *
from src.main.org.apache.commons.codec.net.QCodec import *

# from src.test.org.apache.commons.codec.net.RFC1522Codec_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class RFC1522Codec_ESTest(unittest.TestCase):

    def test17(self) -> None:
        bCodec0 = BCodec.BCodec0()
        charset0 = "UTF-8"
        string0 = bCodec0.encodeText0(None, charset0)
        self.assertIsNone(string0)

    def test16(self) -> None:

        charset0 = "UTF-8"
        qCodec0 = QCodec(-189081844, " cannot be quoted-printable encoded", charset0)
        string0 = qCodec0._encodeText1(" cannot be quoted-printable encoded", "UTF-8")
        assert string0 is not None
        self.assertEqual("=?UTF-8?Q? cannot be quoted-printable encoded?=", string0)

    def test15(self) -> None:
        qCodec0 = QCodec.QCodec2()
        string0 = qCodec0._encodeText1(None, "~")
        self.assertIsNone(string0)

    def test14(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decodeText(None)
        self.assertIsNone(string0)

    def test13(self) -> None:

        charset0 = "UTF-8"
        qCodec0 = QCodec(-189081844, " cannot be quoted-printable encoded", charset0)
        try:
            qCodec0.decode0("?=")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: malformed encoded content
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test12(self) -> None:

        bCodec0 = BCodec.BCodec0()
        rfc1522Codec = RFC1522Codec()

        try:
            rfc1522Codec._decodeText("=?")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: malformed encoded content
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test11(self) -> None:

        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.decodeText("=?fB?=")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: charset token not found
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test10(self) -> None:

        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.decodeText("=??=?")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: charset not specified
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test09(self) -> None:

        bCodec0 = BCodec.BCodec0()
        rfc1522Codec = RFC1522Codec()

        try:
            rfc1522Codec._decodeText("=?fB?=?=")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # RFC 1522 violation: encoding token not found
            #
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test08(self) -> None:

        charset0 = "UTF-8"
        codecPolicy0 = CodecPolicy.LENIENT
        bCodec0 = BCodec(charset0, codecPolicy0)

        try:
            bCodec0.decode1("=?UTF-8?Q?nN-?=")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # This codec cannot decode Q encoded content
            self.verifyException("org.apache.commons.codec.net.RFC1522Codec", e)

    def test07(self) -> None:

        bCodec0 = BCodec.BCodec0()
        # Undeclared exception in Java code
        try:
            bCodec0.decodeText("=?=")
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test06(self) -> None:
        qCodec0 = QCodec.QCodec2()
        try:
            qCodec0.encodeText0("", None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError:
            pass

    def test05(self) -> None:
        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.encodeText1("/Pd>}/R", None)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test04(self) -> None:
        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.encodeText1("=>[ySVTkOjI*,Q5<", "=>[ySVTkOjI*,Q5<")
            self.fail("Expecting exception: IllegalCharsetNameException")
        except IllegalCharsetNameException as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test03(self) -> None:
        bCodec0 = BCodec.BCodec0()
        try:
            bCodec0.encodeText1("k", "k")
            self.fail("Expecting exception: UnsupportedCharsetException")
        except UnsupportedCharsetException as e:
            self.verifyException("java.nio.charset.Charset", e)

    def test02(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decodeText("=?UTF-8?B??=")
        self.assertEqual("", string0)

    def test01(self) -> None:

        bCodec0 = BCodec.BCodec0()
        string0 = bCodec0.decodeText(
            "=?UTF-8?B?PT9VVEYtOD9RPz0zRD0zRlVURi04PTNGUT0zRm4tPTNGPTNEPz0=?=?=?=?="
        )
        self.assertEqual("=?UTF-8?Q?=3D=3FUTF-8=3FQ=3Fn-=3F=3D?=", string0)

    def test00(self) -> None:
        qCodec0 = QCodec.QCodec2()
        charset0 = "UTF-8"
        string0 = qCodec0._encodeText0("nN-", charset0)
        self.assertEqual("=?UTF-8?Q?nN-?=", string0)
