package org.apache.commons.cli;

import java.util.List;
import org.graalvm.polyglot.Value;

public class MissingOptionException extends ParseException {
  private static final long serialVersionUID = 8161889051578563249L;
  private static Value clz =
      ContextInitializer.getPythonClass("/MissingOptionException.py", "MissingOptionException");
  private Value obj;

  public MissingOptionException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public List getMissingOptions() {
    //
    // return missingOptions;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMissingOptions").as(List.class);
  }

  public static MissingOptionException MissingOptionException1(
      int constructorId, final List missingOptions, final String message) {
    //
    // if (constructorId == 1) {
    // return new MissingOptionException(
    // constructorId, missingOptions, createMessage(missingOptions));
    // }
    // return new MissingOptionException(constructorId, missingOptions, message);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MissingOptionException1", constructorId, missingOptions, message)
        .as(MissingOptionException.class);
  }

  public MissingOptionException(
      int constructorId, final List missingOptions, final String message) {
    //
    //
    // super(message);
    // if (constructorId == 1) {
    // this.missingOptions = missingOptions;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, missingOptions, message);
  }

  private static String createMessage(final List<?> missingOptions) {
    //
    // final StringBuilder buf = new StringBuilder("Missing required option");
    // buf.append(missingOptions.size() == 1 ? "" : "s");
    // buf.append(": ");
    //
    // final Iterator<?> it = missingOptions.iterator();
    // while (it.hasNext()) {
    // buf.append(it.next());
    // if (it.hasNext()) {
    // buf.append(", ");
    // }
    // }
    //
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createMessage", missingOptions).as(String.class);
  }
}
