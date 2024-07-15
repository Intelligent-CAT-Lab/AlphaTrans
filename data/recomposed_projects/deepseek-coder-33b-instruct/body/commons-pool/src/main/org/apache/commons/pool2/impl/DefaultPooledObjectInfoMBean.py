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
        pass

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

        from datetime import datetime

        last_borrow_time = self.getLastBorrowTime()
        formatted_time = datetime.fromtimestamp(last_borrow_time / 1000.0).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        return formatted_time

    def getLastBorrowTime(self) -> int:
        pass

    def getCreateTimeFormatted(self) -> str:

        # Convert the create time to a datetime object
        create_time = datetime.fromtimestamp(self.getCreateTime() / 1000)

        # Format the datetime object to a string
        formatted_time = create_time.strftime("%Y-%m-%d %H:%M:%S")

        return formatted_time

    def getCreateTime(self) -> int:
        pass

    def getBorrowedCount(self) -> int:
        pass
