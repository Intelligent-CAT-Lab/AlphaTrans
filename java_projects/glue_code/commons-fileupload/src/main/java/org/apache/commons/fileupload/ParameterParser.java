package org.apache.commons.fileupload;

import java.util.Map;
import org.graalvm.polyglot.Value;

public class ParameterParser {
  private boolean lowerCaseNames = false;
  private int i2 = 0;
  private int i1 = 0;
  private int len = 0;
  private int pos = 0;
  private char[] chars = null;
  private static Value clz = ContextInitializer.getPythonClass("<placeholder>", "ParameterParser");
  private Value obj;

  public ParameterParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Map<String, String> parse3(
      final char[] charArray, int offset, int length, char separator) {
    //
    //
    // if (charArray == null) {
    // return new HashMap<String, String>();
    // }
    // HashMap<String, String> params = new HashMap<String, String>();
    // this.chars = charArray;
    // this.pos = offset;
    // this.len = length;
    //
    // String paramName = null;
    // String paramValue = null;
    // while (hasChar()) {
    // paramName = parseToken(new char[] {'=', separator});
    // paramValue = null;
    // if (hasChar() && (charArray[pos] == '=')) {
    // pos++; // skip '='
    // paramValue = parseQuotedToken(new char[] {separator});
    //
    // if (paramValue != null) {
    // try {
    // paramValue = MimeUtility.decodeText(paramValue);
    // } catch (UnsupportedEncodingException e) {
    // }
    // }
    // }
    // if (hasChar() && (charArray[pos] == separator)) {
    // pos++; // skip separator
    // }
    // if ((paramName != null) && (paramName.length() > 0)) {
    // if (this.lowerCaseNames) {
    // paramName = paramName.toLowerCase(Locale.ENGLISH);
    // }
    //
    // params.put(paramName, paramValue);
    // }
    // }
    // return params;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse3", charArray, offset, length, separator).as(Map.class);
  }

  public Map<String, String> parse2(final char[] charArray, char separator) {
    //
    // if (charArray == null) {
    // return new HashMap<String, String>();
    // }
    // return parse3(charArray, 0, charArray.length, separator);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse2", charArray, separator).as(Map.class);
  }

  public Map<String, String> parse1(final String str, char separator) {
    //
    // if (str == null) {
    // return new HashMap<String, String>();
    // }
    // return parse2(str.toCharArray(), separator);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse1", str, separator).as(Map.class);
  }

  public Map<String, String> parse0(final String str, char[] separators) {
    //
    // if (separators == null || separators.length == 0) {
    // return new HashMap<String, String>();
    // }
    // char separator = separators[0];
    // if (str != null) {
    // int idx = str.length();
    // for (char separator2 : separators) {
    // int tmp = str.indexOf(separator2);
    // if (tmp != -1 && tmp < idx) {
    // idx = tmp;
    // separator = separator2;
    // }
    // }
    // }
    // return parse1(str, separator);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse0", str, separators).as(Map.class);
  }

  public void setLowerCaseNames(boolean b) {
    //
    // this.lowerCaseNames = b;
    //

    obj.invokeMember("setLowerCaseNames", b);
  }

  public boolean isLowerCaseNames() {
    //
    // return this.lowerCaseNames;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isLowerCaseNames").as(boolean.class);
  }

  public ParameterParser() {
    //
    // super();
    //

    this.obj = clz.invokeMember("__init__");
  }

  private String parseQuotedToken(final char[] terminators) {
    //
    // char ch;
    // i1 = pos;
    // i2 = pos;
    // boolean quoted = false;
    // boolean charEscaped = false;
    // while (hasChar()) {
    // ch = chars[pos];
    // if (!quoted && isOneOf(ch, terminators)) {
    // break;
    // }
    // if (!charEscaped && ch == '"') {
    // quoted = !quoted;
    // }
    // charEscaped = (!charEscaped && ch == '\\');
    // i2++;
    // pos++;
    // }
    // return getToken(true);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parseQuotedToken", terminators).as(String.class);
  }

  private String parseToken(final char[] terminators) {
    //
    // char ch;
    // i1 = pos;
    // i2 = pos;
    // while (hasChar()) {
    // ch = chars[pos];
    // if (isOneOf(ch, terminators)) {
    // break;
    // }
    // i2++;
    // pos++;
    // }
    // return getToken(false);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parseToken", terminators).as(String.class);
  }

  private boolean isOneOf(char ch, final char[] charray) {
    //
    // boolean result = false;
    // for (char element : charray) {
    // if (ch == element) {
    // result = true;
    // break;
    // }
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOneOf", ch, charray).as(boolean.class);
  }

  private String getToken(boolean quoted) {
    //
    // while ((i1 < i2) && (Character.isWhitespace(chars[i1]))) {
    // i1++;
    // }
    // while ((i2 > i1) && (Character.isWhitespace(chars[i2 - 1]))) {
    // i2--;
    // }
    // if (quoted && ((i2 - i1) >= 2) && (chars[i1] == '"') && (chars[i2 - 1] == '"')) {
    // i1++;
    // i2--;
    // }
    // String result = null;
    // if (i2 > i1) {
    // result = new String(chars, i1, i2 - i1);
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getToken", quoted).as(String.class);
  }

  private boolean hasChar() {
    //
    // return this.pos < this.len;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasChar").as(boolean.class);
  }
}
