# Imports Begin
from src.main.org.joda.convert.Validity import *
from src.main.org.joda.convert.StringConverter import *
import unittest
import typing
from typing import *
# Imports End

class ValidityStringConverter(unittest.TestCase, Enum<ValidityStringConverter>, StringConverter<Validity>):

    # Class Fields Begin
    INSTANCE: ValidityStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[Validity], str: str) -> Validity:


        pass # LLM could not translate method body

    def convertToString(self, object: Validity) -> str:

            return object.name()

    # Class Methods End


