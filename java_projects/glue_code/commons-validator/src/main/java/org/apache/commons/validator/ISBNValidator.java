package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class ISBNValidator {
  private static Value clz =
      ContextInitializer.getPythonClass("/ISBNValidator.py", "ISBNValidator");
  private Value obj;

  public ISBNValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isValid(String isbn) {
    //
    // return org.apache.commons.validator.routines.ISBNValidator.getInstance0()
    // .isValidISBN10(isbn);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", isbn).as(boolean.class);
  }

  public ISBNValidator() {
    //
    // super();
    //

    this.obj = clz.invokeMember("__init__");
  }
}
