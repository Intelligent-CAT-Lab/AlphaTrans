# Imports Begin
from commons.fileupload.src.test.java.org.apache.commons.fileupload.MockHttpServletRequest import (
    MockHttpServletRequest,
)
from commons.fileupload.src.test.java.org.apache.commons.fileupload.MyServletInputStream import (
    MyServletInputStream,
)
import unittest
import typing
from typing import *
import io
import pathlib

# Imports End


class MockHttpServletRequest(unittest.TestCase):

    # Class Fields Begin
    __m_requestData: io.BytesIO = None
    __length: int = None
    __m_strContentType: str = None
    __readLimit: int = -1
    __m_headers: Dict[str, str] = {}
    # Class Fields End

    # Class Methods Begin
    def getRealPath(self, arg0: str) -> str:

        pass  # LLM could not translate method body

    def getLocalAddr(self) -> str:

        return None

    def getRemotePort(self) -> int:

        return 0

    def getLocalPort(self) -> int:

        return 0

    def getLocalName(self) -> str:

        return None

    def isRequestedSessionIdFromUrl(self) -> bool:

        return False

    def isSecure(self) -> bool:

        return False

    def getLocales(self) -> typing.Iterator[typing.Any]:

        pass  # LLM could not translate method body

    def getLocale(self) -> typing.Any:

        pass  # LLM could not translate method body

    def removeAttribute(self, arg0: str) -> None:

        pass  # LLM could not translate method body

    def setAttribute(self, arg0: str, arg1: object) -> None:

        pass

    def getRemoteHost(self) -> str:

        return None

    def getRemoteAddr(self) -> str:

        return None

    def getReader(self) -> io.BufferedReader:

        return None

    def getServerPort(self) -> int:

        pass  # LLM could not translate method body

    def getServerName(self) -> str:

        return None

    def getScheme(self) -> str:

        return None

    def getProtocol(self) -> str:

        return None

    def getParameterMap(self) -> typing.Dict[str, typing.List[str]]:

        pass  # LLM could not translate method body

    def getParameterValues(self, arg0: str) -> typing.List[str]:

        return None

    def getParameterNames(self) -> typing.Iterator[str]:

        pass  # LLM could not translate method body

    def getParameter(self, arg0: str) -> str:

        return None

    def setReadLimit(self, readLimit: int) -> None:

        self.__readLimit = readLimit

    def getContentType(self) -> str:

        return self.__m_strContentType

    def setContentLength(self, length: int) -> None:

        self.__length = length

    def getContentLength(self) -> int:

        pass  # LLM could not translate method body

    def setCharacterEncoding(self, arg0: str) -> None:

        raise UnsupportedEncodingException

    def getCharacterEncoding(self) -> str:

        return None

    def getAttributeNames(self) -> typing.Iterator[str]:

        pass  # LLM could not translate method body

    def getAttribute(self, arg0: str) -> object:

        pass  # LLM could not translate method body

    def isRequestedSessionIdFromURL(self) -> bool:

        return False

    def isRequestedSessionIdFromCookie(self) -> bool:

        return False

    def isRequestedSessionIdValid(self) -> bool:

        return False

    def getServletPath(self) -> str:

        return None

    def getRequestURL(self) -> str:

        return None

    def getRequestURI(self) -> str:

        return None

    def getRequestedSessionId(self) -> str:

        return None

    def isUserInRole(self, arg0: str) -> bool:

        return False

    def getRemoteUser(self) -> str:

        pass  # LLM could not translate method body

    def getQueryString(self) -> str:

        return None

    def getContextPath(self) -> str:

        pass  # LLM could not translate method body

    def getPathTranslated(self) -> str:

        pass  # LLM could not translate method body

    def getPathInfo(self) -> str:

        return None

    def getMethod(self) -> str:

        return None

    def getHeaderNames(self) -> typing.Iterator[str]:

        pass  # LLM could not translate method body

    def getHeaders(self, arg0: str) -> typing.Iterator[str]:

        pass  # LLM could not translate method body

    def getHeader(self, headerName: str) -> str:

        return self.__m_headers.get(headerName)

    def getDateHeader(self, arg0: str) -> int:

        return 0

    def getAuthType(self) -> str:

        return None

    @staticmethod
    def MockHttpServletRequest1(
        requestData: typing.List[int], strContentType: str
    ) -> MockHttpServletRequest:

        return MockHttpServletRequest(
            0, io.BytesIO(requestData), strContentType, len(requestData)
        )

    def __init__(
        self,
        constructorId: int,
        requestData: io.BytesIO,
        strContentType: str,
        requestLength: int,
    ) -> None:

        if constructorId == 0:
            self.__m_requestData = requestData
            self.__length = requestLength
            self.__m_strContentType = strContentType
            self.__m_headers[FileUploadBase.CONTENT_TYPE] = strContentType
        else:
            self.__m_requestData = requestData
            self.__length = requestLength
            self.__m_strContentType = strContentType
            self.__m_headers[FileUploadBase.CONTENT_TYPE] = strContentType

    # Class Methods End


class MyServletInputStream(unittest.TestCase):

    # Class Fields Begin
    __in: io.BytesIO = None
    __readLimit: int = None
    # Class Fields End

    # Class Methods Begin
    def read1(self, b: typing.List[int], off: int, len: int) -> int:

        if self.__readLimit > 0:
            return self.__in.read(b, off, min(self.__readLimit, len))
        return self.__in.read(b, off, len)

    def read0(self) -> int:

        return self.__in.read()

    def __init__(self, pStream: io.BytesIO, readLimit: int) -> None:

        self.__in = pStream
        self.__readLimit = readLimit

    # Class Methods End
