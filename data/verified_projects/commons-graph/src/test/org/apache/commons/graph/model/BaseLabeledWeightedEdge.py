import pytest

from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import BaseLabeledEdge
import typing
from typing import *

W = typing.TypeVar('W')


class BaseLabeledWeightedEdge(BaseLabeledEdge, typing.Generic[W]):

    __serialVersionUID: int = 5935967858178091436

    
    def __init__(self, label: str, weight: W) -> None:
        super().__init__(label)
        self.__weight = Assertions.checkNotNull(weight, "Argument 'weight' must not be null")


    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True
        
        if not super().equals(obj):
            return False
        
        if type(self) != type(obj):
            return False
        
        other = obj

        return Objects.eq(self.__weight, other.getWeight())

    
    def getWeight(self) -> W:
        return self.__weight
    
    
    def hashCode(self) -> int:
        return Objects.hash(super().hashCode(), 31, self.__weight)

    
    def toString(self) -> str:
        return f"{self.getLabel()} ({self.__weight})"
