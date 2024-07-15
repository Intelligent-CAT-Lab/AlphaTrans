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

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.AnnotationStringConverterFactory import *

# from src.test.org.joda.convert.AnnotationStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class AnnotationStringConverterFactory_ESTest(unittest.TestCase):

    def test5(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE
        string0 = annotationStringConverterFactory0.toString()
        self.assertEqual("AnnotationStringConverterFactory", string0)

    def test4(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE
        class0 = object
        typedFromStringConverter0 = (
            annotationStringConverterFactory0.findFromStringConverter(class0)
        )
        self.assertIsNone(typedFromStringConverter0)

    def test3(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE
        class0 = AnnotationStringConverterFactory
        stringConverter0 = annotationStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test2(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE
        class0 = AnnotationStringConverterFactory
        typedFromStringConverter0 = (
            annotationStringConverterFactory0.findFromStringConverter(class0)
        )
        self.assertIsNone(typedFromStringConverter0)

    def test1(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE

        with self.assertRaises(RuntimeError):
            annotationStringConverterFactory0.findConverter(None)

    def test0(self) -> None:

        annotationStringConverterFactory0 = AnnotationStringConverterFactory.INSTANCE

        with self.assertRaises(RuntimeError):
            annotationStringConverterFactory0.findFromStringConverter(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.joda.convert.AnnotationStringConverterFactory", e)
