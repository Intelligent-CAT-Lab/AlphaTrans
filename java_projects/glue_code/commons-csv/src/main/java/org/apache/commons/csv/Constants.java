package org.apache.commons.csv;

import org.graalvm.polyglot.Value;

final class Constants {
  static final char US = 31;
  static final int UNDEFINED = -2;
  static final char TAB = '\t';
  static final String SQL_NULL_STRING = "\\N";
  static final char SP = ' ';
  static final char RS = 30;
  static final char PIPE = '|';
  static final String PARAGRAPH_SEPARATOR = "\u2029";
  static final String NEXT_LINE = "\u0085";
  static final String LINE_SEPARATOR = "\u2028";
  static final char LF = '\n';
  static final char FF = '\f';
  static final int END_OF_STREAM = -1;
  static final String[] EMPTY_STRING_ARRAY = {};
  static final String EMPTY = "";
  static final Character DOUBLE_QUOTE_CHAR = Character.valueOf('"');
  static final String CRLF = "\r\n";
  static final char CR = '\r';
  static final char COMMENT = '#';
  static final String COMMA = ",";
  static final char BACKSPACE = '\b';
  static final char BACKSLASH = '\\';
  private static Value clz = ContextInitializer.getPythonClass("/Constants.py", "Constants");
  private Value obj;

  public Constants(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  private Constants() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
