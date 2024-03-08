package org.apache.commons.cli;

import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class OptionValidator {
  private static Value clz =
      ContextInitializer.getPythonClass("/OptionValidator.py", "OptionValidator");
  private Value obj;

  public OptionValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static String validate(final String option) throws IllegalArgumentException {
    try {
      //
      // if (option == null) {
      // return null;
      // }
      //
      // if (option.length() == 1) {
      // final char ch = option.charAt(0);
      //
      // if (!isValidOpt(ch)) {
      // throw new IllegalArgumentException("Illegal option name '" + ch + "'");
      // }
      // } else {
      // for (final char ch : option.toCharArray()) {
      // if (!isValidChar(ch)) {
      // throw new IllegalArgumentException(
      // "The option '"
      // + option
      // + "' contains an illegal "
      // + "character : '"
      // + ch
      // + "'");
      // }
      // }
      // }
      // return option;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("validate", option).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "OptionValidator.validate");
    }
  }

  private static boolean isValidOpt(final char c) {
    //
    // return isValidChar(c) || c == '?' || c == '@';
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isValidOpt", c).as(boolean.class);
  }

  private static boolean isValidChar(final char c) {
    //
    // return Character.isJavaIdentifierPart(c);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isValidChar", c).as(boolean.class);
  }
}
