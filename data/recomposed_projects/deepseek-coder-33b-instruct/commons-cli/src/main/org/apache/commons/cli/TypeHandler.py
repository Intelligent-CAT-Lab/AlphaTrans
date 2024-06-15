from __future__ import annotations
import urllib
import pathlib
import io
import numbers
import typing
from typing import *
import datetime
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *


class TypeHandler:

    @staticmethod
    def createValue0(str: str, clazz: typing.Type[typing.Any]) -> typing.Any:

        if clazz == PatternOptionBuilder.STRING_VALUE:
            return str
        elif clazz == PatternOptionBuilder.OBJECT_VALUE:
            return TypeHandler.createObject(str)
        elif clazz == PatternOptionBuilder.NUMBER_VALUE:
            return TypeHandler.createNumber(str)
        elif clazz == PatternOptionBuilder.DATE_VALUE:
            return TypeHandler.createDate(str)
        elif clazz == PatternOptionBuilder.CLASS_VALUE:
            return TypeHandler.createClass(str)
        elif clazz == PatternOptionBuilder.FILE_VALUE:
            return TypeHandler.createFile(str)
        elif clazz == PatternOptionBuilder.EXISTING_FILE_VALUE:
            return TypeHandler.openFile(str)
        elif clazz == PatternOptionBuilder.FILES_VALUE:
            return TypeHandler.createFiles(str)
        elif clazz == PatternOptionBuilder.URL_VALUE:
            return TypeHandler.createURL(str)
        else:
            raise ParseException("Unable to handle the class: " + str(clazz))

    @staticmethod
    def openFile(str: str) -> typing.Union[io.FileIO, io.BufferedReader]:

        try:
            return open(str, "r")
        except FileNotFoundError:
            raise ParseException("Unable to find file: " + str)

    @staticmethod
    def createValue1(str: str, obj: typing.Any) -> typing.Any:

        return TypeHandler.createValue0(str, typing.cast(typing.Type[typing.Any], obj))

    @staticmethod
    def createURL(
        str: str,
    ) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:

        try:
            return urllib.parse.urlparse(str)
        except ValueError:
            raise ParseException("Unable to parse the URL: " + str)

    @staticmethod
    def createObject(classname: str) -> typing.Any:

        try:
            cl = getattr(__import__("builtins"), classname)
        except AttributeError:
            raise ParseException("Unable to find the class: " + classname)

        try:
            return cl()
        except Exception as e:
            raise ParseException(
                e.__class__.__name__ + "; Unable to create an instance of: " + classname
            )

    @staticmethod
    def createNumber(str: str) -> typing.Union[int, float, numbers.Number]:

        try:
            if "." in str:
                return float(str)
            return int(str)
        except ValueError as e:
            raise ParseException(e.args[0])

    @staticmethod
    def createFiles(str: str) -> typing.List[pathlib.Path]:

        # The Java code you provided does not create any files, it just declares a method that throws an NotImplementedError.
        # If you want to create files in Python, you can use the built-in open function.
        # Here is an example of how you can create a file:

        # Create a file
        with open("example.txt", "w") as f:
            f.write(str)

        # Get the path of the created file
        file_path = pathlib.Path("example.txt")

        # Return the path of the created file as a list
        return [file_path]

    @staticmethod
    def createFile(str: str) -> pathlib.Path:

        return pathlib.Path(str)

    @staticmethod
    def createDate(str: str) -> typing.Union[datetime.date, datetime.datetime]:

        # Convert the string to a datetime object
        try:
            return datetime.datetime.strptime(str, "%Y-%m-%d")
        except ValueError:
            pass

        # Convert the string to a date object
        try:
            return datetime.datetime.strptime(str, "%Y-%m-%d").date()
        except ValueError:
            pass

        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    @staticmethod
    def createClass(classname: str) -> typing.Type[typing.Any]:

        try:
            return globals()[classname]
        except KeyError:
            raise ParseException("Unable to find the class: " + classname)
