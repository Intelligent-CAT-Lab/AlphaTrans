from __future__ import annotations
import time
import re
import pathlib
import io
import numbers
import typing
from typing import *
from datetime import datetime, date
import urllib
import inspect
import builtins
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *


class GlobalStateSync(type):
    """
    Syncs globals() whenever any member is accessed. 
    """
    def __getattribute__(cls, name):
        globals().update(inspect.currentframe().f_back.f_globals)
        return object.__getattribute__(cls, name)


class TypeHandler(metaclass=GlobalStateSync):

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
        return TypeHandler.createValue0(str_, obj)

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
            result = urllib.parse.urlparse(str_)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Invalid URL")
            if not result.scheme in ["http", "https", "ftp", "nntp", "file", "jar"]:
                raise ValueError("Unsupported URL scheme")
            return result
        except ValueError:
            raise ParseException("Unable to parse the URL: " + str_)

    @staticmethod
    def createObject(classname: str) -> typing.Any:
        
        try:
            classes_source = dict()
            classes_source.update(globals())
            classes_source.update(vars(builtins))
            cl = classes_source[classname]
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
        raise NotImplementedError("Not yet implemented")

    @staticmethod
    def createFile(str_: str) -> pathlib.Path:
        return pathlib.Path(str_)

    @staticmethod
    def createDate(str_: str) -> typing.Union[datetime, date]:
        raise NotImplementedError("Not yet implemented")

    @staticmethod
    def createClass(classname: str) -> typing.Type[typing.Any]:
        try:
            classes_source = dict()
            classes_source.update(globals())
            classes_source.update(vars(builtins))
            return classes_source[classname]
        except KeyError:
            raise ParseException("Unable to find the class: " + classname)
