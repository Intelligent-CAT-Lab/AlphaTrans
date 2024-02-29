# Imports Begin
'''Temmporary Solution: modify the sys.path list to include the directories where your modules are located.'''
import sys
sys.path.append('/Users/kekaiyao/Desktop/AlphaTrans/data/recomposed_projects/commons-fileupload/src/main/org/apache/commons/fileupload')
from FileItemHeaders import *
#from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import typing
from typing import *

# Imports End


"""java.io.Serializable is mapped to typing.Any, so this class should not inherit from it explicitly"""
class FileItemHeadersImpl(FileItemHeaders):

    # Class Fields Begin
    __version: str = "1.0.0"
    """LLM named the following Map `headerNameToValueListMap`, but later referenced it as `__headerNameToValueListMap` """
    __headerNameToValueListMap: Dict[str, List[str]] = {}
    # Class Fields End

    # Class Methods Begin
    def getHeaders(self, name: str) -> typing.Iterator[str]:

        nameLower = name.lower()
        headerValueList = self.__headerNameToValueListMap.get(nameLower) 
        if headerValueList is None:
            headerValueList = []
        return iter(headerValueList)

    def getHeaderNames(self) -> typing.Iterator[str]:

        """LLM returned the raw list rather than an Iterator"""
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

    # Class Methods End
