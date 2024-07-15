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
            raise ParseException(str(e))

    @staticmethod
    def createFiles(str: str) -> typing.List[pathlib.Path]:

        # Assuming str is a comma-separated list of file names
        file_names = str.split(",")

        # Create a list to hold the file paths
        file_paths = []

        # Create each file and add its path to the list
        for file_name in file_names:
            file_path = pathlib.Path(file_name)
            file_path.touch()
            file_paths.append(file_path)

        return file_paths

    @staticmethod
    def createFile(str: str) -> pathlib.Path:
        return pathlib.Path(str)

    @staticmethod
    def createDate(str: str) -> typing.Union[datetime.datetime, datetime.date]:

        # Check if the string is in the format 'yyyy-MM-dd'
        if str.count("-") == 2:
            return datetime.datetime.strptime(str, "%Y-%m-%d").date()

        # Check if the string is in the format 'yyyy-MM-dd HH:mm:ss'
        elif str.count("-") == 2 and str.count(":") == 2:
            return datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

        # Check if the string is in the format 'yyyy-MM-ddTHH:mm:ss'
        elif str.count("-") == 2 and str.count(":") == 2 and str.count("T") == 1:
            return datetime.datetime.strptime(str, "%Y-%m-%dT%H:%M:%S")

        # Check if the string is in the format 'yyyy-MM-ddTHH:mm:ss.SSS'
        elif (
            str.count("-") == 2
            and str.count(":") == 2
            and str.count("T") == 1
            and str.count(".") == 1
        ):
            return datetime.datetime.strptime(str, "%Y-%m-%dT%H:%M:%S.%f")

        # If the string doesn't match any of the above formats, raise an exception
        else:
            raise ValueError("Invalid date format")

    @staticmethod
    def createClass(classname: str) -> typing.Type[typing.Any]:
        try:
            return globals()[classname]
        except KeyError:
            raise ParseException("Unable to find the class: " + classname)
