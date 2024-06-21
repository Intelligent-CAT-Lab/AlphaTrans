from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.DestroyMode import *


class ObjectPool(ABC):

    def returnObject(self, obj: typing.Any) -> None:

        # Your code here
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:

        # Your code here
        pass

    def getNumIdle(self) -> int:

        pass

    def getNumActive(self) -> int:

        # Your implementation here
        pass

    def close(self) -> None:

        pass

    def clear(self) -> None:

        # Python does not have built-in support for checked exceptions, so we can just raise the exception
        raise Exception("Method not implemented")

    def borrowObject(self) -> typing.Any:

        try:
            # Your code here
            pass
        except Exception as e:
            raise e
        except NoSuchElementException as e:
            raise e
        except IllegalStateException as e:
            raise e

    def addObject(self) -> None:

        try:
            # Your code here
            pass
        except Exception as e:
            raise e
        except IllegalStateException as e:
            raise e
        except NotImplementedError as e:
            raise e

    def invalidateObject1(self) -> None:

        def invalidateObject0(self, obj: typing.Any) -> None:
            pass

        try:
            invalidateObject0(obj)
        except Exception as e:
            raise e

    def addObjects(self) -> None:

        for i in range(count):
            self.addObject()
