package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

public class BasicParser extends Parser {
  private static Value clz = ContextInitializer.getPythonClass("/BasicParser.py", "BasicParser");
  private Value obj;

  public BasicParser(Value obj) {
    this.obj = obj;
  }

  public BasicParser() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  protected String[] flatten(
      @SuppressWarnings("unused") final Options options,
      final String[] arguments,
      @SuppressWarnings("unused") final boolean stopAtNonOption) {
    //
    // return arguments;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("flatten", options, arguments, stopAtNonOption).as(String[].class);
  }
}
