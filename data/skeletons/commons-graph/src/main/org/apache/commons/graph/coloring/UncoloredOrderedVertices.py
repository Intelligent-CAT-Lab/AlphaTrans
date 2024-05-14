# Imports Begin
import typing

# Imports End


class UncoloredOrderedVertices(Iterable, Comparator):

    # Class Fields Begin
    __orderedVertices: typing.Dict[int, typing.Set[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def size(self) -> int:
        pass

    def iterator(self) -> typing.Iterator[typing.Any]:
        pass

    def compare(self, o1: int, o2: int) -> int:
        pass

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:
        pass

    # Class Methods End


class Iterator:

    # Class Fields Begin
    __keys: typing.Iterator[int] = None
    __pending: typing.Iterator[typing.Any] = None
    __next: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def remove(self) -> None:
        pass

    def next(self) -> typing.Any:
        pass

    def hasNext(self) -> bool:
        pass

    # Class Methods End
