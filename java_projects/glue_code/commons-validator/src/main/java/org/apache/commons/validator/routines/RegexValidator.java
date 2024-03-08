package org.apache.commons.validator.routines;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class RegexValidator implements Serializable {
  private static final long serialVersionUID = -8832409930574867162L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/RegexValidator.py", "RegexValidator");
  private Value obj;

  public RegexValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder buffer = new StringBuilder();
    // buffer.append("RegexValidator{");
    // for (int i = 0; i < patterns.length; i++) {
    // if (i > 0) {
    // buffer.append(",");
    // }
    // buffer.append(patterns[i].pattern());
    // }
    // buffer.append("}");
    // return buffer.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public String validate(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    // for (int i = 0; i < patterns.length; i++) {
    // Matcher matcher = patterns[i].matcher(value);
    // if (matcher.matches()) {
    // int count = matcher.groupCount();
    // if (count == 1) {
    // return matcher.group(1);
    // }
    // StringBuilder buffer = new StringBuilder();
    // for (int j = 0; j < count; j++) {
    // String component = matcher.group(j + 1);
    // if (component != null) {
    // buffer.append(component);
    // }
    // }
    // return buffer.toString();
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate", value).as(String.class);
  }

  public String[] match(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    // for (int i = 0; i < patterns.length; i++) {
    // Matcher matcher = patterns[i].matcher(value);
    // if (matcher.matches()) {
    // int count = matcher.groupCount();
    // String[] groups = new String[count];
    // for (int j = 0; j < count; j++) {
    // groups[j] = matcher.group(j + 1);
    // }
    // return groups;
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("match", value).as(String[].class);
  }

  public boolean isValid(String value) {
    //
    // if (value == null) {
    // return false;
    // }
    // for (int i = 0; i < patterns.length; i++) {
    // if (patterns[i].matcher(value).matches()) {
    // return true;
    // }
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", value).as(boolean.class);
  }

  public static RegexValidator RegexValidator3(String regex) {
    //
    // return RegexValidator.RegexValidator2(regex, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("RegexValidator3", regex).as(RegexValidator.class);
  }

  public static RegexValidator RegexValidator2(String regex, boolean caseSensitive) {
    //
    // return new RegexValidator(new String[] {regex}, caseSensitive);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("RegexValidator2", regex, caseSensitive).as(RegexValidator.class);
  }

  public static RegexValidator RegexValidator1(String[] regexs) {
    //
    // return new RegexValidator(regexs, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("RegexValidator1", regexs).as(RegexValidator.class);
  }

  public RegexValidator(String[] regexs, boolean caseSensitive) {
    //
    //
    // if (regexs == null || regexs.length == 0) {
    // throw new IllegalArgumentException("Regular expressions are missing");
    // }
    // patterns = new Pattern[regexs.length];
    // int flags = (caseSensitive ? 0 : Pattern.CASE_INSENSITIVE);
    // for (int i = 0; i < regexs.length; i++) {
    // if (regexs[i] == null || regexs[i].length() == 0) {
    // throw new IllegalArgumentException("Regular expression[" + i + "] is missing");
    // }
    // patterns[i] = Pattern.compile(regexs[i], flags);
    // }
    //

    this.obj = clz.invokeMember("__init__", regexs, caseSensitive);
  }
}
