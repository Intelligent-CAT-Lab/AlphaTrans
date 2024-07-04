from __future__ import annotations
import time
import re
from abc import ABC
import io
import typing
from typing import *


class DefaultPooledObjectInfoMBean(ABC):

    def getPooledObjectType(self) -> str:
        pass

    def getPooledObjectToString(self) -> str:

        # Here you should implement the logic to convert the pooled object to a string.
        # Since the Java method is abstract, it's not clear what the actual implementation is.
        # So, I'll leave it as a placeholder.

        return "Pooled Object String"

    def getLastReturnTimeFormatted(self) -> str:

        from datetime import datetime

        last_return_time = self.getLastReturnTime()
        formatted_time = datetime.fromtimestamp(last_return_time / 1000.0).strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )

        return formatted_time

    def getLastReturnTime(self) -> int:
        pass

    def getLastBorrowTrace(self) -> str:
        pass

    def getLastBorrowTimeFormatted(self) -> str:

        # Assuming getLastBorrowTime() is a method in the same class
        last_borrow_time = self.getLastBorrowTime()

        # Convert the timestamp to a datetime object
        dt_object = datetime.fromtimestamp(last_borrow_time / 1e3)

        # Format the datetime object to a string
        formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")

        return formatted_time

    def getLastBorrowTime(self) -> int:
        pass

    def getCreateTimeFormatted(self) -> str:

        # Assuming getCreateTime() is a method in the same class
        create_time = self.getCreateTime()

        # Convert the create_time to a datetime object
        from datetime import datetime

        dt_object = datetime.fromtimestamp(create_time / 1e3)

        # Format the datetime object to a string
        return dt_object.strftime("%Y-%m-%d %H:%M:%S")

    def getCreateTime(self) -> int:
        pass

    def getBorrowedCount(self) -> int:
        pass
