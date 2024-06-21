from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfoMBean import *


class DefaultPooledObjectInfo(DefaultPooledObjectInfoMBean):

    __pooledObject: PooledObject[typing.Any] = None

    __PATTERN: str = "yyyy-MM-dd HH:mm:ss Z"

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("DefaultPooledObjectInfo [pooledObject=")
        builder.write(str(self.__pooledObject))
        builder.write("]")
        return builder.getvalue()

    def getPooledObjectType(self) -> str:

        return self.__pooledObject.getObject().__class__.__name__

    def getPooledObjectToString(self) -> str:

        if self.__pooledObject is None:
            return ""

        return str(self.__pooledObject.getObject())

    def getLastReturnTimeFormatted(self) -> str:

        return self.__getTimeFormatted(self.getLastReturnTime())

    def getLastReturnTime(self) -> int:

        return self.__pooledObject.getLastReturnInstant().toEpochMilli()

    def getLastBorrowTrace(self) -> str:

        sw = io.StringIO()
        pw = PrintWriter(sw)
        self.__pooledObject.printStackTrace(pw)
        return sw.getvalue()

    def getLastBorrowTimeFormatted(self) -> str:

        return self.__getTimeFormatted(self.getLastBorrowTime())

    def getLastBorrowTime(self) -> int:

        return self.__pooledObject.getLastBorrowInstant().toEpochMilli()

    def getCreateTimeFormatted(self) -> str:

        return self.__getTimeFormatted(self.getCreateTime())

    def getCreateTime(self) -> int:

        return self.__pooledObject.getCreateInstant().toEpochMilli()

    def getBorrowedCount(self) -> int:

        return self.__pooledObject.getBorrowedCount()

    def __init__(self, pooledObject: PooledObject[typing.Any]) -> None:

        self.__pooledObject = pooledObject

    def __getTimeFormatted(self, millis: int) -> str:

        from datetime import datetime

        return datetime.fromtimestamp(millis / 1000.0).strftime(self.__PATTERN)
