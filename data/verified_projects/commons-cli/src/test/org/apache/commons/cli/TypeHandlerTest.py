# Imports Begin
from src.main.org.apache.commons.cli.TypeHandler import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.ParseException import *
import unittest
from urllib.parse import ParseResult, SplitResult, DefragResult, urlunparse
from typing import *

# Imports End

class TypeHandlerTest(unittest.TestCase):

    class Instantiable:
        pass

    class NotInstantiable:
        def __init__(self) -> None:
            raise AssertionError("This class should not be instantiated.")

    # Class Methods Begin
    def testCreateValueClass(self) -> None:
        try:
            clazz = TypeHandler.createValue0(
                self.Instantiable.__name__, PatternOptionBuilder.CLASS_VALUE)
            self.assertEqual(self.Instantiable, clazz)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    def testCreateValueClass_notFound(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0("what ever", PatternOptionBuilder.CLASS_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")

    
    def testCreateValueDate(self) -> None:
        try:
            with self.assertRaises((RuntimeError, NotImplementedError)):
                TypeHandler.createValue0("what ever", PatternOptionBuilder.DATE_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected RuntimeError or NotImplementedError, got: {e}")
    
    
    def testCreateValueExistingFile(self) -> None:
        try:
            with TypeHandler.createValue0(
                "src/test/resources/org/apache/commons/cli/existing-readable.file",
                PatternOptionBuilder.EXISTING_FILE_VALUE,
            ) as result:
                self.assertIsNotNone(result)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    def testCreateValueExistingFile_nonExistingFile(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0(
                    "non-existing.file", PatternOptionBuilder.EXISTING_FILE_VALUE
                )
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")
    
    
    def testCreateValueFile(self) -> None:
        try:
            result = TypeHandler.createValue0(
                "some-file.txt", PatternOptionBuilder.FILE_VALUE
            )
            self.assertEqual("some-file.txt", result.name)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testCreateValueFiles(self) -> None:
        try:
            with self.assertRaises((RuntimeError, NotImplementedError)):
                TypeHandler.createValue0("some.files", PatternOptionBuilder.FILES_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected RuntimeError or NotImplementedError, got: {e}")
    
    
    def testCreateValueInteger_failure(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0("just-a-string", int)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")

    
    def testCreateValueNumber_Double(self) -> None:
        try:
            self.assertEqual(
                1.5, TypeHandler.createValue0("1.5", PatternOptionBuilder.NUMBER_VALUE)
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    def testCreateValueNumber_Long(self) -> None:
        try:
            self.assertEqual(
                15, TypeHandler.createValue0("15", PatternOptionBuilder.NUMBER_VALUE)
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testCreateValueNumber_noNumber(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0("not a number", PatternOptionBuilder.NUMBER_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")
    
    
    def testCreateValueObject_InstantiableClass(self) -> None:
        try:
            result = TypeHandler.createValue0(
                self.Instantiable.__name__, PatternOptionBuilder.OBJECT_VALUE)
            self.assertIsInstance(result, self.Instantiable)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    def testCreateValueObject_notInstantiableClass(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0(self.NotInstantiable.__name__, PatternOptionBuilder.OBJECT_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")

    
    def testCreateValueObject_unknownClass(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0("unknown", PatternOptionBuilder.OBJECT_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")

    
    def testCreateValueString(self) -> None:
        try:
            self.assertEqual(
                "String",
                TypeHandler.createValue0("String", PatternOptionBuilder.STRING_VALUE),
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testCreateValueURL(self) -> None:
        try:
            urlString = "https://commons.apache.org"
            result = TypeHandler.createValue0(urlString, PatternOptionBuilder.URL_VALUE)
            if isinstance(result, (ParseResult, SplitResult, DefragResult)):
                self.assertEqual(urlString, urlunparse(result))
            else:
                self.assertEqual(urlString, result)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    def testCreateValueURL_malformed(self) -> None:
        try:
            with self.assertRaises(ParseException):
                TypeHandler.createValue0("malformed-url", PatternOptionBuilder.URL_VALUE)
        except Exception as e:
            self.fail(f"Incorrect exception raised - Expected ParseException, got: {e}")

    # Class Methods End

