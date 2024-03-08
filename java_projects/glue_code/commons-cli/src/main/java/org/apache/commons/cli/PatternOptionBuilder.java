package org.apache.commons.cli;

import java.io.File;
import java.io.FileInputStream;
import java.net.URL;
import java.util.Date;
import org.graalvm.polyglot.Value;

public class PatternOptionBuilder {
  public static final Class<URL> URL_VALUE = URL.class;
  public static final Class<File[]> FILES_VALUE = File[].class;
  public static final Class<File> FILE_VALUE = File.class;
  public static final Class<FileInputStream> EXISTING_FILE_VALUE = FileInputStream.class;
  public static final Class<?> CLASS_VALUE = Class.class;
  public static final Class<Date> DATE_VALUE = Date.class;
  public static final Class<Number> NUMBER_VALUE = Number.class;
  public static final Class<Object> OBJECT_VALUE = Object.class;
  public static final Class<String> STRING_VALUE = String.class;
  private static Value clz =
      ContextInitializer.getPythonClass("/PatternOptionBuilder.py", "PatternOptionBuilder");
  private Value obj;

  public PatternOptionBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Options parsePattern(final String pattern) {
    //
    // char opt = ' ';
    // boolean required = false;
    // Class<?> type = null;
    //
    // final Options options = new Options();
    //
    // for (int i = 0; i < pattern.length(); i++) {
    // final char ch = pattern.charAt(i);
    //
    // if (!isValueCode(ch)) {
    // if (opt != ' ') {
    // final Option option =
    // Option.builder1(String.valueOf(opt))
    // .hasArg1(type != null)
    // .required1(required)
    // .type(type)
    // .build();
    //
    // options.addOption0(option);
    // required = false;
    // type = null;
    // opt = ' ';
    // }
    //
    // opt = ch;
    // } else if (ch == '!') {
    // required = true;
    // } else {
    // type = (Class<?>) getValueClass(ch);
    // }
    // }
    //
    // if (opt != ' ') {
    // final Option option =
    // Option.builder1(String.valueOf(opt))
    // .hasArg1(type != null)
    // .required1(required)
    // .type(type)
    // .build();
    //
    // options.addOption0(option);
    // }
    //
    // return options;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("parsePattern", pattern).as(Options.class);
  }

  public static boolean isValueCode(final char ch) {
    //
    // return ch == '@' || ch == ':' || ch == '%' || ch == '+' || ch == '#' || ch == '<'
    // || ch == '>' || ch == '*' || ch == '/' || ch == '!';
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isValueCode", ch).as(boolean.class);
  }

  public static Object getValueClass(final char ch) {
    //
    // switch (ch) {
    // case '@':
    // return PatternOptionBuilder.OBJECT_VALUE;
    // case ':':
    // return PatternOptionBuilder.STRING_VALUE;
    // case '%':
    // return PatternOptionBuilder.NUMBER_VALUE;
    // case '+':
    // return PatternOptionBuilder.CLASS_VALUE;
    // case '#':
    // return PatternOptionBuilder.DATE_VALUE;
    // case '<':
    // return PatternOptionBuilder.EXISTING_FILE_VALUE;
    // case '>':
    // return PatternOptionBuilder.FILE_VALUE;
    // case '*':
    // return PatternOptionBuilder.FILES_VALUE;
    // case '/':
    // return PatternOptionBuilder.URL_VALUE;
    // }
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getValueClass", ch).as(Object.class);
  }
}
