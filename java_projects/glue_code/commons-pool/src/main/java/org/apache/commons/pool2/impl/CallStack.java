package org.apache.commons.pool;

import java.io.PrintWriter;

public interface CallStack {
  boolean printStackTrace(final PrintWriter writer);

  void fillInStackTrace();

  void clear();
}
