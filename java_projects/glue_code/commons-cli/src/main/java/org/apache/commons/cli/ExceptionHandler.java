package org.apache.commons.cli;

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

    if (exceptionType.equals("AmbiguousOptionException")) {
      return new AmbiguousOptionException(exceptionObj);
    }
    if (exceptionType.equals("AlreadySelectedException")) {
      return new AlreadySelectedException(exceptionObj);
    }
    if (exceptionType.equals("ParseException")) {
      return new ParseException(exceptionObj);
    }
    if (exceptionType.equals("UnrecognizedOptionException")) {
      return new UnrecognizedOptionException(exceptionObj);
    }
    if (exceptionType.equals("MissingOptionException")) {
      return new MissingOptionException(exceptionObj);
    }
    if (exceptionType.equals("MissingArgumentException")) {
      return new MissingArgumentException(exceptionObj);
    }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
