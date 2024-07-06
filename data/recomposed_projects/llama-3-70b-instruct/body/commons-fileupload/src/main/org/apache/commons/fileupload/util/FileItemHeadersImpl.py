from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *


class FileItemHeadersImpl(FileItemHeaders):

    __headerNameToValueListMap: typing.Dict[str, typing.List[str]] = {}

    __serialVersionUID: int = -4455695752627032559

    def getHeaders(self, name: str) -> typing.Iterator[str]:
        name_lower = name.lower()
        header_value_list = self.__headerNameToValueListMap.get(name_lower)
        if header_value_list is None:
            header_value_list = []
        return iter(header_value_list)

    def getHeaderNames(self) -> typing.Iterator[str]:
        return self.__headerNameToValueListMap.keys()

    def getHeader(self, name: str) -> str:
        name_lower = name.lower()
        header_value_list = self.__headerNameToValueListMap.get(name_lower)
        if header_value_list is None:
            return None
        return header_value_list[0]

    def addHeader(self, name: str, value: str) -> None:
        name_lower = name.lower()
        header_value_list = self.__headerNameToValueListMap.get(name_lower)
        if header_value_list is None:
            header_value_list = []
            self.__headerNameToValueListMap[name_lower] = header_value_list
        header_value_list.append(value)
