package org.apache.commons.validator.routines;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit;
import org.graalvm.polyglot.Value;

public class ISSNValidator implements Serializable {
  private static final ISSNValidator ISSN_VALIDATOR = new ISSNValidator();
  private static final CodeValidator EAN_VALIDATOR =
      CodeValidator.CodeValidator4(EAN_ISSN_REGEX, EAN_ISSN_LEN, EAN13CheckDigit.EAN13_CHECK_DIGIT);
  private static final CodeValidator VALIDATOR =
      CodeValidator.CodeValidator4(ISSN_REGEX, ISSN_LEN, ISSNCheckDigit.ISSN_CHECK_DIGIT);
  private static final int EAN_ISSN_LEN = 13;
  private static final String EAN_ISSN_REGEX = "^(977)(?:(\\d{10}))$";
  private static final String ISSN_PREFIX = "977";
  private static final int ISSN_LEN = 8;
  private static final String ISSN_REGEX =
      "(?:ISSN )?(\\d{4})-(\\d{3}[0-9X])$"; // We don't include the '-' in the code, so it is
  private static final long serialVersionUID = 4319515687976420405L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/ISSNValidator.py", "ISSNValidator");
  private Value obj;

  public ISSNValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String extractFromEAN13(String ean13) {
    //
    // String input = ean13.trim();
    // if (input.length() != EAN_ISSN_LEN) {
    // throw new IllegalArgumentException(
    // "Invalid length " + input.length() + " for '" + input + "'");
    // }
    // if (!input.startsWith(ISSN_PREFIX)) {
    // throw new IllegalArgumentException(
    // "Prefix must be " + ISSN_PREFIX + " to contain an ISSN: '" + ean13 + "'");
    // }
    // Object result = validateEan(input);
    // if (result == null) {
    // return null;
    // }
    // input = result.toString();
    // try {
    // String issnBase = input.substring(3, 10); // TODO: how to derive these
    // String checkDigit = ISSNCheckDigit.ISSN_CHECK_DIGIT.calculate(issnBase);
    // String issn = issnBase + checkDigit;
    // return issn;
    // } catch (CheckDigitException e) { // Should not happen
    // throw new IllegalArgumentException(
    // "Check digit error for '" + ean13 + "' - " + e.getMessage());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("extractFromEAN13", ean13).as(String.class);
  }

  public String convertToEAN13(String issn, String suffix) {
    //
    //
    // if (suffix == null || !suffix.matches("\\d\\d")) {
    // throw new IllegalArgumentException("Suffix must be two digits: '" + suffix + "'");
    // }
    //
    // Object result = validate(issn);
    // if (result == null) {
    // return null;
    // }
    //
    // final String input = result.toString();
    // String ean13 = ISSN_PREFIX + input.substring(0, input.length() - 1) + suffix;
    // try {
    // String checkDigit = EAN13CheckDigit.EAN13_CHECK_DIGIT.calculate(ean13);
    // ean13 += checkDigit;
    // return ean13;
    // } catch (CheckDigitException e) { // Should not happen
    // throw new IllegalArgumentException(
    // "Check digit error for '" + ean13 + "' - " + e.getMessage());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("convertToEAN13", issn, suffix).as(String.class);
  }

  public Object validate(String code) {
    //
    // return VALIDATOR.validate(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate", code).as(Object.class);
  }

  public boolean isValid(String code) {
    //
    // return VALIDATOR.isValid(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public Object validateEan(String code) {
    //
    // return EAN_VALIDATOR.validate(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateEan", code).as(Object.class);
  }

  public static ISSNValidator getInstance() {
    //
    // return ISSN_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(ISSNValidator.class);
  }
}
