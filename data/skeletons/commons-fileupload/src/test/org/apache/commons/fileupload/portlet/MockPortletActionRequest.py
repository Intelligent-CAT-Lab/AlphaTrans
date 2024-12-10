from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib

# Imports End


class MockPortletActionRequest:

    # Class Fields Begin
    __attributes: typing.Dict[str, typing.Any] = None
    __parameters: typing.Dict[str, str] = None
    __characterEncoding: str = None
    __length: int = None
    __contentType: str = None
    __requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    # Class Fields End

    # Class Methods Begin
    def setCharacterEncoding(self, characterEncoding: str) -> None:
        pass

    def getReader(self) -> io.BufferedReader:
        pass

    def getPortletInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass

    def getContentType(self) -> str:
        pass

    def getContentLength(self) -> int:
        pass

    def getCharacterEncoding(self) -> str:
        pass

    def setAttribute(self, key: str, value: typing.Any) -> None:
        pass

    def removeAttribute(self, key: str) -> None:
        pass

    def isUserInRole(self, arg0: str) -> bool:
        pass

    def isSecure(self) -> bool:
        pass

    def isRequestedSessionIdValid(self) -> bool:
        pass

    def getServerPort(self) -> int:
        pass

    def getServerName(self) -> str:
        pass

    def getScheme(self) -> str:
        pass

    def getResponseContentTypes(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getResponseContentType(self) -> str:
        pass

    def getRequestedSessionId(self) -> str:
        pass

    def getRemoteUser(self) -> str:
        pass

    def getPropertyNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getProperty(self, arg0: str) -> str:
        pass

    def getProperties(self, arg0: str) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getParameterValues(self, arg0: str) -> typing.List[typing.List[str]]:
        pass

    def getParameterNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getParameterMap(self) -> typing.Dict[typing.Any, typing.Any]:
        pass

    def getParameter(self, key: str) -> str:
        pass

    def getLocales(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getLocale(self) -> typing.Any:
        pass

    def getContextPath(self) -> str:
        pass

    def getAuthType(self) -> str:
        pass

    def getAttributeNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:
        pass

    def getAttribute(self, key: str) -> typing.Any:
        pass

    @staticmethod
    def MockPortletActionRequest1(
        requestData: typing.List[int], contentType: str
    ) -> MockPortletActionRequest:
        pass

    def __init__(
        self,
        requestLength: int,
        byteArrayInputStream: typing.Union[io.BytesIO, bytearray],
        contentType: str,
    ) -> None:
        pass

    # Class Methods End
