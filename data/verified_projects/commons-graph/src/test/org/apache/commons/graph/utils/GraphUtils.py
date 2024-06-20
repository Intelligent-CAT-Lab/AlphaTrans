import pytest

from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.GraphException import *
import typing
from typing import *



class GraphUtils:

    def __init__(self) -> None:
        pass


    @staticmethod
    def buildBipartedGraph(nVertices, g) -> None:
        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        fistPartition = []
        secondPartition = []

        count = 0
        for v1 in g.getVertices0():
            if count == nVertices // 2:
                count += 1
                break
            count += 1
            fistPartition.append(v1)

        count = 0
        for v2 in g.getVertices0():
            if count < nVertices // 2:
                count += 1
                continue
            count += 1
            secondPartition.append(v2)

        for v1 in fistPartition:
            for v2 in secondPartition:
                if not v1.equals(v2):
                    try:
                        g.addEdge(v1, BaseLabeledEdge(f"{v1} -> {v2}"), v2)
                    except GraphException:
                        pass

    
    @staticmethod
    def buildCompleteGraph(nVertices, g) -> None:
        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        for v1 in g.getVertices0():
            for v2 in g.getVertices0():
                if not v1.equals(v2):
                    try:
                        g.addEdge(v1, BaseLabeledEdge(f"{v1} -> {v2}"), v2)
                    except GraphException:
                        pass
    
    
    @staticmethod
    def buildCrownGraph(nVertices, g) -> None:
        tmp = []

        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
            tmp.append(v)

        for i in range(nVertices):
            next = i + 1
            if i == (nVertices - 1):
                next = 0
            e = BaseLabeledEdge(f"{i} -> {next}")
            try:
                g.addEdge(tmp[i], e, tmp[next])
            except GraphException:
                pass

    
    @staticmethod
    def buildSudokuGraph(sudoku) -> typing.List[typing.List[BaseLabeledVertex]]:
        grid = [[None for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                grid[row][col] = BaseLabeledVertex(f"{row}, {col}")
                sudoku.addVertex(grid[row][col])

        rowsOffsets = [0, 3, 6]
        colsOffsets = [0, 3, 6]

        for rof in range(3):
            for cof in range(3):
                boxes = []
                for row in range(rowsOffsets[rof], 3 + rowsOffsets[rof]):
                    for col in range(colsOffsets[cof], 3 + colsOffsets[cof]):
                        boxes.append(grid[row][col])

                for v1 in boxes:
                    for v2 in boxes:
                        e = BaseLabeledEdge(f"{v1} -> {v2}")
                        if not v1.equals(v2):
                            try:
                                sudoku.addEdge(v1, e, v2)
                            except GraphException:
                                pass

        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1 = grid[j][i]
                    v2 = grid[j][h]

                    if not v1.equals(v2):
                        e = BaseLabeledEdge(f"{v1} -> {v2}")
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass

        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1 = grid[i][j]
                    v2 = grid[h][j]

                    if not v1.equals(v2):
                        e = BaseLabeledEdge(f"{v1} -> {v2}")
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass

        return grid
