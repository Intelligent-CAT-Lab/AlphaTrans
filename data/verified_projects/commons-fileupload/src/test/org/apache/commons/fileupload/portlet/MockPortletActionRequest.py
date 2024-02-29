# Imports Begin
import typing
from typing import *
from io import BytesIO, BufferedReader
import locale
from fileupload.portlet import FileUploadBase

# Imports End


class MockPortletActionRequest:

    # Class Fields Begin
    # Class Fields End
    def __init__(self, requestLength: int, byteArrayInputStream: BytesIO, contentType: str):
        self.__attributes = {}
        self.__parameters = {}
        self.__characterEncoding = None
        self.__length = requestLength
        self.__contentType = contentType
        self.__requestData = byteArrayInputStream
        self.__attributes[FileUploadBase.CONTENT_TYPE] = contentType

    # Class Methods Begin
    @staticmethod
    def MockPortletActionRequest1(requestData: typing.List[int], contentType: str) -> MockPortletActionRequest:
        return MockPortletActionRequest(len(requestData), BytesIO(requestData), contentType)
    
    def getAttribute(self, key: str) -> typing.Any:
        return self.__attributes.get(key)
    
    def getAttributeNames(self) -> typing.Iterator[typing.Any]:
        return iter(self.__attributes.keys())
    
    def getAuthType(self) -> str:
        return None

    def getContextPath(self) -> str:
        return None
    
    def getLocale(self) -> typing.Any:
        return locale.getdefaultlocale()

    def getLocales(self) -> typing.Iterator[typing.Any]:
        available_locales = []
        for l in locale.locale_alias.items():
            try:
                available_locales.append(l)
            except:
                pass
        return iter(available_locales)
    
    def getParameter(self, key: str) -> str:
        return self.__parameters.get(key)
    
    def getParameterMap(self) -> typing.Dict[typing.Any, typing.Any]:
        return self.__parameters
    
    def getParameterNames(self) -> typing.Iterator[typing.Any]:
        return iter(self.__parameters.keys())
    
    def getParameterValues(self, arg0: str) -> typing.List[str]:
        return None

    def getProperties(self, arg0: str) -> typing.Iterator[typing.Any]:
        return None

    def getProperty(self, arg0: str) -> str:
        return None

    def getPropertyNames(self) -> typing.Iterator[typing.Any]:
        return None

    def getRemoteUser(self) -> str:
        return None

    def getRequestedSessionId(self) -> str:
        return None

    def getResponseContentType(self) -> str:
        return None

    def getResponseContentTypes(self) -> typing.Iterator[typing.Any]:
        return None

    def getScheme(self) -> str:
        return None

    def getServerName(self) -> str:
        return None

    def getServerPort(self) -> int:
        return 0

    def isRequestedSessionIdValid(self) -> bool:
        return False

    def isSecure(self) -> bool:
        return False

    def isUserInRole(self, arg0: str) -> bool:
        return False
    
    def removeAttribute(self, key: str) -> None:
        del self.__attributes[key]

    def setAttribute(self, key: str, value: typing.Any) -> None:
        self.__attributes[key] = value

    def getCharacterEncoding(self) -> str:
        return self.__characterEncoding

    def getContentLength(self) -> int:
        return self.__length
    
    def getContentType(self) -> str:
        return self.__contentType
    
    def getPortletInputStream(self) -> BytesIO:
        return self.__requestData
    
    def getReader(self) -> BufferedReader:
        return None
    
    def setCharacterEncoding(self, characterEncoding: str) -> None:
        self.__characterEncoding = characterEncoding

    # Class Methods End
