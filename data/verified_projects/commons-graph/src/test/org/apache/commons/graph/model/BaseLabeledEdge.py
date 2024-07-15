import pytest

from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
import typing
from typing import *


class BaseLabeledEdge:

    __serialVersionUID: int = -4985890761880816592

    def __init__(self, label: str) -> None:
        self.__label = Assertions.checkNotNull(label, "Argument 'label' must not be null")

    
    def equals(self, obj: typing.Any) -> bool:
        if self is obj:
            return True
        
        if obj is None or type(self) != type(obj):
            return False
        
        other = obj

        return Objects.eq(self.__label, other.getLabel())

    
    def getLabel(self) -> str:
        return self.__label
    
    
    def hashCode(self) -> int:
        return Objects.hash(1, 31, self.__label)

    
    def toString(self) -> str:
        return f"{self.getLabel()}()"
