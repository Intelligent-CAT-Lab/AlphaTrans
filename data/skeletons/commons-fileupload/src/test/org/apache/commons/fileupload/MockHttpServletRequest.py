from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib

# Imports End


class MyServletInputStream:

    # Class Fields Begin
    __in: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __readLimit: int = None
    # Class Fields End

    # Class Methods Begin
    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def __init__(
        self,
        pStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        readLimit: int,
    ) -> None:
        pass

    # Class Methods End


class MockHttpServletRequest:

    # Class Fields Begin
    __m_requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __length: int = None
    __m_strContentType: str = None
    __readLimit: int = None
    __m_headers: typing.Dict[str, str] = None
    # Class Fields End

    # Class Methods Begin
    def getRealPath(self, arg0: str) -> str:
        pass

    def getLocalAddr(self) -> str:
        pass

    def getRemotePort(self) -> int:
        pass

    def getLocalPort(self) -> int:
        pass

    def getLocalName(self) -> str:
        pass

    def isRequestedSessionIdFromUrl(self) -> bool:
        pass

    def isSecure(self) -> bool:
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

    def removeAttribute(self, arg0: str) -> None:
        pass

    def setAttribute(self, arg0: str, arg1: typing.Any) -> None:
        pass

    def getRemoteHost(self) -> str:
        pass

    def getRemoteAddr(self) -> str:
        pass

    def getReader(self) -> io.BufferedReader:
        pass

    def getServerPort(self) -> int:
        pass

    def getServerName(self) -> str:
        pass

    def getScheme(self) -> str:
        pass

    def getProtocol(self) -> str:
        pass

    def getParameterMap(self) -> typing.Dict[str, typing.List[str]]:
        pass

    def getParameterValues(self, arg0: str) -> typing.List[typing.List[str]]:
        pass

    def getParameterNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        pass

    def getParameter(self, arg0: str) -> str:
        pass

    def setReadLimit(self, readLimit: int) -> None:
        pass

    def getContentType(self) -> str:
        pass

    def setContentLength(self, length: int) -> None:
        pass

    def getContentLength(self) -> int:
        pass

    def setCharacterEncoding(self, arg0: str) -> None:
        pass

    def getCharacterEncoding(self) -> str:
        pass

    def getAttributeNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        pass

    def getAttribute(self, arg0: str) -> typing.Any:
        pass

    def isRequestedSessionIdFromURL(self) -> bool:
        pass

    def isRequestedSessionIdFromCookie(self) -> bool:
        pass

    def isRequestedSessionIdValid(self) -> bool:
        pass

    def getServletPath(self) -> str:
        pass

    def getRequestURL(self) -> io.StringIO:
        pass

    def getRequestURI(self) -> str:
        pass

    def getRequestedSessionId(self) -> str:
        pass

    def isUserInRole(self, arg0: str) -> bool:
        pass

    def getRemoteUser(self) -> str:
        pass

    def getQueryString(self) -> str:
        pass

    def getContextPath(self) -> str:
        pass

    def getPathTranslated(self) -> str:
        pass

    def getPathInfo(self) -> str:
        pass

    def getMethod(self) -> str:
        pass

    def getHeaderNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        pass

    def getHeaders(
        self, arg0: str
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        pass

    def getHeader(self, headerName: str) -> str:
        pass

    def getDateHeader(self, arg0: str) -> int:
        pass

    def getAuthType(self) -> str:
        pass

    @staticmethod
    def MockHttpServletRequest1(
        requestData: typing.List[int], strContentType: str
    ) -> MockHttpServletRequest:
        pass

    def __init__(
        self,
        constructorId: int,
        requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        strContentType: str,
        requestLength: int,
    ) -> None:
        pass

    # Class Methods End
