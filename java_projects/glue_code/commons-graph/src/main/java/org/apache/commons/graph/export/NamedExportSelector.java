package org.apache.commons.graph.export;


public interface NamedExportSelector<V, E> extends ExportSelector<V, E> {
  ExportSelector<V, E> withName(String name);
}
