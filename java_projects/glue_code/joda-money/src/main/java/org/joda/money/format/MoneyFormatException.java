package org.joda.money.format;

import java.io.IOException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;

public class MoneyFormatException extends RuntimeException {
  private static final long serialVersionUID = 87533576L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MoneyFormatException.py", "MoneyFormatException");
  private Value obj;

  public MoneyFormatException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void rethrowIOException() throws IOException {
    try {
      //
      // if (getCause() instanceof IOException) {
      // throw (IOException) getCause();
      // }
      //

      this.obj.invokeMember("rethrowIOException");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "MoneyFormatException.rethrowIOException");
    }
  }

  public static MoneyFormatException MoneyFormatException1(String message) {
    //
    // return new MoneyFormatException(message, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MoneyFormatException1", message).as(MoneyFormatException.class);
  }

  public MoneyFormatException(String message, Throwable cause) {
    //
    // super(message, cause);
    //

    this.obj = clz.invokeMember("__init__", message, cause);
  }
}
