package org.apache.commons.graph.export;


public interface ExportSelector<V, E> {
  DotExporter<V, E> usingDotNotation() throws GraphExportException;
}
