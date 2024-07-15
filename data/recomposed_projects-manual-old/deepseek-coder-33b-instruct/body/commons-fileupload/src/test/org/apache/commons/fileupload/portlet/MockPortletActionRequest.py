from __future__ import annotations
import locale
import re
import unittest
import pytest
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *


class MockPortletActionRequest:

    __requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    __contentType: str = ""

    __length: int = 0

    __characterEncoding: str = ""

    __parameters: typing.Dict[str, str] = {}
    __attributes: typing.Dict[str, typing.Any] = {}

    def setCharacterEncoding(self, characterEncoding: str) -> None:
        self.__characterEncoding = characterEncoding

    def getReader(self) -> io.BufferedReader:

        # Check if the request data is a StringIO or BytesIO
        if isinstance(self.__requestData, (io.StringIO, io.BytesIO)):
            return io.BufferedReader(self.__requestData)

        # If the request data is a BufferedReader, return it as is
        elif isinstance(self.__requestData, io.BufferedReader):
            return self.__requestData

        # If the request data is None, raise an exception
        else:
            raise ValueError("Request data is not set")

    def getPortletInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        return self.__requestData

    def getContentType(self) -> str:
        return self.__contentType

    def getContentLength(self) -> int:
        return self.__length

    def getCharacterEncoding(self) -> str:
        return self.__characterEncoding

    def setAttribute(self, key: str, value: typing.Any) -> None:
        self.__attributes[key] = value

    def removeAttribute(self, key: str) -> None:
        if key in self.__attributes:
            del self.__attributes[key]

    def isUserInRole(self, arg0: str) -> bool:
        return False

    def isSecure(self) -> bool:
        return False

    def isRequestedSessionIdValid(self) -> bool:
        return False

    def getServerPort(self) -> int:
        return 0

    def getServerName(self) -> str:
        return None

    def getScheme(self) -> str:
        return None

    def getResponseContentTypes(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:

        # The Java method is returning an Enumeration, which is an interface in Java.
        # In Python, we can use a list or a generator to achieve the same functionality.
        # Here, we are returning a generator.

        for key, value in self.__attributes.items():
            yield key, value

    def getResponseContentType(self) -> str:
        return self.__contentType

    def getRequestedSessionId(self) -> str:
        return None

    def getRemoteUser(self) -> str:
        return None

    def getPropertyNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        return iter(self.__parameters.keys())

    def getProperty(self, arg0: str) -> str:
        return self.__parameters.get(arg0, None)

    def getProperties(self, arg0: str) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:

        # Python does not have a direct equivalent to Java's Enumeration.
        # Instead, we can use a list or a generator to mimic the behavior.
        # Here, we'll use a generator.

        # If you want to return a list, you can use the following code:
        # return list(self.__parameters.items())

        # If you want to return a generator, you can use the following code:
        return ((k, v) for k, v in self.__parameters.items())

    def getParameterValues(self, arg0: str) -> typing.List[str]:
        return list(self.__parameters.get(arg0, []))

    def getParameterNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        return iter(self.__parameters.keys())

    def getParameterMap(self) -> typing.Dict[typing.Any, typing.Any]:
        return dict(self.__parameters)

    def getParameter(self, key: str) -> str:
        return self.__parameters.get(key)

    def getLocales(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        return iter(Locale.getAvailableLocales())

    def getLocale(self) -> typing.Any:
        return locale.getdefaultlocale()

    def getContextPath(self) -> str:
        return None

    def getAuthType(self) -> str:
        return None

    def getAttributeNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        return iter(self.__attributes.keys())

    def getAttribute(self, key: str) -> typing.Any:
        return self.__attributes.get(key)

    @staticmethod
    def MockPortletActionRequest1(
        requestData: typing.List[int], contentType: str
    ) -> MockPortletActionRequest:

        byteArrayInputStream = BytesIO(bytes(requestData))
        return MockPortletActionRequest(
            len(requestData), byteArrayInputStream, contentType
        )

    def __init__(
        self,
        requestLength: int,
        byteArrayInputStream: typing.Union[io.BytesIO, bytearray],
        contentType: str,
    ) -> None:

        self.__requestData = byteArrayInputStream
        self.__length = requestLength
        self.__contentType = contentType
        self.__attributes[FileUploadBase.CONTENT_TYPE] = contentType
