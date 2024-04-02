# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import unittest
import typing
from typing import *
from io import BytesIO
import io
import pathlib

# Imports End


class MockPortletActionRequest(unittest.TestCase):

    # Class Fields Begin
    __attributes: Dict[str, object] = {}
    __parameters: Dict[str, str] = {}
    __characterEncoding: str = None
    __length: int = None
    __contentType: str = None
    __requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    # Class Fields End

    # Class Methods Begin
    def setCharacterEncoding(self, characterEncoding: str) -> None:

        self.__characterEncoding = characterEncoding

    def getReader(self) -> io.BufferedReader:

        return None

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

        self.__attributes.pop(key, None)

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

        return None

    def getResponseContentType(self) -> str:

        return None

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

        return iter([])

    def getProperty(self, arg0: str) -> str:

        return None

    def getProperties(self, arg0: str) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:

        return None

    def getParameterValues(self, arg0: str) -> typing.List[str]:

        return None

    def getParameterNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:

        return iter(self.__parameters.keys())

    def getParameterMap(self) -> typing.Dict[typing.Any, typing.Any]:

        return self.__parameters

    def getParameter(self, key: str) -> str:

        return self.__parameters.get(key)

    def getLocales(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any],
        typing.Generator[typing.Any, typing.Any, typing.Any],
    ]:

        return iter(locale.get_available_locales())

    def getLocale(self) -> typing.Any:

        pass  # LLM could not translate method body

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
    ) -> "MockPortletActionRequest":

        pass  # LLM could not translate method body

    def __init__(
        self,
        requestLength: int,
        byteArrayInputStream: typing.Union[io.BytesIO, bytearray],
        contentType: str,
    ) -> None:

        self.__requestData = byteArrayInputStream
        self.__length = requestLength
        self.__contentType = contentType
        self.__attributes = {}
        self.__attributes[FileUploadBase.CONTENT_TYPE] = contentType

    # Class Methods End
