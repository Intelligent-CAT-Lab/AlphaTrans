# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import typing
from typing import *

# Imports End


class FileItemHeadersImpl(Serializable, FileItemHeaders):

    # Class Fields Begin
    __version: str = "1.0.0"
    headerNameToValueListMap: Dict[str, List[str]] = {}
    # Class Fields End

    # Class Methods Begin
    def getHeaders(self, name: str) -> typing.Iterator[str]:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower)
        if headerValueList is None:
            headerValueList = []
        return iter(headerValueList)

    def getHeaderNames(self) -> typing.Iterator[str]:

        return self.__headerNameToValueListMap.keys()

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

    # Class Methods End
