from __future__ import annotations
import re
import unittest
import pytest
import io
import numbers
import typing
from typing import *
import unittest
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.TypeHandler import *


class Instantiable:

    pass


class NotInstantiable:

    def __init__(self) -> None:
        raise TypeError("This class cannot be instantiated")


class TypeHandlerTest(unittest.TestCase):

    def testCreateValueURL_malformed(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0("malformed-url", PatternOptionBuilder.URL_VALUE)

    def testCreateValueURL(self) -> None:

        url_string = "https://commons.apache.org"
        result = TypeHandler.createValue0(url_string, PatternOptionBuilder.URL_VALUE)
        self.assertEqual(url_string, result.geturl())

    def testCreateValueString(self) -> None:

        self.assertEqual(
            "String",
            TypeHandler.createValue0("String", PatternOptionBuilder.STRING_VALUE),
        )

    def testCreateValueObject_unknownClass(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0("unknown", PatternOptionBuilder.OBJECT_VALUE)

    def testCreateValueObject_notInstantiableClass(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0(
                NotInstantiable.__name__, PatternOptionBuilder.OBJECT_VALUE
            )

    def testCreateValueObject_InstantiableClass(self) -> None:

        result = TypeHandler.createValue0(
            Instantiable.__name__, PatternOptionBuilder.OBJECT_VALUE
        )
        self.assertIsInstance(result, Instantiable)

    def testCreateValueNumber_noNumber(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0("not a number", PatternOptionBuilder.NUMBER_VALUE)

    def testCreateValueNumber_Long(self) -> None:

        self.assertEqual(
            15, TypeHandler.createValue0("15", PatternOptionBuilder.NUMBER_VALUE)
        )

    def testCreateValueNumber_Double(self) -> None:

        self.assertEqual(
            1.5, TypeHandler.createValue0("1.5", PatternOptionBuilder.NUMBER_VALUE)
        )

    def testCreateValueInteger_failure(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0("just-a-string", int)

    def testCreateValueFiles(self) -> None:

        with pytest.raises(NotImplementedError):
            TypeHandler.createValue0("some.files", PatternOptionBuilder.FILES_VALUE)

    def testCreateValueFile(self) -> None:

        result = TypeHandler.createValue0(
            "some-file.txt", PatternOptionBuilder.FILE_VALUE
        )
        self.assertEqual("some-file.txt", result.name)

    def testCreateValueExistingFile_nonExistingFile(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0(
                "non-existing.file", PatternOptionBuilder.EXISTING_FILE_VALUE
            )

    def testCreateValueExistingFile(self) -> None:

        with TypeHandler.createValue0(
                "src/test/resources/org/apache/commons/cli/existing-readable.file",
                PatternOptionBuilder.EXISTING_FILE_VALUE,
            ) as result:
                self.assertIsNotNone(result)

    def testCreateValueDate(self) -> None:

        with pytest.raises(NotImplementedError):
            TypeHandler.createValue0("what ever", PatternOptionBuilder.DATE_VALUE)

    def testCreateValueClass_notFound(self) -> None:

        with pytest.raises(ParseException):
            TypeHandler.createValue0("what ever", PatternOptionBuilder.CLASS_VALUE)

    def testCreateValueClass(self) -> None:

        clazz = TypeHandler.createValue0(
            Instantiable.__name__, PatternOptionBuilder.CLASS_VALUE)
        self.assertEqual(Instantiable, clazz)
