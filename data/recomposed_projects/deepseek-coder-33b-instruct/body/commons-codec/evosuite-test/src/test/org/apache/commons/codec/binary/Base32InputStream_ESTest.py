from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base32InputStream import *

# from src.test.org.apache.commons.codec.binary.Base32InputStream_ESTest_scaffolding import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Base32InputStream_ESTest(unittest.TestCase):

    def test4(self) -> None:

        pipedInputStream0 = io.BytesIO()
        baseNCodecInputStream0 = Base32InputStream.Base32InputStream0(pipedInputStream0)

        with pytest.raises(ValueError):
            Base32InputStream.Base32InputStream2(
                baseNCodecInputStream0, False, 23, None
            )
            pytest.fail("Expecting exception: ValueError")

    def test3(self) -> None:

        pipedInputStream0 = io.BytesIO()
        codecPolicy0 = CodecPolicy.STRICT
        base32InputStream0 = None
        try:
            base32InputStream0 = Base32InputStream(
                pipedInputStream0, True, 1703, None, codecPolicy0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # lineLength 1703 > 0, but lineSeparator is null
            self.verifyException("org.apache.commons.codec.binary.Base32", e)

    def test2(self) -> None:

        pipedInputStream0 = io.BytesIO()
        byteArray0 = bytearray()
        codecPolicy0 = CodecPolicy.LENIENT
        base32InputStream0 = Base32InputStream(
            pipedInputStream0, True, 2781, byteArray0, codecPolicy0
        )
        self.assertEqual(1, base32InputStream0.available())

    def test1(self) -> None:

        file_descriptor0 = io.FileIO("file_path", "r")
        mock_file_input_stream0 = io.BufferedReader(file_descriptor0)
        base_n_codec_input_stream0 = Base32InputStream.Base32InputStream1(
            mock_file_input_stream0, True
        )
        assert not base_n_codec_input_stream0.markSupported()

    def test0(self) -> None:

        inputStream0 = io.BytesIO()
        byteArray0 = bytearray()
        baseNCodecInputStream0 = Base32InputStream.Base32InputStream2(
            inputStream0, True, 1327, byteArray0
        )
        self.assertFalse(baseNCodecInputStream0.markSupported())
