package org.apache.commons.codec;

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

    if (exceptionType.equals("EncoderException")) {
      return new EncoderException(exceptionObj);
    }
    if (exceptionType.equals("DecoderException")) {
      return new DecoderException(exceptionObj);
    }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
