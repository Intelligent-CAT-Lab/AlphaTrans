# Imports Begin
from src.main.org.apache.commons.cli.TypeHandler import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
import unittest
import typing
from typing import *
import numbers

# Imports End


class TypeHandlerTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testCreateValueURL_malformed(self) -> None:

        with self.assertRaises(ValueError):
            TypeHandler.createValue0("malformed-url", PatternOptionBuilder.URL_VALUE)

    def testCreateValueURL(self) -> None:

        url_string = "https://commons.apache.org"
        result = TypeHandler.createValue0(url_string, PatternOptionBuilder.URL_VALUE)
        self.assertEqual(url_string, result.toString())

    def testCreateValueString(self) -> None:

        self.assertEqual(
            "String",
            TypeHandler.createValue0("String", PatternOptionBuilder.STRING_VALUE),
        )

    def testCreateValueObject_unknownClass(self) -> None:

        with self.assertRaises(ValueError):
            TypeHandler.createValue0("unknown", PatternOptionBuilder.OBJECT_VALUE)

    def testCreateValueObject_notInstantiableClass(self) -> None:

        with self.assertRaises(TypeError):
            TypeHandler.createValue0(NotInstantiable, PatternOptionBuilder.OBJECT_VALUE)

    def testCreateValueObject_InstantiableClass(self) -> None:

        pass  # LLM could not translate method body

    def testCreateValueNumber_noNumber(self) -> None:

        with self.assertRaises(ValueError):
            TypeHandler.createValue0("not a number", PatternOptionBuilder.NUMBER_VALUE)

    def testCreateValueNumber_Long(self) -> None:

        self.assertEqual(
            self.createValue0("15", PatternOptionBuilder.NUMBER_VALUE), Long.valueOf(15)
        )

    def testCreateValueNumber_Double(self) -> None:

        self.assertEqual(
            1.5, TypeHandler.createValue0("1.5", PatternOptionBuilder.NUMBER_VALUE)
        )

    def testCreateValueInteger_failure(self) -> None:

        with self.assertRaises(ValueError):
            TypeHandler.createValue0("just-a-string", int)

    def testCreateValueFiles(self) -> None:

        TypeHandler.createValue0("some.files", PatternOptionBuilder.FILES_VALUE)

    def testCreateValueFile(self) -> None:

        result = TypeHandler.createValue0(
            "some-file.txt", PatternOptionBuilder.FILE_VALUE
        )
        self.assertEqual("some-file.txt", result.getName())

    def testCreateValueExistingFile_nonExistingFile(self) -> None:

        with self.assertRaises(Exception):
            TypeHandler.createValue0(
                "non-existing.file", PatternOptionBuilder.EXISTING_FILE_VALUE
            )

    def testCreateValueExistingFile(self) -> None:

        with self.createValue0(
            "src/test/resources/org/apache/commons/cli/existing-readable.file",
            PatternOptionBuilder.EXISTING_FILE_VALUE,
        ) as result:
            self.assertNotNull(result)

    def testCreateValueDate(self) -> None:

        TypeHandler.createValue0("what ever", PatternOptionBuilder.DATE_VALUE)

    def testCreateValueClass_notFound(self) -> None:

        with self.assertRaises(ValueError):
            TypeHandler.createValue0("what ever", PatternOptionBuilder.CLASS_VALUE)

    def testCreateValueClass(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End


class Instantiable(unittest.TestCase):

    pass


class NotInstantiable(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(self) -> None:

        pass

    # Class Methods End
