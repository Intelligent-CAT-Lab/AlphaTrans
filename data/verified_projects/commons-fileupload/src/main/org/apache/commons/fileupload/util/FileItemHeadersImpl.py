import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import typing
from typing import *

# Imports End


class FileItemHeadersImpl(FileItemHeaders):

    # Class Fields Begin
    __serialVersionUID: int = -4455695752627032559
    __headerNameToValueListMap: typing.Dict[str, typing.List[str]] = {}
    # Class Fields End

    # Class Methods Begin
    def getHeaders(self, name: str) -> typing.Iterator[str]:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            headerValueList = []
        return iter(headerValueList)

    def getHeaderNames(self) -> typing.Iterator[str]:

        return iter(self.__headerNameToValueListMap.keys())

    def getHeader(self, name: str) -> str:

        name_lower = name.lower()
        header_value_list = self.__headerNameToValueListMap.get(name_lower)
        if header_value_list is None:
            return None
        return header_value_list[0]

    def addHeader(self, name: str, value: str) -> None:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            headerValueList = []
            self.__headerNameToValueListMap[nameLower] = headerValueList
        headerValueList.append(value)

    # Class Methods End
