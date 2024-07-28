from __future__ import annotations
import time
import re
import pathlib
import io
import numbers
import typing
from typing import *
import datetime
import urllib
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *


class TypeHandler:

    @staticmethod
    def createValue0(str_: str, clazz: typing.Type[typing.Any]) -> typing.Any:

        if clazz == PatternOptionBuilder.STRING_VALUE:
            return str_
        if clazz == PatternOptionBuilder.OBJECT_VALUE:
            return TypeHandler.createObject(str_)
        if clazz == PatternOptionBuilder.NUMBER_VALUE:
            return TypeHandler.createNumber(str_)
        if clazz == PatternOptionBuilder.DATE_VALUE:
            return TypeHandler.createDate(str_)
        if clazz == PatternOptionBuilder.CLASS_VALUE:
            return TypeHandler.createClass(str_)
        if clazz == PatternOptionBuilder.FILE_VALUE:
            return TypeHandler.createFile(str_)
        if clazz == PatternOptionBuilder.EXISTING_FILE_VALUE:
            return TypeHandler.openFile(str_)
        if clazz == PatternOptionBuilder.FILES_VALUE:
            return TypeHandler.createFiles(str_)
        if clazz == PatternOptionBuilder.URL_VALUE:
            return TypeHandler.createURL(str_)
        raise ParseException("Unable to handle the class: " + str(clazz))

    @staticmethod
    def openFile(str_: str) -> typing.Union[io.FileIO, io.BufferedReader]:
        try:
            return open(str_, "r")
        except FileNotFoundError:
            raise ParseException("Unable to find file: " + str_)

    @staticmethod
    def createValue1(str_: str, obj: typing.Any) -> typing.Any:

        if isinstance(obj, PatternOptionBuilder):
            return TypeHandler.createValue0(str_, obj.getType())
        else:
            raise ParseException("Unable to handle the class: " + str(obj))

    @staticmethod
    def createURL(
        str_: str,
    ) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:
        try:
            return urllib.parse.urlparse(str_)
        except ValueError:
            raise ParseException("Unable to parse the URL: " + str_)

    @staticmethod
    def createObject(classname: str) -> typing.Any:

        try:
            cl = globals()[classname]
        except KeyError:
            raise ParseException("Unable to find the class: " + classname)

        try:
            return cl()
        except Exception as e:
            raise ParseException(
                e.__class__.__name__ + "; Unable to create an instance of: " + classname
            )

    @staticmethod
    def createNumber(str_: str) -> typing.Union[int, float, numbers.Number]:
        try:
            if "." in str_:
                return float(str_)
            return int(str_)
        except ValueError as e:
            raise ParseException(str(e))

    @staticmethod
    def createFiles(str_: str) -> typing.List[pathlib.Path]:

        # Split the string into a list of file paths
        file_paths = str_.split(",")

        # Create a list to hold the file objects
        files = []

        # Iterate over the file paths
        for path in file_paths:

            # Create a file object
            file = pathlib.Path(path.strip())

            # Add the file object to the list
            files.append(file)

        # Return the list of file objects
        return files

    @staticmethod
    def createFile(str_: str) -> pathlib.Path:
        return pathlib.Path(str_)

    @staticmethod
    def createDate(str_: str) -> typing.Union[datetime.datetime, datetime.date]:

        # Convert the string to a datetime object
        try:
            return datetime.datetime.strptime(str_, "%Y-%m-%d")
        except ValueError:
            pass

        # If the conversion fails, try to convert it to a date object
        try:
            return datetime.datetime.strptime(str_, "%Y-%m-%d").date()
        except ValueError:
            pass

        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    @staticmethod
    def createClass(classname: str) -> typing.Type[typing.Any]:
        try:
            return globals()[classname]
        except KeyError:
            raise ParseException("Unable to find the class: " + classname)
