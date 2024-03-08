package org.apache.commons.validator.routines;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.routines.checkdigit.CheckDigit;
import org.graalvm.polyglot.Value;

public final class CodeValidator implements Serializable {
  private static final long serialVersionUID = 446960910870938233L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/CodeValidator.py", "CodeValidator");
  private Value obj;

  public CodeValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object validate(String input) {
    //
    //
    // if (input == null) {
    // return null;
    // }
    //
    // String code = input.trim();
    // if (code.length() == 0) {
    // return null;
    // }
    //
    // if (regexValidator != null) {
    // code = regexValidator.validate(code);
    // if (code == null) {
    // return null;
    // }
    // }
    //
    // if ((minLength >= 0 && code.length() < minLength)
    // || (maxLength >= 0 && code.length() > maxLength)) {
    // return null;
    // }
    //
    // if (checkdigit != null && !checkdigit.isValid(code)) {
    // return null;
    // }
    //
    // return code;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate", input).as(Object.class);
  }

  public boolean isValid(String input) {
    //
    // return (validate(input) != null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", input).as(boolean.class);
  }

  public RegexValidator getRegexValidator() {
    //
    // return regexValidator;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRegexValidator").as(RegexValidator.class);
  }

  public int getMaxLength() {
    //
    // return maxLength;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxLength").as(int.class);
  }

  public int getMinLength() {
    //
    // return minLength;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinLength").as(int.class);
  }

  public CheckDigit getCheckDigit() {
    //
    // return checkdigit;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCheckDigit").as(CheckDigit.class);
  }

  public static CodeValidator CodeValidator5(String regex, CheckDigit checkdigit) {
    //
    // return new CodeValidator(1, checkdigit, -1, null, -1, regex);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CodeValidator5", regex, checkdigit).as(CodeValidator.class);
  }

  public static CodeValidator CodeValidator4(String regex, int length, CheckDigit checkdigit) {
    //
    // return new CodeValidator(1, checkdigit, length, null, length, regex);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CodeValidator4", regex, length, checkdigit).as(CodeValidator.class);
  }

  public static CodeValidator CodeValidator2(RegexValidator regexValidator, CheckDigit checkdigit) {
    //
    // return new CodeValidator(0, checkdigit, -1, regexValidator, -1, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CodeValidator2", regexValidator, checkdigit).as(CodeValidator.class);
  }

  public static CodeValidator CodeValidator1(
      RegexValidator regexValidator, int length, CheckDigit checkdigit) {
    //
    // return new CodeValidator(0, checkdigit, length, regexValidator, length, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CodeValidator1", regexValidator, length, checkdigit)
        .as(CodeValidator.class);
  }

  public CodeValidator(
      int constructorId,
      CheckDigit checkdigit,
      int maxLength,
      RegexValidator regexValidator,
      int minLength,
      String regex) {
    //
    // if (constructorId == 0) {
    // this.regexValidator = regexValidator;
    // this.minLength = minLength;
    // this.maxLength = maxLength;
    // this.checkdigit = checkdigit;
    // } else {
    // if (regex != null && regex.length() > 0) {
    // this.regexValidator = RegexValidator.RegexValidator3(regex);
    // } else {
    // this.regexValidator = null;
    // }
    // this.minLength = minLength;
    // this.maxLength = maxLength;
    // this.checkdigit = checkdigit;
    // }
    //

    this.obj =
        clz.invokeMember(
            "__init__", constructorId, checkdigit, maxLength, regexValidator, minLength, regex);
  }
}
