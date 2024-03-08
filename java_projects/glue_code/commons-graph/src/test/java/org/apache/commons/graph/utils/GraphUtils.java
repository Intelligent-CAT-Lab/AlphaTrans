package org.apache.commons.graph;

import org.apache.commons.graph.model.BaseLabeledEdge;
import org.apache.commons.graph.model.BaseLabeledVertex;
import org.apache.commons.graph.model.BaseMutableGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.graalvm.polyglot.Value;

public class GraphUtils {
  private static Value clz = ContextInitializer.getPythonClass("/GraphUtils.py", "GraphUtils");
  private Value obj;

  public GraphUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static BaseLabeledVertex[][] buildSudokuGraph(
      UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> sudoku) {
    //
    // BaseLabeledVertex[][] grid = new BaseLabeledVertex[9][9];
    // for (int row = 0; row < 9; row++) {
    // for (int col = 0; col < 9; col++) {
    // grid[row][col] = new BaseLabeledVertex(format("%s, %s", row, col));
    // sudoku.addVertex(grid[row][col]);
    // }
    // }
    //
    // int[] rowsOffsets = new int[] {0, 3, 6};
    // int[] colsOffsets = new int[] {0, 3, 6};
    //
    // for (int rof = 0; rof < 3; rof++) {
    // for (int cof = 0; cof < 3; cof++) {
    // List<BaseLabeledVertex> boxes = new ArrayList<BaseLabeledVertex>();
    // for (int row = rowsOffsets[rof]; row < 3 + rowsOffsets[rof]; row++) {
    // for (int col = colsOffsets[cof]; col < 3 + colsOffsets[cof]; col++) {
    // boxes.add(grid[row][col]);
    // }
    // }
    //
    // for (BaseLabeledVertex v1 : boxes) {
    // for (BaseLabeledVertex v2 : boxes) {
    //
    // BaseLabeledEdge e = new BaseLabeledEdge(format("%s -> %s", v1, v2));
    // if (!v1.equals(v2)) {
    // try {
    // sudoku.addEdge(v1, e, v2);
    // } catch (GraphException ge) {
    // }
    // }
    // }
    // }
    // }
    // }
    //
    // for (int j = 0; j < 9; j++) {
    // for (int i = 0; i < 9; i++) {
    // for (int h = 0; h < 9; h++) {
    // BaseLabeledVertex v1 = grid[j][i];
    // BaseLabeledVertex v2 = grid[j][h];
    //
    // if (!v1.equals(v2)) {
    // BaseLabeledEdge e = new BaseLabeledEdge(format("%s -> %s", v1, v2));
    // try {
    // sudoku.addEdge(v1, e, v2);
    // } catch (GraphException ge) {
    // }
    // }
    // }
    // }
    // }
    //
    // for (int j = 0; j < 9; j++) {
    // for (int i = 0; i < 9; i++) {
    // for (int h = 0; h < 9; h++) {
    // BaseLabeledVertex v1 = grid[i][j];
    // BaseLabeledVertex v2 = grid[h][j];
    //
    // if (!v1.equals(v2)) {
    // BaseLabeledEdge e = new BaseLabeledEdge(format("%s -> %s", v1, v2));
    // try {
    // sudoku.addEdge(v1, e, v2);
    // } catch (GraphException ge) {
    // }
    // }
    // }
    // }
    // }
    // return grid;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("buildSudokuGraph", sudoku).as(BaseLabeledVertex[][].class);
  }

  public static void buildCrownGraph(
      int nVertices, UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g) {
    //
    // List<BaseLabeledVertex> tmp = new ArrayList<BaseLabeledVertex>();
    //
    // for (int i = 0; i < nVertices; i++) {
    // BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
    // g.addVertex(v);
    // tmp.add(v);
    // }
    //
    // for (int i = 0; i < nVertices; i++) {
    // int next = i + 1;
    // if (i == (nVertices - 1)) {
    // next = 0;
    // }
    // BaseLabeledEdge e = new BaseLabeledEdge(format("%s -> %s", i, next));
    // try {
    // g.addEdge(tmp.get(i), e, tmp.get(next));
    // } catch (GraphException ge) {
    // }
    // }
    //

    clz.invokeMember("buildCrownGraph", nVertices, g);
  }

  public static void buildCompleteGraph(
      int nVertices, BaseMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g) {
    //
    // for (int i = 0; i < nVertices; i++) {
    // BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
    // g.addVertex(v);
    // }
    //
    // for (BaseLabeledVertex v1 : g.getVertices0()) {
    // for (BaseLabeledVertex v2 : g.getVertices0()) {
    // if (!v1.equals(v2)) {
    // try {
    // g.addEdge(v1, new BaseLabeledEdge(format("%s -> %s", v1, v2)), v2);
    // } catch (GraphException e) {
    // }
    // }
    // }
    // }
    //

    clz.invokeMember("buildCompleteGraph", nVertices, g);
  }

  public static void buildBipartedGraph(
      int nVertices, UndirectedMutableGraph<BaseLabeledVertex, BaseLabeledEdge> g) {
    //
    // for (int i = 0; i < nVertices; i++) {
    // BaseLabeledVertex v = new BaseLabeledVertex(valueOf(i));
    // g.addVertex(v);
    // }
    //
    // List<BaseLabeledVertex> fistPartition = new ArrayList<BaseLabeledVertex>();
    // List<BaseLabeledVertex> secondPartition = new ArrayList<BaseLabeledVertex>();
    //
    // int count = 0;
    // for (BaseLabeledVertex v1 : g.getVertices0()) {
    // if (count++ == nVertices / 2) {
    // break;
    // }
    // fistPartition.add(v1);
    // }
    //
    // count = 0;
    // for (BaseLabeledVertex v2 : g.getVertices0()) {
    // if (count++ < nVertices / 2) {
    // continue;
    // }
    // secondPartition.add(v2);
    // }
    //
    // for (BaseLabeledVertex v1 : fistPartition) {
    // for (BaseLabeledVertex v2 : secondPartition) {
    // if (!v1.equals(v2)) {
    // try {
    // g.addEdge(v1, new BaseLabeledEdge(format("%s -> %s", v1, v2)), v2);
    // } catch (GraphException e) {
    // }
    // }
    // }
    // }
    //

    clz.invokeMember("buildBipartedGraph", nVertices, g);
  }

  private GraphUtils() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
