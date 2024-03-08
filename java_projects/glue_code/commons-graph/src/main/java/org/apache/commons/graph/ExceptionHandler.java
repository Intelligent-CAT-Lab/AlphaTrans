package org.apache.commons.graph;

import org.apache.commons.graph.coloring.NotEnoughColorsException;
import org.apache.commons.graph.export.GraphExportException;
import org.apache.commons.graph.shortestpath.NegativeWeightedCycleException;
import org.apache.commons.graph.shortestpath.PathNotFoundException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

/**
 * Provides a method to handle exceptions from Polyglot.
 *
 * <p>e: the PolyglotException object to handle thrower: the class and method that threw the
 * exception (as "Class.method")
 */
public final class ExceptionHandler {
  public static Exception handle(PolyglotException e, String thrower) {
    String exceptionType = e.getMessage().split(":")[0];
    String exceptionMessage = e.getMessage().split(": ")[1];
    Value exceptionObj = e.getGuestObject();

    if (exceptionType.equals("GraphExportException")) {
      return new GraphExportException(exceptionObj);
    }
    if (exceptionType.equals("NotEnoughColorsException")) {
      return new NotEnoughColorsException(exceptionObj);
    }
    if (exceptionType.equals("GraphException")) {
      return new GraphException(exceptionObj);
    }
    if (exceptionType.equals("NegativeWeightedCycleException")) {
      return new NegativeWeightedCycleException(exceptionObj);
    }
    if (exceptionType.equals("PathNotFoundException")) {
      return new PathNotFoundException(exceptionObj);
    }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
