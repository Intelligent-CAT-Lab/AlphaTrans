from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *


class FileItemHeadersImpl(FileItemHeaders):

    __serialVersionUID: int = -4455695752627032559

    def getHeaders(self, name: str) -> typing.Iterator[str]:
        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            headerValueList = []
        return iter(headerValueList)

    def getHeaderNames(self) -> typing.Iterator[str]:
        return iter(self.__headerNameToValueListMap.keys())

    def getHeader(self, name: str) -> str:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            return None
        return headerValueList[0]

    def addHeader(self, name: str, value: str) -> None:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            headerValueList = []
            self.__headerNameToValueListMap[nameLower] = headerValueList
        headerValueList.append(value)

    def __init__(self) -> None:
        super().__init__()
        self.__headerNameToValueListMap: typing.Dict[str, typing.List[str]] = {}
