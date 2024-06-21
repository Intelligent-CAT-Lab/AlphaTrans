from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.UsageTracking import *


class BaseProxyHandler:

    __usageTracking: UsageTracking[typing.Any] = None
    __pooledObject: typing.Any = None

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write(self.__class__.__name__)
        builder.write(" [pooledObject=")
        builder.write(str(self.__pooledObject))
        builder.write(", usageTracking=")
        builder.write(str(self.__usageTracking))
        builder.write("]")
        return builder.getvalue()

    def validateProxiedObject(self) -> None:

        if self.__pooledObject is None:
            raise IllegalStateException(
                "This object may no longer be "
                + "used as it has been returned to the Object Pool."
            )

    def getPooledObject(self) -> typing.Any:

        return self.__pooledObject

    def doInvoke(
        self,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:

        self.validateProxiedObject()
        object = self.getPooledObject()
        if self.__usageTracking is not None:
            self.__usageTracking.use(object)
        return method(object, *args)

    def disableProxy(self) -> typing.Any:

        result = self.__pooledObject
        self.__pooledObject = None
        return result

    def __init__(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> None:

        self.__pooledObject = pooledObject
        self.__usageTracking = usageTracking
