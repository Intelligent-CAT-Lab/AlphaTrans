# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.DefaultTailVertexConnector import *
from src.main.org.apache.commons.graph.MutableGraph import *
import typing

# Imports End


class DefaultHeadVertexConnector(HeadVertexConnector):

    # Class Fields Begin
    __graph: MutableGraph[typing.Any, typing.Any] = None
    __edge: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def from_(self, head: typing.Any) -> TailVertexConnector[typing.Any, typing.Any]:
        pass

    def __init__(
        self, graph: MutableGraph[typing.Any, typing.Any], edge: typing.Any
    ) -> None:
        pass

    # Class Methods End
